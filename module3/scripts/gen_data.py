# -*- coding: utf-8 -*-
"""Génère les exports fictifs utilisés pour la revue des accès du T4 2026.

Les anomalies sont introduites volontairement (voir le corrigé dans le README).
Données entièrement fictives. Date de référence : 15/12/2026.
"""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

from matrice import MATRICE, COMPTES_TECHNIQUES

random.seed(2026)
REF = date(2026, 12, 15)
DATA = Path(__file__).resolve().parent.parent / "data"
DOM = "medisoft.example"

PRENOMS = ["Lucas", "Emma", "Hugo", "Léa", "Louis", "Chloé", "Nathan", "Manon", "Jules", "Camille", "Adam", "Sarah",
           "Arthur", "Inès", "Raphaël", "Jade", "Gabriel", "Louise", "Théo", "Alice", "Tom", "Lina", "Noah", "Zoé",
           "Ethan", "Clara", "Paul", "Anna", "Maxime", "Julie", "Yanis", "Lucie", "Sacha", "Eva", "Mathis", "Nina",
           "Enzo", "Romane", "Antoine", "Margaux", "Victor", "Océane", "Samuel", "Laura", "Baptiste", "Elsa", "Rayan",
           "Mila", "Thomas", "Pauline", "Kylian", "Aya", "Martin", "Lou", "Axel", "Agathe", "Malo", "Salomé", "Timéo",
           "Charlotte", "Mehdi", "Fatou", "Kofi", "Awa", "Simon", "Yasmine", "Bastien", "Amina", "Quentin", "Ambre",
           "Florian", "Mathilde", "Dylan", "Héloïse", "Kevin", "Céline", "Olivier", "Sophie", "Damien", "Elise",
           "Rémi", "Marion", "Alexis", "Justine", "Cédric", "Aurélie", "Fabien", "Nadia", "Loïc", "Estelle",
           "Guillaume", "Hélène", "Jérôme", "Isabelle", "Karim", "Morgane", "Nicolas", "Ophélie", "Pierre", "Rose"]
NOMS = ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand", "Leroy", "Moreau", "Simon",
        "Laurent", "Lefebvre", "Michel", "Garcia", "David", "Bertrand", "Roux", "Vincent", "Fournier", "Morel",
        "Girard", "Andre", "Lefevre", "Mercier", "Dupont", "Lambert", "Bonnet", "Francois", "Martinez", "Legrand",
        "Garnier", "Faure", "Rousseau", "Blanc", "Guerin", "Muller", "Henry", "Roussel", "Nicolas", "Perrin",
        "Morin", "Mathieu", "Clement", "Gauthier", "Dumont", "Lopez", "Fontaine", "Chevalier", "Robin", "Masson",
        "Sanchez", "Gerard", "Nguyen", "Boyer", "Denis", "Lemaire", "Duval", "Joly", "Gautier", "Roger", "Roche",
        "Roy", "Noel", "Meyer", "Lucas", "Meunier", "Jean", "Perez", "Marchand", "Dufour", "Blanchard", "Gillet",
        "Barbier", "Brun", "Dumas", "Brunet", "Schmitt", "Leroux", "Colin", "Fernandez", "Pierre", "Renard",
        "Arnaud", "Rolland", "Caron", "Aubert", "Giraud", "Leclerc", "Vidal", "Bourgeois", "Renaud", "Lemoine",
        "Picard", "Gaillard", "Philippe", "Leclercq", "Lacroix", "Fabre", "Dupuis"]

used = set()


def nom_unique():
    while True:
        p, n = random.choice(PRENOMS), random.choice(NOMS)
        if (p, n) not in used:
            used.add((p, n))
            return p, n


def ascii_(s):
    tr = str.maketrans("éèêëàâäîïôöùûüçÉÈÎ", "eeeeaaaiioouuucEEI")
    return s.translate(tr).lower().replace(" ", "")


def d(s):
    return date.fromisoformat(s)


