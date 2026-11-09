# -*- coding: utf-8 -*-
"""Tableau de bord sécurité MediSoft — fin T1 2027 (module 6)."""
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.chart import BarChart, Reference

OUT = Path(__file__).resolve().parent.parent / "output" / "Tableau_de_bord_securite_MediSoft.xlsx"
FONT, NAVY = "Arial", "1F3864"
thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="top", wrap_text=True)
F = lambda **k: Font(name=FONT, size=k.pop("size", 10), **k)
FILL_HEAD = PatternFill("solid", fgColor=NAVY)
FILL_INPUT = PatternFill("solid", fgColor="FFF2CC")
FILL_LIGHT = PatternFill("solid", fgColor="D9E2F3")
RED, ORANGE, YELLOW, GREEN, GREY = (PatternFill("solid", fgColor=c) for c in ("FFC7CE", "F8CBAD", "FFEB9C", "C6EFCE", "E7E6E6"))
wb = Workbook()


def header(ws, row, cols, widths):
    for i, (c, w) in enumerate(zip(cols, widths), start=1):
        cell = ws.cell(row, i, c)
        cell.font = F(bold=True, color="FFFFFF")
        cell.fill = FILL_HEAD
        cell.alignment = CENTER
        cell.border = BORDER
        if w:
            ws.column_dimensions[cell.column_letter].width = w
    ws.row_dimensions[row].height = 32


def body(cell, center=False, bold=False, inp=False):
    cell.font = F(bold=bold, color="0000FF") if inp else F(bold=bold)
    cell.alignment = CENTER if center else WRAP
    cell.border = BORDER
    if inp:
        cell.fill = FILL_INPUT


def title(ws, t, s):
    ws["A1"] = t
    ws["A1"].font = F(size=16, bold=True, color=NAVY)
    ws["A2"] = s
    ws["A2"].font = F(italic=True, color="595959")


def cf_values(ws, rng, mapping):
    for val, fill in mapping:
        ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=[f'"{val}"'], fill=fill))


# ------------------------------------------------------------------ 0. Lisez-moi
ws = wb.active
ws.title = "0_Lisez-moi"
title(ws, "MediSoft — Tableau de bord de la sécurité, fin du 1er trimestre 2027",
      "Module 6 du projet GRC. Sert au comité sécurité trimestriel et à la revue de direction (ISO 27001 clause 9). Données fictives.")
ws.column_dimensions["A"].width = 30
ws.column_dimensions["B"].width = 95
ws.column_dimensions["C"].width = 14
ws.cell(4, 1, "Date de référence").font = F(bold=True)
c = ws.cell(4, 3, date(2027, 3, 31))
c.number_format = "DD/MM/YYYY"
body(c, center=True, inp=True)
wb.defined_names["DATE_REF"] = DefinedName("DATE_REF", attr_text="'0_Lisez-moi'!$C$4")
r = 6
for t, d in [("1_KPI", "18 indicateurs : valeur de départ (T4 2026), valeur actuelle (T1 2027), cible, seuil d'alerte, statut et tendance calculés"),
             ("2_Maturite", "Évolution de la maturité ISO 27001 par thème depuis l'analyse d'écarts du module 1"),
             ("3_Plan_action", "Avancement des 18 chantiers du plan d'action, retards calculés"),
             ("4_Dossier_preuves", "Préparation de l'audit de certification : preuve attendue pour chaque exigence clé, document correspondant, disponibilité"),
             ("5_Non_conformites", "Registre des non-conformités issues de l'audit interne (clause 10.2)"),
             ("6_Synthese", "Une page pour la direction : chiffres clés et graphiques")]:
    ws.cell(r, 1, t).font = F(bold=True)
    ws.cell(r, 2, d).alignment = WRAP
    r += 1
r += 1
ws.cell(r, 1, "Règles de statut des KPI").font = F(size=12, bold=True, color=NAVY)
for t, d in [("Atteint", "La valeur actuelle atteint la cible"),
             ("En progrès", "La cible n'est pas atteinte, mais la valeur est meilleure que le seuil d'alerte"),
             ("En retard", "La valeur est moins bonne que le seuil d'alerte : point à remonter au comité"),
             ("Sens", "« Haut » : plus la valeur est élevée, mieux c'est. « Bas » : l'inverse (délais, taux de clic…)")]:
    r += 1
    ws.cell(r, 1, t).font = F(bold=True)
    ws.cell(r, 2, d)

