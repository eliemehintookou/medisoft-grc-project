# -*- coding: utf-8 -*-
"""Revue des accès MediSoft — rapprochement RH / Entra ID / AWS / GitHub.

Usage : python access_review.py [date_de_reference AAAA-MM-JJ]

Le script compare les droits réellement attribués (exports des systèmes) à la
source de vérité RH et à la matrice des rôles, puis produit la liste des
anomalies à faire valider par les managers et le RSSI (MS-POL-02 §7).
"""
import csv
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

from matrice import MATRICE, COMPTES_TECHNIQUES, GROUPES_SENSIBLES, AWS_SENSIBLES, SEUIL_INACTIVITE_JOURS

BASE = Path(__file__).resolve().parent.parent
DATA, OUT = BASE / "data", BASE / "output"
REF = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date(2026, 12, 15)
ORDRE = {"Critique": 0, "Élevée": 1, "Moyenne": 2, "Faible": 3}


def lire(nom):
    with open(DATA / nom, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=";"))


def dt(s):
    return date.fromisoformat(s) if s else None


rh = {r["email"]: r for r in lire("export_rh.csv")}
rh_par_mat = {r["matricule"]: r for r in rh.values()}
entra = lire("export_entra_id.csv")
aws = lire("export_aws_identity_center.csv")
gh = lire("export_github.csv")

aws_par_user = defaultdict(list)
for a in aws:
    aws_par_user[a["utilisateur"]].append(f"{a['compte_aws']}:{a['permission_set']}")

findings = []
deja_signale = set()   # comptes déjà traités par une règle « de fond »


def ajoute(regle, gravite, systeme, compte, personne, constat, reco, decideur):
    findings.append(dict(regle=regle, gravite=gravite, systeme=systeme, compte=compte, personne=personne,
                         constat=constat, recommandation=reco, decideur=decideur))


def qui(r):
    return f"{r['prenom']} {r['nom']} ({r['matricule']}, {r['role']})" if r else "Inconnu (aucune fiche RH)"


def parti(r):
    """Renvoie la date à partir de laquelle la personne ne devrait plus avoir d'accès, sinon None."""
    if not r:
        return None
    if r["date_sortie"] and dt(r["date_sortie"]) <= REF:
        return dt(r["date_sortie"])
    if r["fin_mission"] and dt(r["fin_mission"]) < REF:
        return dt(r["fin_mission"])
    return None


# ---------------------------------------------------------------- Entra ID
emp_ids = defaultdict(list)
for c in entra:
    if c["employee_id"]:
        emp_ids[c["employee_id"]].append(c)