# ------------------------------------------------------------------ Population RH
# (service, rôle, type, nombre)
PLAN = [
    ("Direction", "DIR", "Salarié", 2), ("R&D", "CTO", "Salarié", 1), ("R&D", "DEV-LEAD", "Salarié", 3),
    ("R&D", "DEV", "Salarié", 27), ("R&D", "DEV", "Alternant", 2), ("R&D", "DEV", "Stagiaire", 1),
    ("Ops", "OPS-LEAD", "Salarié", 1), ("Ops", "OPS", "Salarié", 5),
    ("Support", "SUP-N1", "Salarié", 8), ("Support", "SUP-N2", "Salarié", 6),
    ("Commercial", "COM", "Salarié", 11),
    ("Sécurité", "RSSI", "Salarié", 1), ("Juridique", "DPO", "Salarié", 1), ("RH", "RH", "Salarié", 3),
    ("Finance", "FIN", "Salarié", 4), ("Juridique", "JUR", "Salarié", 2), ("Marketing", "MKT", "Salarié", 5),
]
# + 2 personnes en mobilité (1 Ops devenu Dev, 1 Support N2 devenu commercial) = 85 actifs

rh = []
seq = 1


def ajoute(service, role, typ, entree, sortie="", fin_mission="", role_prec="", date_mob="", absence="Non", prestataire=False):
    global seq
    p, n = nom_unique()
    mat = (f"P{seq:03d}" if prestataire else f"E{seq:03d}")
    seq += 1
    rec = dict(matricule=mat, prenom=p, nom=n, email=f"{ascii_(p)}.{ascii_(n)}@{DOM}", service=service,
               role=role, poste=MATRICE[role][0], type_contrat=typ, date_entree=entree, date_sortie=sortie,
               fin_mission=fin_mission, role_precedent=role_prec, date_mobilite=date_mob, absence_longue=absence)
    rh.append(rec)
    return rec


for service, role, typ, nb in PLAN:
    for _ in range(nb):
        jours = random.randint(60, 2400)
        ajoute(service, role, typ, (REF - timedelta(days=jours)).isoformat())

# Mobilités
mob_ops_dev = ajoute("R&D", "DEV", "Salarié", "2022-03-01", role_prec="OPS", date_mob="2026-07-01")
mob_sup_com = ajoute("Commercial", "COM", "Salarié", "2021-09-15", role_prec="SUP-N2", date_mob="2026-09-01")

# Départs 2026
dep_dev = ajoute("R&D", "DEV", "Salarié", "2023-01-09", sortie="2026-09-30")
dep_com = ajoute("Commercial", "COM", "Salarié", "2024-05-02", sortie="2026-10-31")
dep_ops = ajoute("Ops", "OPS", "Salarié", "2021-11-02", sortie="2026-08-14")
dep_ok1 = ajoute("Support", "SUP-N1", "Salarié", "2024-02-01", sortie="2026-06-30")
dep_ok2 = ajoute("R&D", "DEV", "Salarié", "2022-06-13", sortie="2026-03-31")
dep_ok3 = ajoute("Marketing", "MKT", "Salarié", "2025-01-06", sortie="2026-11-30")

# Prestataires
pr_mobile = ajoute("R&D", "PRESTA-DEV", "Prestataire", "2026-02-01", fin_mission="2027-03-31", prestataire=True)
pr_ops = ajoute("Ops", "PRESTA-OPS", "Prestataire", "2026-10-01", fin_mission="2027-01-31", prestataire=True)
pr_fin1 = ajoute("R&D", "PRESTA-DEV", "Prestataire", "2025-06-01", fin_mission="2025-12-19", prestataire=True)
pr_fin2 = ajoute("R&D", "PRESTA-DEV", "Prestataire", "2025-11-03", fin_mission="2026-04-30", prestataire=True)
pr_fin3 = ajoute("R&D", "PRESTA-DEV", "Prestataire", "2026-01-05", fin_mission="2026-06-30", prestataire=True)

actifs = [r for r in rh if not r["date_sortie"] and not r["matricule"].startswith("P")]
assert len(actifs) == 85, len(actifs)


def pick(role, exclude=()):
    for r in actifs:
        if r["role"] == role and r["matricule"] not in exclude and r not in (mob_ops_dev, mob_sup_com):
            return r
    raise ValueError(role)


# Personnes concernées par des anomalies
maternite = pick("SUP-N1")
maternite["absence_longue"] = "Oui"
cto = pick("CTO")
ops_lead = pick("OPS-LEAD")
dev_admin = pick("DEV")
stagiaire = next(r for r in actifs if r["type_contrat"] == "Stagiaire")
dev_2fa = pick("DEV", exclude={dev_admin["matricule"]})
dev_doublon = pick("DEV", exclude={dev_admin["matricule"], dev_2fa["matricule"]})
com_ops = pick("COM")
com_mfa = pick("COM", exclude={com_ops["matricule"]})
fin_mfa = pick("FIN")
fin_inactif = pick("FIN", exclude={fin_mfa["matricule"]})
mkt_mfa = pick("MKT")
jur_inactif = pick("JUR")
ops_mfa = pick("OPS")
com_mfa2 = pick("COM", exclude={com_ops["matricule"], com_mfa["matricule"]})