# ------------------------------------------------------------------ 3. Plan d'action (créé avant les KPI qui y font référence)
wsP = wb.create_sheet("3_Plan_action")
title(wsP, "Suivi du plan d'action", "Les 18 chantiers issus de l'analyse d'écarts (module 1). Avancement saisi par les porteurs, retard calculé.")
cols = ["ID", "Chantier", "Porteur", "Priorité", "Échéance", "Module", "Avancement", "Réalisé au 31/03/2027", "Reste à faire", "Statut"]
header(wsP, 4, cols, [8, 24, 18, 9, 12, 10, 12, 50, 45, 14])
PA = [
    ("PA-01", "Gouvernance", "Direction générale", "P1", date(2027, 3, 31), "M2", 1.0, "RSSI et DPO nommés ; comité sécurité tenu en janvier et en avril ; RACI publiée", "—"),
    ("PA-02", "Certification HDS v2.0", "DG + RSSI", "P1", date(2027, 3, 31), "M6", 0.4, "Organisme certificateur choisi ; audit interne blanc réalisé", "Corriger les 2 non-conformités majeures ; audit de certification en juin 2027"),
    ("PA-03", "Corpus documentaire", "RSSI", "P1", date(2027, 3, 31), "M2", 1.0, "PSSI, 10 politiques, charte, procédures publiées", "—"),
    ("PA-04", "Identités et accès", "DSI / Ops", "P1", date(2027, 3, 31), "M3", 0.85, "MFA 100 % des comptes à privilèges ; 1re revue des accès ; GitHub sous SSO", "Synchronisation SIRH → Entra ID ; élévation à la demande AWS"),
    ("PA-05", "Chiffrement", "Ops", "P1", date(2027, 3, 31), "M2", 0.9, "92 % des ressources chiffrées ; TLS interne activé", "Migrer 2 anciennes bases non chiffrées"),
    ("PA-06", "Gestion des incidents", "RSSI", "P1", date(2027, 3, 31), "M5", 1.0, "Procédure, playbooks, registre, 2 incidents traités", "—"),
    ("PA-07", "Vulnérabilités et correctifs", "Ops / CTO", "P1", date(2027, 3, 31), "M6", 0.6, "Scan hebdomadaire en place ; SCA et SBOM dans la CI", "Respect des délais de correction (72 % au lieu de 90 %)"),
    ("PA-08", "Données de test", "CTO", "P1", date(2027, 3, 31), "M4", 1.0, "Jeux de données synthétiques ; copies de production supprimées de la préproduction", "—"),
    ("PA-09", "Sensibilisation", "RSSI + RH", "P1", date(2027, 3, 31), "M5", 0.65, "E-learning lancé (64 %) ; atelier direction ; 2 campagnes simulées", "Atteindre 95 % de collaborateurs formés"),
    ("PA-10", "Cloisonnement", "Ops", "P1", date(2027, 6, 30), "M3", 0.5, "AWS Organizations ; comptes dev et préprod séparés ; SSH fermé", "Migration de la production dans son compte dédié"),
    ("PA-11", "Journalisation et supervision", "Ops + RSSI", "P1", date(2027, 6, 30), "M5", 0.45, "CloudTrail centralisé ; GuardDuty activé ; Wazuh en test", "Journal applicatif des accès aux dossiers patients sur l'API mobile (NC majeure)"),
    ("PA-12", "Continuité", "Ops", "P1", date(2027, 6, 30), "M6", 0.3, "Sauvegardes immuables ; 1 test de restauration réussi", "BIA, PCA, test du PRA (NC majeure)"),
    ("PA-13", "Fournisseurs et contrats", "Juridique + RSSI", "P1", date(2027, 6, 30), "M4", 0.55, "Politique, registre, 5 fournisseurs Tier 1 évalués", "Plans de sortie ; avenants DORA ; contrat du freelance"),
    ("PA-14", "Développement sécurisé", "CTO", "P1", date(2027, 6, 30), "M4", 0.6, "Revue de code obligatoire ; SAST et détection de secrets en CI", "DAST ; pentest PASSI prévu en mai"),
    ("PA-15", "Postes de travail", "DSI", "P2", date(2027, 6, 30), "M3", 0.5, "MDM déployé sur 70 % des postes ; EDR déployé", "Macs ; blocage USB"),
    ("PA-16", "Inventaire et classification", "RSSI", "P2", date(2027, 6, 30), "M6", 0.4, "Inventaire AWS et postes ; schéma de classification", "Outils SaaS ; cartographie des flux de données de santé"),
    ("PA-17", "Pilotage du SMSI", "RSSI", "P2", date(2027, 9, 30), "M6", 0.6, "Tableau de bord ; audit interne blanc ; 1re revue de direction", "Automatiser les KPI ; programme d'audit complet"),
    ("PA-18", "Veille et conformité", "RSSI + DPO", "P2", date(2027, 12, 31), "M1 / M5", 0.5, "Bulletin de veille mensuel ; registre des obligations revu", "Suivi de la loi Résilience (NIS2) et des décrets"),
]
ps = 5
for i, (pid, ch, por, pr, ech, mod, av, fait, reste) in enumerate(PA, start=ps):
    for j, v in enumerate([pid, ch, por, pr, ech, mod, av, fait, reste, None], start=1):
        body(wsP.cell(i, j, v), center=j in (1, 4, 5, 6, 7, 10), bold=j == 2, inp=j == 7)
    wsP.cell(i, 5).number_format = "DD/MM/YYYY"
    wsP.cell(i, 7).number_format = "0%"
    wsP.cell(i, 10, f'=IF(G{i}>=1,"Terminé",IF(E{i}<=DATE_REF,"En retard",IF(G{i}>0,"En cours","À lancer")))')