for c in entra:
    upn, actif = c["upn"], c["compte_actif"] == "Oui"
    groupes = [g for g in c["groupes"].split(";") if g]
    r = rh.get(upn) or (rh_par_mat.get(c["employee_id"]) if c["employee_id"] else None)
    derniere = dt(c["derniere_connexion"])

    # R12 — comptes techniques
    if upn in COMPTES_TECHNIQUES:
        if c["type_compte"] == "Service" and derniere:
            ajoute("R12 Compte de service utilisé en interactif", "Élevée", "Entra ID", upn,
                   f"Compte technique — propriétaire : {COMPTES_TECHNIQUES[upn][1]}",
                   f"Connexion interactive le {derniere:%d/%m/%Y} sur un compte de service (mot de passe sans expiration). "
                   "Un compte de service ne doit jamais servir à se connecter : identifiants probablement partagés.",
                   "Changer le secret, le stocker dans AWS Secrets Manager, bloquer la connexion interactive (accès conditionnel), identifier l'utilisateur",
                   "Resp. Ops + RSSI")
            deja_signale.add(upn)
        continue

    # R06 — doublon
    if c["employee_id"] and len(emp_ids[c["employee_id"]]) > 1 and upn != (r or {}).get("email"):
        ajoute("R06 Compte en doublon", "Élevée" if actif else "Faible", "Entra ID", upn, qui(r),
               f"Deuxième compte pour la même personne (compte principal : {r['email'] if r else '?'}). "
               f"Dernière connexion le {derniere:%d/%m/%Y}, MFA {'non ' if c['mfa_enregistre'] == 'Non' else ''}enregistré.",
               "Supprimer le compte en doublon après vérification avec l'intéressé", "Manager + Resp. Ops")
        deja_signale.add(upn)
        continue

    if r is None:
        sensibles = [g for g in groupes if g in GROUPES_SENSIBLES]
        if c["type_compte"] == "Externe":
            ajoute("R05 Compte invité sans référence", "Moyenne", "Entra ID", upn, "Externe sans fiche RH ni sponsor",
                   f"Compte invité actif depuis le {dt(c['date_creation']):%d/%m/%Y}, dernière connexion le {derniere:%d/%m/%Y}, "
                   "sans date d'expiration ni sponsor interne identifié.",
                   "Identifier le sponsor ; désactiver si la mission est terminée ; imposer une date d'expiration aux invités",
                   "RSSI")
        else:
            generique = upn.split("@")[0] in ("support", "admin", "contact", "compta", "info")
            if generique:
                ajoute("R04 Compte générique partagé", "Critique" if sensibles else "Élevée", "Entra ID", upn,
                       "Compte partagé (aucune personne identifiée)",
                       f"Compte générique actif, membre de {', '.join(sensibles) or 'groupes standards'}, MFA "
                       f"{'non ' if c['mfa_enregistre'] == 'Non' else ''}enregistré, mot de passe sans expiration, "
                       f"dernière connexion le {derniere:%d/%m/%Y}. Les accès aux dossiers patients ne sont pas imputables.",
                       "Supprimer le compte ; créer des comptes nominatifs ; boîte partagée sans droit de connexion",
                       "Resp. Support + RSSI")
            else:
                ajoute("R04 Compte orphelin", "Critique" if sensibles else "Élevée", "Entra ID", upn,
                       "Inconnu (aucune fiche RH)",
                       f"Compte actif sans propriétaire, créé le {dt(c['date_creation']):%d/%m/%Y}, membre de "
                       f"{', '.join(sensibles) or ', '.join(groupes)}, MFA {'non ' if c['mfa_enregistre'] == 'Non' else ''}enregistré, "
                       f"dernière connexion le {derniere:%d/%m/%Y}.",
                       "Désactiver immédiatement ; analyser les journaux de connexion ; supprimer après 30 jours sans réclamation",
                       "RSSI")
        deja_signale.add(upn)
        continue

    # R01 / R03 — personne partie ou mission terminée avec compte actif
    fin = parti(r)
    if fin and actif:
        usage_apres = derniere and derniere > fin
        regle = "R03 Prestataire terminé encore actif" if r["matricule"].startswith("P") else "R01 Départ non traité"
        ajoute(regle, "Critique" if usage_apres else "Élevée", "Entra ID", upn, qui(r),
               f"{'Fin de mission' if r['matricule'].startswith('P') else 'Sortie'} le {fin:%d/%m/%Y}, compte toujours actif. "
               + (f"CONNEXION APRÈS LE DÉPART le {derniere:%d/%m/%Y} : accès possiblement illégitime."
                  if usage_apres else f"Dernière connexion le {derniere:%d/%m/%Y}."),
               "Désactiver immédiatement" + (" ; ouvrir un incident de sécurité et analyser les actions réalisées"
                                              if usage_apres else ""),
               "RSSI" if usage_apres else "Manager + Resp. Ops")
        deja_signale.add(upn)
        continue
    if fin:
        continue

    # R07 — groupes hors matrice
    autorises = set(MATRICE[r["role"]][1])
    for g in groupes:
        if g in autorises:
            continue
        mobilite = r["role_precedent"] and g in MATRICE[r["role_precedent"]][1]
        grav = "Critique" if g in ("GRP-SUPPORT-DONNEES-PATIENTS", "GRP-ADMIN-ENTRA") else (
            "Élevée" if g in GROUPES_SENSIBLES else "Moyenne")
        constat = f"Membre de {g} ({GROUPES_SENSIBLES.get(g, 'groupe métier')}), non prévu pour le rôle {r['role']}."
        if mobilite:
            constat += f" Droit hérité de l'ancien poste ({r['role_precedent']}) — mobilité du {dt(r['date_mobilite']):%d/%m/%Y}."
        ajoute("R07 Droits cumulés après mobilité" if mobilite else "R07 Droit excédentaire", grav, "Entra ID", upn, qui(r),
               constat, f"Retirer {g}", "Manager")

    # R10 — MFA
    if actif and c["mfa_enregistre"] == "Non":
        privilegie = any(g in GROUPES_SENSIBLES for g in groupes) or any(
            d.split(":")[1] in AWS_SENSIBLES for d in aws_par_user.get(upn, []))
        ajoute("R10 MFA non enregistré", "Élevée" if privilegie else "Moyenne", "Entra ID", upn, qui(r),
               "Aucune méthode MFA enregistrée" + (" sur un compte disposant d'accès sensibles." if privilegie else "."),
               "Imposer l'enregistrement MFA (accès conditionnel) sous 48 h", "Resp. Ops")

    # R11 — inactivité
    if actif and derniere and (REF - derniere).days > SEUIL_INACTIVITE_JOURS:
        jours = (REF - derniere).days
        if r["absence_longue"] == "Oui":
            ajoute("R11 Compte inactif (absence justifiée)", "Faible", "Entra ID", upn, qui(r),
                   f"Aucune connexion depuis {jours} jours ; absence longue déclarée par la DRH.",
                   "Désactiver pendant l'absence et réactiver au retour (exception documentée)", "Manager")
        else:
            ajoute("R11 Compte inactif", "Moyenne", "Entra ID", upn, qui(r),
                   f"Aucune connexion depuis {jours} jours (seuil : {SEUIL_INACTIVITE_JOURS}).",
                   "Confirmer le besoin avec le manager, sinon désactiver", "Manager")