# ------------------------------------------------------------------ Annuaire Entra ID
entra = []


def compte(email, nom_aff, emp_id, service, poste, enabled=True, created="", last="", mfa=True, pne=False,
           typ="Membre", groupes=()):
    entra.append(dict(upn=email, nom_affiche=nom_aff, employee_id=emp_id, service=service, poste=poste,
                      compte_actif="Oui" if enabled else "Non", date_creation=created, derniere_connexion=last,
                      mfa_enregistre="Oui" if mfa else "Non", mdp_sans_expiration="Oui" if pne else "Non",
                      type_compte=typ, groupes=";".join(groupes)))


def recent():
    return (REF - timedelta(days=random.randint(0, 12))).isoformat()


for r in rh:
    role = r["role"]
    groupes = list(MATRICE[role][1])
    est_presta = r["matricule"].startswith("P")
    typ = "Externe" if est_presta else "Membre"
    enabled, last = True, recent()
    if r["date_sortie"]:
        enabled = False
        last = (d(r["date_sortie"]) - timedelta(days=1)).isoformat()
    if r["fin_mission"] and d(r["fin_mission"]) < REF:
        enabled = False
        last = r["fin_mission"]
    compte(r["email"], f"{r['prenom']} {r['nom']}", r["matricule"], r["service"], r["poste"], enabled,
           r["date_entree"], last, True, False, typ, groupes)

E = {c["upn"]: c for c in entra}

# A1 — départ : compte resté actif ET utilisé après le départ
E[dep_dev["email"]].update(compte_actif="Oui", derniere_connexion="2026-10-02")
# A2 — départ : compte resté actif
E[dep_com["email"]].update(compte_actif="Oui", derniere_connexion="2026-10-30")
# A5 — prestataire terminé : compte invité toujours actif
E[pr_fin3["email"]].update(compte_actif="Oui", derniere_connexion="2026-09-18")
# A9 — mobilité Support N2 -> Commercial : accès aux données patients conservé
E[mob_sup_com["email"]]["groupes"] = ";".join(MATRICE["COM"][1] + ["GRP-SUPPORT", "GRP-SUPPORT-DONNEES-PATIENTS"])
# A10 — mobilité Ops -> Dev : groupe Ops conservé
E[mob_ops_dev["email"]]["groupes"] = ";".join(MATRICE["DEV"][1] + ["GRP-OPS"])
# A12 — commercial membre du groupe Ops
E[com_ops["email"]]["groupes"] = ";".join(MATRICE["COM"][1] + ["GRP-OPS"])
# A15/A16 — MFA non enregistré
for r in (com_mfa, fin_mfa, mkt_mfa, ops_mfa, com_mfa2):
    E[r["email"]]["mfa_enregistre"] = "Non"
# A17 — inactivité > 90 jours (dont une absence longue justifiée)
E[maternite["email"]]["derniere_connexion"] = "2026-07-14"
E[fin_inactif["email"]]["derniere_connexion"] = "2026-08-01"
E[jur_inactif["email"]]["derniere_connexion"] = "2026-06-10"

# Comptes hors RH
p, n = dev_doublon["prenom"], dev_doublon["nom"]
compte(f"{ascii_(p)}.{ascii_(n)}2@{DOM}", f"{p} {n}", dev_doublon["matricule"], "R&D", "Développeur", True,
       "2025-03-10", "2026-02-01", False, False, "Membre", ["GRP-ALL", "GRP-RD"])                     # A13 doublon
compte(f"test.admin@{DOM}", "Test Admin", "", "", "", True, "2024-03-12", "2026-05-20", False, True, "Membre",
       ["GRP-ALL", "GRP-ADMIN-ENTRA"])                                                                  # A7 orphelin
compte(f"support@{DOM}", "Support MediSoft", "", "Support", "", True, "2020-06-01", "2026-12-14", False, True, "Membre",
       ["GRP-ALL", "GRP-SUPPORT", "GRP-SUPPORT-DONNEES-PATIENTS"])                                      # A8 générique