pe = ps + len(PA) - 1
cf_values(wsP, f"J{ps}:J{pe}", [("Terminé", GREEN), ("En cours", YELLOW), ("En retard", RED), ("À lancer", GREY)])
wsP.conditional_formatting.add(f"D{ps}:D{pe}", CellIsRule(operator="equal", formula=['"P1"'], fill=RED))
dv = DataValidation(type="decimal", operator="between", formula1="0", formula2="1")
wsP.add_data_validation(dv)
dv.add(f"G{ps}:G{pe}")
t = pe + 2
wsP.cell(t, 2, "Avancement global").font = F(bold=True)
c = wsP.cell(t, 7, f"=AVERAGE(G{ps}:G{pe})")
c.number_format = "0%"
c.font = F(bold=True, size=11, color=NAVY)
wsP.cell(t + 1, 2, "Chantiers en retard").font = F(bold=True)
wsP.cell(t + 1, 7, f'=COUNTIF(J{ps}:J{pe},"En retard")').font = F(bold=True, size=11, color=NAVY)
wsP.freeze_panes = "C5"
PLAN_AVG = f"'3_Plan_action'!$G${t}"
PLAN_LATE = f"'3_Plan_action'!$G${t+1}"

# ------------------------------------------------------------------ 1. KPI
ws = wb.create_sheet("1_KPI", 1)
title(ws, "Indicateurs de sécurité (KPI)", "Valeurs fictives. Statut et tendance calculés à partir de la cible, du seuil d'alerte et du sens de l'indicateur.")
cols = ["N°", "Domaine", "Indicateur", "Source", "Unité", "Sens", "T4 2026", "T1 2027", "Cible", "Seuil d'alerte",
        "Statut", "Tendance", "Lien PSSI / plan"]