# ---------------------------------------------------------------- AWS
for user, droits in aws_par_user.items():
    if user in COMPTES_TECHNIQUES:
        attendus = set(COMPTES_TECHNIQUES[user][2])
        for dr in droits:
            if dr not in attendus:
                ajoute("R08 Droit AWS excédentaire", "Élevée", "AWS", user, "Compte technique", f"{dr} non déclaré", "Retirer", "RSSI")
        continue
    r = rh.get(user)
    fin = parti(r)
    if fin:
        sensibles = [d for d in droits if d.split(":")[1] in AWS_SENSIBLES]
        ajoute("R02 Accès résiduel après départ", "Critique" if any(d.startswith("prod:") for d in sensibles) else "Élevée",
               "AWS", user, qui(r),
               f"Sortie le {fin:%d/%m/%Y} ; affectations toujours présentes : {', '.join(droits)}. "
               "Le compte Entra est désactivé, mais les affectations doivent être supprimées (clés d'accès éventuelles, réactivation).",
               "Supprimer toutes les affectations ; vérifier l'absence de clés d'accès IAM et de sessions actives", "Resp. Ops")
        continue
    if r is None:
        ajoute("R04 Compte orphelin", "Critique", "AWS", user, "Inconnu", f"Affectations : {', '.join(droits)}", "Supprimer", "RSSI")
        continue
    autorises = set(MATRICE[r["role"]][2])
    for dr in droits:
        if dr in autorises:
            continue
        compte_aws, ps = dr.split(":")
        mobilite = r["role_precedent"] and dr in MATRICE[r["role_precedent"]][2]
        grav = "Critique" if ps == "AdministratorAccess" and r["role"] in ("DEV",) else (
            "Élevée" if ps in AWS_SENSIBLES or compte_aws == "prod" else "Moyenne")
        constat = f"{ps} sur le compte {compte_aws}, non prévu pour le rôle {r['role']}."
        if ps == "AdministratorAccess":
            constat += " AdministratorAccess est réservé aux comptes d'urgence (MS-POL-02 §5)."
        if mobilite:
            constat += f" Droit hérité de l'ancien poste ({r['role_precedent']})."
        ajoute("R08 Droits cumulés après mobilité" if mobilite else "R08 Droit AWS excédentaire", grav, "AWS", user, qui(r),
               constat, "Retirer l'affectation ; passer par l'élévation à la demande si besoin ponctuel", "RSSI")

# ---------------------------------------------------------------- GitHub
for g in gh:
    r = rh.get(g["email"])
    fin = parti(r)
    if fin:
        typ = "Fin de mission" if r["matricule"].startswith("P") else "Sortie"
        ajoute("R02 Accès résiduel après départ", "Élevée", "GitHub", g["login"], qui(r),
               f"{typ} le {fin:%d/%m/%Y} ; toujours {g['role_org']} de l'organisation (équipes : {g['equipes'] or '—'}). "
               "Accès au code source de MediSoft Care.",
               "Retirer de l'organisation ; faire tourner les secrets auxquels la personne avait accès", "CTO")
        continue
    if r is None:
        ajoute("R04 Compte orphelin", "Élevée", "GitHub", g["login"], "Inconnu", "Membre sans fiche RH", "Retirer", "CTO")
        continue
    attendu = MATRICE[r["role"]][3]
    if g["role_org"] != attendu:
        grav = "Élevée" if g["role_org"] == "owner" else "Moyenne"
        ajoute("R09 Rôle GitHub excédentaire", grav, "GitHub", g["login"], f"{qui(r)} — {r['type_contrat']}",
               f"Rôle « {g['role_org']} » au lieu de « {attendu} ». Un owner peut modifier la sécurité de l'organisation, "
               "supprimer des dépôts et inviter des membres.",
               f"Rétrograder en « {attendu} »", "CTO")
    if g["deux_facteurs"] != "Oui":
        ajoute("R13 2FA GitHub désactivée", "Élevée", "GitHub", g["login"], qui(r),
               "Authentification à deux facteurs désactivée sur un compte ayant accès au code source.",
               "Imposer la 2FA au niveau de l'organisation (paramètre « Require 2FA »)", "CTO")

# ---------------------------------------------------------------- Sortie
findings.sort(key=lambda f: (ORDRE[f["gravite"]], f["regle"], f["compte"]))
for i, f in enumerate(findings, 1):
    f["id"] = f"F-{i:03d}"
OUT.mkdir(exist_ok=True)
cols = ["id", "regle", "gravite", "systeme", "compte", "personne", "constat", "recommandation", "decideur"]
with open(OUT / "anomalies.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=cols, delimiter=";")
    w.writeheader()
    w.writerows([{k: f[k] for k in cols} for f in findings])

stats = defaultdict(int)
for f in findings:
    stats[f["gravite"]] += 1
print(f"Revue des accès au {REF:%d/%m/%Y} — {len(entra)} comptes Entra, {len(aws)} affectations AWS, {len(gh)} membres GitHub")
print(f"{len(findings)} anomalies : " + ", ".join(f"{k} {stats[k]}" for k in ORDRE if stats[k]))
for f in findings:
    print(f"{f['id']} [{f['gravite']:8}] {f['systeme']:8} {f['regle']:40} {f['compte']}")