compte("auditeur1@cabinet-audit.example", "Auditeur externe 1", "", "", "", True, "2026-09-01", "2026-10-10", True,
       False, "Externe", ["GRP-EXT-AUDIT"])                                                             # A18 invité
compte("auditeur2@cabinet-audit.example", "Auditeur externe 2", "", "", "", True, "2026-09-01", "2026-10-09", True,
       False, "Externe", ["GRP-EXT-AUDIT"])                                                             # A18 invité
for upn, (lib, owner, _) in COMPTES_TECHNIQUES.items():
    is_bg = upn.startswith("breakglass")
    compte(upn, lib, "", "Technique", lib, True, "2023-01-15",
           "2026-12-03" if upn.startswith("svc-backup") else "", True if is_bg else False,
           not is_bg, "Service" if not is_bg else "Membre",
           ["GRP-BREAKGLASS"] if is_bg else ["GRP-SERVICE"])                                            # A19 svc-backup

# ------------------------------------------------------------------ AWS IAM Identity Center
aws = []
for r in rh:
    c = E[r["email"]]
    if r["date_sortie"] and r is not dep_ops:
        continue
    if r["fin_mission"] and d(r["fin_mission"]) < REF:
        continue
    for droit in MATRICE[r["role"]][2]:
        compte_aws, ps = droit.split(":")
        aws.append(dict(utilisateur=r["email"], compte_aws=compte_aws, permission_set=ps))
for upn, (_, _, droits) in COMPTES_TECHNIQUES.items():
    for droit in droits:
        a, ps = droit.split(":")
        aws.append(dict(utilisateur=upn, compte_aws=a, permission_set=ps))
# A3 — départ Ops : droits AWS non retirés (compte Entra bien désactivé)
# (déjà inclus ci-dessus : le départ Ops a été conservé volontairement)
# A10 — mobilité Ops -> Dev : accès production conservé
aws.append(dict(utilisateur=mob_ops_dev["email"], compte_aws="prod", permission_set="OpsEngineer"))
# A11 — AdministratorAccess en production hors comptes d'urgence
for r in (cto, ops_lead, dev_admin):
    aws.append(dict(utilisateur=r["email"], compte_aws="prod", permission_set="AdministratorAccess"))

# ------------------------------------------------------------------ GitHub
gh = []
ROLE_GH = {"owner": "owner", "maintainer": "maintainer", "member": "member", "outside-collaborator": "outside-collaborator"}
for r in rh:
    role_gh = MATRICE[r["role"]][3]
    if role_gh == "aucun":
        continue
    if r["date_sortie"] and r is not dep_ops:
        continue
    teams = {"DEV": "dev", "DEV-LEAD": "dev;release-approvers", "CTO": "dev;release-approvers", "OPS": "ops",
             "OPS-LEAD": "ops;release-approvers", "RSSI": "securite", "PRESTA-DEV": "mobile-app"}.get(r["role"], "")
    login = ascii_(r["prenom"])[0] + ascii_(r["nom"]) + "-ms"
    gh.append(dict(login=login, email=r["email"], role_org=ROLE_GH[role_gh],
                   deux_facteurs="Oui", equipes=teams))
G = {g["email"]: g for g in gh}
G[stagiaire["email"]]["role_org"] = "owner"            # A20 stagiaire propriétaire de l'organisation
G[dev_2fa["email"]]["deux_facteurs"] = "Non"           # A21 2FA désactivée
# A4/A5/A6 — les 3 prestataires terminés gardent leur accès GitHub (déjà inclus : fin de mission non filtrée)

# ------------------------------------------------------------------ Écriture
DATA.mkdir(exist_ok=True)


def ecrire(nom, rows):
    with open(DATA / nom, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(rows)


ecrire("export_rh.csv", rh)
ecrire("export_entra_id.csv", entra)
ecrire("export_aws_identity_center.csv", aws)
ecrire("export_github.csv", gh)

mat_rows = []
for code, (lib, grp, aws_d, gh_r, console) in MATRICE.items():
    mat_rows.append(dict(role=code, libelle=lib, groupes_entra=";".join(grp), droits_aws=";".join(aws_d),
                         role_github=gh_r, console_medisoft=console))
ecrire("matrice_roles.csv", mat_rows)
print(f"RH: {len(rh)} | Entra: {len(entra)} | AWS: {len(aws)} | GitHub: {len(gh)}")