header(ws, 4, cols, [5, 16, 44, 26, 8, 7, 10, 10, 9, 10, 13, 15, 16])
P, N = "%", "nb"
KPI = [
    ("Accès", "Comptes à privilèges protégés par MFA", "Entra ID (accès conditionnel)", P, "Haut", 0.40, 1.00, 1.00, 0.90, "O1 / PA-04"),
    ("Accès", "Anomalies de la revue des accès corrigées", "Revue des accès (module 3)", P, "Haut", None, 0.94, 1.00, 0.80, "PA-04"),
    ("Accès", "Délai moyen de désactivation après un départ", "Script access_review.py", "jours", "Bas", 34, 0.5, 0, 2, "PA-04"),
    ("Protection", "Ressources de stockage chiffrées", "AWS Config", P, "Haut", 0.55, 0.92, 1.00, 0.85, "O2 / PA-05"),
    ("Protection", "Score de conformité AWS Security Hub (CIS)", "AWS Security Hub", P, "Haut", 0.48, 0.81, 0.90, 0.70, "PA-10"),
    ("Protection", "Postes gérés par le MDM", "Intune", P, "Haut", 0.0, 0.70, 1.00, 0.80, "PA-15"),
    ("Vulnérabilités", "Vulnérabilités critiques corrigées en moins de 7 jours", "Scanner de vulnérabilités", P, "Haut", None, 0.72, 0.90, 0.80, "O4 / PA-07"),
    ("Vulnérabilités", "Secrets détectés dans le code (nouveaux)", "Détection de secrets en CI", N, "Bas", 3, 0, 0, 1, "PA-14"),
    ("Continuité", "Tests de restauration réussis (cumul annuel)", "PV de test (MS-POL-04)", N, "Haut", 0, 1, 1, 1, "O5 / PA-12"),
    ("Incidents", "Notifications réalisées dans les délais", "Registre des incidents", P, "Haut", None, 1.00, 1.00, 1.00, "PA-06"),
    ("Incidents", "Incidents G3 et G4 sur le trimestre", "Registre des incidents", N, "Bas", 2, 1, 0, 2, "PA-06"),
    ("Humain", "Collaborateurs formés (e-learning)", "CyberQuiz", P, "Haut", 0.0, 0.64, 0.95, 0.50, "O3 / PA-09"),
    ("Humain", "Taux de clic aux campagnes de phishing simulé", "CyberQuiz", P, "Bas", 0.24, 0.15, 0.10, 0.20, "PA-09"),
    ("Humain", "Taux de signalement des campagnes simulées", "CyberQuiz", P, "Haut", 0.18, 0.37, 0.50, 0.30, "PA-09"),
    ("Fournisseurs", "Fournisseurs Tier 1 évalués et à jour", "Registre des fournisseurs", P, "Haut", 0.0, 1.00, 1.00, 0.80, "PA-13"),
    ("Fournisseurs", "Fournisseurs Tier 1 sans plan de sortie", "Registre des fournisseurs", N, "Bas", 5, 3, 0, 4, "PA-13"),
    ("Conformité", "Dérogations échues non clôturées", "Registre des dérogations", N, "Bas", 0, 0, 0, 1, "MS-PRO-01"),
    ("Pilotage", "Avancement global du plan d'action", "Onglet 3_Plan_action", P, "Haut", 0.0, "PLAN", 0.60, 0.50, "PA-17"),
]
ks = 5
for i, (dom, ind, src, unit, sens, base, cur, cib, seuil, lien) in enumerate(KPI, start=ks):
    vals = [i - ks + 1, dom, ind, src, unit, sens, base, None if cur == "PLAN" else cur, cib, seuil, None, None, lien]
    for j, v in enumerate(vals, start=1):
        body(ws.cell(i, j, v), center=j in (1, 5, 6, 7, 8, 9, 10, 11, 12), inp=j in (7, 8, 9, 10))
    if cur == "PLAN":
        ws.cell(i, 8, f"={PLAN_AVG}")
        ws.cell(i, 8).font = F(color="008000")
        ws.cell(i, 8).fill = PatternFill(fill_type=None)
    fmt = "0%" if unit == P else "0.0" if unit == "jours" else "0"
    for j in (7, 8, 9, 10):
        ws.cell(i, j).number_format = fmt
    if base is None:
        ws.cell(i, 7, "n.d.")
    ws.cell(i, 11, f'=IF(F{i}="Haut",IF(H{i}>=I{i},"Atteint",IF(H{i}>=J{i},"En progrès","En retard")),'
                   f'IF(H{i}<=I{i},"Atteint",IF(H{i}<=J{i},"En progrès","En retard")))')
    ws.cell(i, 12, f'=IF(NOT(ISNUMBER(G{i})),"Nouvel indicateur",IF(H{i}=G{i},"→ stable",'
                   f'IF((H{i}>G{i})=(F{i}="Haut"),"↗ amélioration","↘ dégradation")))')
ke = ks + len(KPI) - 1
cf_values(ws, f"K{ks}:K{ke}", [("Atteint", GREEN), ("En progrès", YELLOW), ("En retard", RED)])
ws.conditional_formatting.add(f"L{ks}:L{ke}", FormulaRule(formula=[f'LEFT(L{ks},1)="↗"'], font=F(bold=True, color="008000")))
ws.conditional_formatting.add(f"L{ks}:L{ke}", FormulaRule(formula=[f'LEFT(L{ks},1)="↘"'], font=F(bold=True, color="C00000")))
ws.freeze_panes = "D5"
ws.auto_filter.ref = f"A4:M{ke}"
KPI_RNG = f"'1_KPI'!$K${ks}:$K${ke}"

# ------------------------------------------------------------------ 2. Maturité
ws = wb.create_sheet("2_Maturite", 2)
title(ws, "Évolution de la maturité ISO 27001", "T4 2026 : analyse d'écarts du module 1. T1 2027 : réévaluation par l'audit interne blanc de mars 2027.")
header(ws, 4, ["Périmètre", "T4 2026", "T1 2027", "Cible", "Progression", "Commentaire"], [32, 11, 11, 9, 12, 70])
MAT = [
    ("Clauses 4 à 10 (SMSI)", 0.72, 1.8, "Périmètre, politique, rôles, appréciation des risques et revue de direction en place ; audit interne encore partiel"),
    ("A.5 Organisationnelles", 0.73, 1.9, "Documentation complète ; preuves d'application encore incomplètes (fournisseurs, continuité)"),
    ("A.6 Personnes", 1.00, 1.9, "Charte signée, sensibilisation lancée, processus de départ corrigé"),
    ("A.7 Physiques", 1.85, 2.1, "Peu de changements : périmètre physique limité (bureaux)"),
    ("A.8 Technologiques", 1.03, 1.8, "MFA, chiffrement, CI sécurisée ; journalisation applicative et PRA encore insuffisants"),
]
ms = 5
for i, (p, a, b, cm) in enumerate(MAT, start=ms):
    for j, v in enumerate([p, a, b, 3, None, cm], start=1):
        body(ws.cell(i, j, v), center=j in (2, 3, 4, 5), bold=j == 1, inp=j in (2, 3, 4))
    ws.cell(i, 5, f"=C{i}-B{i}")
    for j in (2, 3, 4, 5):
        ws.cell(i, j).number_format = "0.0"
    ws.cell(i, 5).number_format = "+0.0;-0.0"
me = ms + len(MAT) - 1
ws.cell(me + 2, 1, "Lecture : la maturité a plus que doublé en un trimestre, surtout grâce à la documentation (niveau 2). Le niveau 3 exige la preuve que les règles sont appliquées dans la durée : c'est l'enjeu des trimestres suivants.").font = F(italic=True, size=9, color="595959")
ws.merge_cells(start_row=me + 2, start_column=1, end_row=me + 2, end_column=6)
ws.row_dimensions[me + 2].height = 30
ws.cell(me + 2, 1).alignment = WRAP
ch = BarChart()
ch.type = "col"
ch.title = "Maturité moyenne (0-5) : T4 2026 → T1 2027"
ch.y_axis.scaling.min = 0
ch.y_axis.scaling.max = 3.5
ch.add_data(Reference(ws, min_col=2, max_col=4, min_row=4, max_row=me), titles_from_data=True)
ch.set_categories(Reference(ws, min_col=1, min_row=ms, max_row=me))
ch.height, ch.width = 8, 18
ws.add_chart(ch, "A13")
MAT_RNG = (ms, me)

# ------------------------------------------------------------------ 4. Dossier de preuves
ws = wb.create_sheet("4_Dossier_preuves")
title(ws, "Dossier de preuves — préparation de l'audit de certification",
      "Pour chaque exigence clé : ce que l'auditeur demandera, où se trouve la preuve dans le projet, et si elle est disponible.")
header(ws, 4, ["Exigence", "Intitulé", "Preuve attendue par l'auditeur", "Document ou enregistrement", "Disponibilité", "Commentaire"],
       [11, 30, 45, 40, 13, 40])
PR = [
    ("Cl. 4.3", "Périmètre du SMSI", "Périmètre documenté et validé", "MS-POL-00 §3", "Disponible", ""),
    ("Cl. 5.1", "Leadership", "Preuves de l'implication de la direction", "PSSI signée ; CR des comités ; CR de revue de direction (MS-ENR-07)", "Disponible", ""),
    ("Cl. 5.2", "Politique", "Politique approuvée et communiquée", "MS-POL-00 ; preuve de diffusion", "Disponible", ""),
    ("Cl. 5.3", "Rôles", "Rôles et responsabilités attribués", "MS-POL-01 (RACI) ; lettres de nomination RSSI et DPO", "Disponible", ""),
    ("Cl. 6.1.2", "Appréciation des risques", "Méthode et résultats de l'appréciation des risques", "Rapport EBIOS RM", "Disponible", "Revue annuelle à planifier"),
    ("Cl. 6.1.3", "Traitement des risques", "Déclaration d'applicabilité et plan de traitement validés ; acceptation des risques résiduels", "SoA (module 1) ; plan d'action", "Partielle", "Acceptation formelle des risques résiduels à signer par les propriétaires"),
    ("Cl. 6.2", "Objectifs", "Objectifs mesurables et leur suivi", "PSSI §5 ; onglet 1_KPI", "Disponible", ""),
    ("Cl. 7.2", "Compétences", "Compétences requises et preuves de formation", "Matrice de compétences", "Partielle", "Matrice incomplète pour l'équipe Ops (NC-2027-05)"),
    ("Cl. 7.3", "Sensibilisation", "Programme et preuves de participation", "MS-PRO-05 ; exports CyberQuiz", "Disponible", "64 % formés, objectif 95 % en juin"),
    ("Cl. 7.5", "Informations documentées", "Maîtrise des documents (versions, approbation)", "MS-PRO-02 ; liste des documents", "Partielle", "2 documents sans date d'approbation (NC-2027-06)"),
    ("Cl. 9.1", "Surveillance et mesure", "Indicateurs suivis et analysés", "Ce tableau de bord", "Disponible", ""),
    ("Cl. 9.2", "Audit interne", "Programme et rapports d'audit", "MS-ENR-06", "Disponible", "Programme 2027 à compléter (2 audits restants)"),
    ("Cl. 9.3", "Revue de direction", "Compte rendu avec les éléments d'entrée et de sortie requis", "MS-ENR-07", "Disponible", ""),
    ("Cl. 10.2", "Non-conformités", "Registre des non-conformités et actions correctives", "Onglet 5_Non_conformites", "Disponible", ""),
    ("A.5.15-18", "Contrôle d'accès", "Politique ; preuves de revue des accès ; traitement des départs", "MS-POL-02 ; revue T4 2026 (module 3) ; MS-PRO-03", "Disponible", ""),
    ("A.5.19-22", "Fournisseurs", "Politique ; évaluations ; clauses", "MS-POL-10 ; registre des fournisseurs", "Partielle", "Plans de sortie manquants pour 3 fournisseurs Tier 1"),
    ("A.5.24-28", "Incidents", "Procédure ; registre ; rapports ; RETEX", "MS-PRO-04 ; MS-ENR-05", "Disponible", ""),
    ("A.5.29-30", "Continuité", "PCA, PRA et preuves de test", "MS-POL-04 ; PV de restauration", "Manquante", "PRA jamais testé (NC-2027-01, majeure)"),
    ("A.5.31", "Exigences légales", "Registre des obligations à jour", "Registre (module 1) ; bulletin de veille", "Disponible", ""),
    ("A.5.34", "Données personnelles", "Registre des traitements ; DPA ; désignation du DPO", "Registre RGPD ; contrats", "Partielle", "Registre du sous-traitant en cours de finalisation"),
    ("A.6.3", "Sensibilisation", "Supports et taux de participation", "Module 5", "Disponible", ""),
    ("A.8.5", "Authentification", "Configuration de la MFA ; taux de couverture", "Export de l'accès conditionnel ; KPI n° 1", "Disponible", ""),
    ("A.8.8", "Vulnérabilités", "Rapports de scan ; délais de correction", "Rapports hebdomadaires ; KPI n° 7", "Partielle", "Délais non respectés (NC-2027-03)"),
    ("A.8.13", "Sauvegarde", "Configuration ; PV de tests de restauration", "MS-POL-04 ; PV du 14/02/2027", "Disponible", ""),
    ("A.8.15", "Journalisation", "Journaux centralisés ; traçabilité des accès aux données de santé", "CloudTrail ; journal applicatif", "Manquante", "Journal des accès incomplet sur l'API mobile (NC-2027-02, majeure)"),
    ("A.8.24", "Cryptographie", "Politique ; preuve du chiffrement des ressources", "MS-POL-03 ; rapport AWS Config", "Partielle", "2 bases encore non chiffrées"),
    ("A.8.25-29", "Développement sécurisé", "Politique ; preuves de revue de code et de tests", "MS-POL-06 ; historique des pull requests ; rapports CI", "Disponible", "Pentest PASSI prévu en mai 2027"),
    ("HDS", "Localisation EEE", "Preuve de la localisation des données et des sauvegardes", "MS-POL-05 ; configuration AWS (régions, SCP)", "Disponible", ""),
]
qs_ = 5
for i, row in enumerate(PR, start=qs_):
    for j, v in enumerate(row, start=1):
        body(ws.cell(i, j, v), center=j in (1, 5), bold=j == 1, inp=j == 5)
qe_ = qs_ + len(PR) - 1
cf_values(ws, f"E{qs_}:E{qe_}", [("Disponible", GREEN), ("Partielle", YELLOW), ("Manquante", RED)])
dv = DataValidation(type="list", formula1='"Disponible,Partielle,Manquante"')
ws.add_data_validation(dv)
dv.add(f"E{qs_}:E{qe_}")
t = qe_ + 2
ws.cell(t, 2, "Taux de préparation").font = F(bold=True)
c = ws.cell(t, 3, f'=(COUNTIF(E{qs_}:E{qe_},"Disponible")+0.5*COUNTIF(E{qs_}:E{qe_},"Partielle"))/COUNTA(E{qs_}:E{qe_})')
c.number_format = "0%"
c.font = F(bold=True, size=11, color=NAVY)
ws.cell(t + 1, 2, "Preuves manquantes").font = F(bold=True)
ws.cell(t + 1, 3, f'=COUNTIF(E{qs_}:E{qe_},"Manquante")').font = F(bold=True, size=11, color=NAVY)
ws.cell(t + 2, 2, "Calcul : preuve disponible = 1 ; partielle = 0,5 ; manquante = 0.").font = F(italic=True, size=9, color="595959")
ws.freeze_panes = "C5"
PREP = (f"'4_Dossier_preuves'!$C${t}", f"'4_Dossier_preuves'!$C${t+1}")

# ------------------------------------------------------------------ 5. Non-conformités
ws = wb.create_sheet("5_Non_conformites")
title(ws, "Registre des non-conformités et actions correctives (clause 10.2)", "Issues de l'audit interne blanc du 15 au 19/03/2027 (MS-ENR-06).")
header(ws, 4, ["N°", "Type", "Exigence", "Constat", "Cause racine", "Action corrective", "Responsable", "Échéance", "Statut", "Retard"],
       [11, 12, 11, 45, 35, 45, 14, 12, 12, 10])
NC = [
    ("NC-2027-01", "Majeure", "A.5.30 / HDS", "Le plan de reprise d'activité n'a jamais été testé ; le RTO de 4 h promis aux clients n'est pas démontré", "Priorité donnée aux sauvegardes ; pas de responsable désigné pour le PRA", "Test complet du PRA dans une autre zone de disponibilité, en présence d'un client assureur", "Resp. Ops", date(2027, 5, 31), "En cours"),
    ("NC-2027-02", "Majeure", "A.8.15 / HDS", "Les consultations de dossiers patients via l'API mobile ne sont pas journalisées : traçabilité incomplète", "Journalisation ajoutée à l'application web uniquement ; l'API mobile, plus récente, a été oubliée", "Journal des accès sur toutes les API ; test de complétude des journaux dans la CI", "CTO", date(2027, 4, 30), "En cours"),
    ("NC-2027-03", "Mineure", "A.8.8", "28 % des vulnérabilités critiques corrigées au-delà de 7 jours", "Pas de créneau de maintenance réservé ; correctifs en concurrence avec les fonctionnalités", "Créneau de correction hebdomadaire réservé ; escalade automatique au CTO à J+5", "CTO", date(2027, 5, 31), "En cours"),
    ("NC-2027-04", "Mineure", "A.5.9", "L'inventaire des actifs n'inclut pas les outils SaaS", "Inventaire limité à AWS et aux postes", "Ajout des SaaS à partir du registre des fournisseurs et des journaux du SSO", "RSSI", date(2027, 4, 30), "Clos"),
    ("NC-2027-05", "Mineure", "Cl. 7.2", "Matrice de compétences incomplète pour l'équipe Ops", "Prestataire Ops arrivé en cours de projet", "Compléter la matrice et le plan de formation Ops", "Resp. Ops", date(2027, 4, 30), "En cours"),
    ("NC-2027-06", "Mineure", "Cl. 7.5", "2 documents publiés sans date d'approbation", "Publication avant la réunion du comité", "Correction ; contrôle de la date d'approbation avant publication", "RSSI", date(2027, 3, 31), "Clos"),
    ("NC-2027-07", "Mineure", "A.8.32", "2 changements en production sur 20 échantillonnés sans ticket d'approbation", "Correctifs urgents réalisés de nuit", "Procédure de changement d'urgence avec validation a posteriori sous 24 h", "Resp. Ops", date(2027, 4, 30), "En cours"),
    ("OBS-2027-01", "Observation", "MS-PRO-01", "Instruction de la dérogation DER-2026-004 supérieure à 2 mois", "—", "Respecter les délais de la procédure", "RSSI", date(2027, 4, 15), "En cours"),
    ("OBS-2027-02", "Observation", "Cl. 9.1", "Indicateurs collectés manuellement, risque d'erreur", "—", "Automatiser la collecte des KPI techniques", "RSSI", date(2027, 9, 30), "En cours"),
]
ns = 5
for i, row in enumerate(NC, start=ns):
    for j, v in enumerate(list(row) + [None], start=1):
        body(ws.cell(i, j, v), center=j in (1, 2, 3, 8, 9, 10), bold=j == 1, inp=j == 9)
    ws.cell(i, 8).number_format = "DD/MM/YYYY"
    ws.cell(i, 10, f'=IF(AND(I{i}<>"Clos",H{i}<DATE_REF),"Oui","Non")')
ne = ns + len(NC) - 1
cf_values(ws, f"B{ns}:B{ne}", [("Majeure", RED), ("Mineure", YELLOW), ("Observation", GREY)])
cf_values(ws, f"I{ns}:I{ne}", [("Clos", GREEN), ("En cours", YELLOW)])
cf_values(ws, f"J{ns}:J{ne}", [("Oui", RED)])
dv = DataValidation(type="list", formula1='"Ouvert,En cours,Clos"')
ws.add_data_validation(dv)
dv.add(f"I{ns}:I{ne}")
ws.freeze_panes = "B5"
NCR = lambda col: f"'5_Non_conformites'!${col}${ns}:${col}${ne}"

# ------------------------------------------------------------------ 6. Synthèse direction
ws = wb.create_sheet("6_Synthese")
title(ws, "Synthèse pour la direction — fin du T1 2027", "Une page pour le comité sécurité et la revue de direction. Tous les chiffres sont calculés.")
ws.column_dimensions["A"].width = 52
ws.column_dimensions["B"].width = 16
rows = [
    ("Indicateurs", None, None),
    ("KPI atteints", f'=COUNTIF({KPI_RNG},"Atteint")', "0"),
    ("KPI en progrès", f'=COUNTIF({KPI_RNG},"En progrès")', "0"),
    ("KPI en retard", f'=COUNTIF({KPI_RNG},"En retard")', "0"),
    ("Maturité", None, None),
    ("Maturité annexe A, moyenne des 4 thèmes — T4 2026", f"=AVERAGE('2_Maturite'!B{MAT_RNG[0]+1}:B{MAT_RNG[1]})", "0.0"),
    ("Maturité annexe A, moyenne des 4 thèmes — T1 2027", f"=AVERAGE('2_Maturite'!C{MAT_RNG[0]+1}:C{MAT_RNG[1]})", "0.0"),
    ("Maturité clauses 4 à 10 — T1 2027", f"='2_Maturite'!C{MAT_RNG[0]}", "0.0"),
    ("Plan d'action", None, None),
    ("Avancement global", f"={PLAN_AVG}", "0%"),
    ("Chantiers en retard", f"={PLAN_LATE}", "0"),
    ("Préparation de l'audit", None, None),
    ("Taux de préparation du dossier de preuves", f"={PREP[0]}", "0%"),
    ("Preuves manquantes", f"={PREP[1]}", "0"),
    ("Non-conformités majeures ouvertes", f'=COUNTIFS({NCR("B")},"Majeure",{NCR("I")},"<>Clos")', "0"),
    ("Non-conformités mineures ouvertes", f'=COUNTIFS({NCR("B")},"Mineure",{NCR("I")},"<>Clos")', "0"),
]
for k, (lab, f, fmt) in enumerate(rows, start=4):
    if f is None:
        ws.cell(k, 1, lab).font = F(size=12, bold=True, color=NAVY)
        continue
    body(ws.cell(k, 1, lab), bold=True)
    c = ws.cell(k, 2, f)
    body(c, center=True, bold=True)
    c.number_format = fmt
    c.font = F(bold=True, size=11, color=NAVY)
last = 4 + len(rows) - 1
ws.cell(last + 2, 1, "Message clé : MediSoft a posé en un trimestre les bases de son SMSI. Deux non-conformités majeures (PRA non testé, journalisation de l'API mobile) doivent être levées avant l'audit de certification HDS v2.0.").font = F(bold=True, color="C00000")
ws.merge_cells(start_row=last + 2, start_column=1, end_row=last + 2, end_column=6)
ws.row_dimensions[last + 2].height = 32
ws.cell(last + 2, 1).alignment = WRAP
ch = BarChart()
ch.type = "col"
ch.title = "Maturité ISO 27001 : T4 2026 → T1 2027"
ch.y_axis.scaling.min = 0
ch.y_axis.scaling.max = 3.5
w2 = wb["2_Maturite"]
ch.add_data(Reference(w2, min_col=2, max_col=4, min_row=4, max_row=MAT_RNG[1]), titles_from_data=True)
ch.set_categories(Reference(w2, min_col=1, min_row=MAT_RNG[0], max_row=MAT_RNG[1]))
ch.height, ch.width = 8, 16
ws.add_chart(ch, "D4")

for w in wb.worksheets:
    w.sheet_view.showGridLines = False
    w.page_setup.orientation = "landscape"
    w.sheet_properties.pageSetUpPr.fitToPage = True
    w.page_setup.fitToWidth = 1
    w.page_setup.fitToHeight = 0
wb.move_sheet("6_Synthese", offset=-(len(wb.sheetnames) - 2))
wb.save(OUT)
print("saved", OUT, wb.sheetnames)
