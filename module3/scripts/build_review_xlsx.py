# -*- coding: utf-8 -*-
"""Construit le classeur de la revue des accès T4 2026 à partir de output/anomalies.csv."""
import csv
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.chart import BarChart, Reference

from matrice import MATRICE, COMPTES_TECHNIQUES

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "output" / "Revue_acces_T4-2026_MediSoft.xlsx"
FONT = "Arial"
NAVY = "1F3864"
thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="top", wrap_text=True)
F = lambda **k: Font(name=FONT, size=k.pop("size", 10), **k)
FILL_HEAD = PatternFill("solid", fgColor=NAVY)
FILL_INPUT = PatternFill("solid", fgColor="FFF2CC")
FILL_LIGHT = PatternFill("solid", fgColor="D9E2F3")
RED, ORANGE, YELLOW, GREEN, GREY = (PatternFill("solid", fgColor=c) for c in ("FFC7CE", "F8CBAD", "FFEB9C", "C6EFCE", "E7E6E6"))

# Décisions issues de la réunion de revue du 15/12/2026 (managers + RSSI)
# id: (décision, justification / commentaire, responsable de la correction, date de correction ou None)
DECISIONS = {
    "F-001": ("Désactiver + incident", "Connexion le 02/10 après la sortie du 30/09. Incident INC-2026-014 ouvert : analyse des journaux d'accès et des actions réalisées", "RSSI", date(2026, 12, 15)),
    "F-002": ("Retirer les accès", "Affectations AWS supprimées ; aucune clé d'accès IAM trouvée ; pas d'activité CloudTrail après le 14/08", "Resp. Ops", date(2026, 12, 15)),
    "F-003": ("Désactiver + incident", "Connexion le 18/09 après la fin de mission du 30/06. Incident INC-2026-015 ouvert ; société prestataire contactée", "RSSI", date(2026, 12, 15)),
    "F-004": ("Supprimer", "Comptes nominatifs créés pour les 6 agents N2 ; boîte support@ convertie en boîte partagée sans connexion", "Resp. Support", date(2026, 12, 16)),
    "F-005": ("Désactiver puis supprimer", "Aucun propriétaire identifié (compte de test créé en 2024 par un ancien Ops). Désactivé, suppression prévue au 15/01/2027", "RSSI", date(2026, 12, 15)),
    "F-006": ("Retirer le droit", "Accès aux dossiers patients sans lien avec le poste commercial depuis le 01/09 : journaux vérifiés, aucun accès constaté", "Manager Commercial", date(2026, 12, 15)),
    "F-007": ("Retirer le droit", "Attribué en 2025 pour un dépannage, jamais retiré", "Resp. Ops", date(2026, 12, 16)),
    "F-008": ("Désactiver", "Oubli lors du départ du 31/10 : la DRH n'a pas transmis l'information", "Resp. Ops", date(2026, 12, 16)),
    "F-009": ("Retirer les accès", "Fin de mission du 19/12/2025", "CTO", date(2026, 12, 17)),
    "F-010": ("Retirer les accès", "Lié à l'incident INC-2026-015", "CTO", date(2026, 12, 15)),
    "F-011": ("Retirer les accès", "Départ du 14/08/2026", "CTO", date(2026, 12, 17)),
    "F-012": ("Retirer les accès", "Fin de mission du 30/04/2026", "CTO", date(2026, 12, 17)),
    "F-013": ("Supprimer", "Ancien compte de test de la collaboratrice", "Resp. Ops", date(2026, 12, 18)),
    "F-014": ("Retirer le droit", "Ajout par erreur lors d'une démonstration client", "Manager Commercial", date(2026, 12, 18)),
    "F-015": ("Retirer le droit", "Mobilité Ops → Dev du 01/07 non répercutée", "Manager R&D", date(2026, 12, 18)),
    "F-016": ("Retirer — élévation à la demande", "Le Resp. Ops conserve OpsEngineer ; AdministratorAccess remplacé par l'élévation à la demande. Migration planifiée le 10/01/2027", "Resp. Ops", None),
    "F-017": ("Retirer — élévation à la demande", "Le CTO demande à conserver l'accès jusqu'à la mise en place de l'élévation à la demande (10/01/2027) : dérogation DER-2026-004 en cours d'instruction", "RSSI", None),
    "F-018": ("Retirer le droit", "Mobilité Ops → Dev du 01/07 non répercutée", "Resp. Ops", date(2026, 12, 18)),
    "F-019": ("Rétrograder", "Droit owner donné pour configurer GitHub Actions lors d'un projet de stage", "CTO", date(2026, 12, 16)),
    "F-020": ("Corriger", "MFA enregistré le 16/12 (clé FIDO2)", "Resp. Ops", date(2026, 12, 16)),
    "F-021": ("Corriger", "Secret changé et déplacé dans Secrets Manager ; connexion interactive bloquée ; l'Ops qui l'utilisait a reçu un rappel", "Resp. Ops", date(2026, 12, 19)),
    "F-022": ("Corriger", "2FA imposée au niveau de l'organisation GitHub", "CTO", date(2026, 12, 16)),
    "F-023": ("Conserver avec expiration", "Mission d'audit interne prolongée jusqu'au 31/01/2027 ; sponsor : RSSI ; expiration du compte fixée au 31/01/2027", "RSSI", date(2026, 12, 16)),
    "F-024": ("Désactiver", "Mission terminée pour cet auditeur", "RSSI", date(2026, 12, 16)),
    "F-025": ("Retirer le droit", "Groupe Support hérité de l'ancien poste", "Manager Commercial", date(2026, 12, 15)),
    "F-026": ("Corriger", "Relance envoyée ; MFA imposé par accès conditionnel au 05/01/2027", "Resp. Ops", None),
    "F-027": ("Corriger", "Relance envoyée ; MFA imposé par accès conditionnel au 05/01/2027", "Resp. Ops", None),
    "F-028": ("Corriger", "Relance envoyée ; MFA imposé par accès conditionnel au 05/01/2027", "Resp. Ops", None),
    "F-029": ("Corriger", "MFA enregistré le 17/12", "Resp. Ops", date(2026, 12, 17)),
    "F-030": ("Désactiver", "Juriste qui utilise désormais uniquement l'outil de gestion des contrats", "Manager Juridique", None),
    "F-031": ("Désactiver", "Compte inutilisé depuis le passage au nouvel outil financier", "Manager Finance", None),
    "F-032": ("Désactiver temporairement", "Congé maternité jusqu'au 15/01/2027 ; réactivation prévue au retour (exception documentée)", "Manager Support", date(2026, 12, 16)),
}

rows = list(csv.DictReader(open(BASE / "output" / "anomalies.csv", encoding="utf-8"), delimiter=";"))
assert set(r["id"] for r in rows) == set(DECISIONS), "décisions manquantes"
NB = {n: sum(1 for _ in open(BASE / "data" / n, encoding="utf-8")) - 1
      for n in ("export_entra_id.csv", "export_aws_identity_center.csv", "export_github.csv")}

wb = Workbook()


def header(ws, row, cols, widths):
    for i, (c, w) in enumerate(zip(cols, widths), start=1):
        cell = ws.cell(row, i, c)
        cell.font = F(bold=True, color="FFFFFF")
        cell.fill = FILL_HEAD
        cell.alignment = CENTER
        cell.border = BORDER
        ws.column_dimensions[cell.column_letter].width = w
    ws.row_dimensions[row].height = 32


def body(cell, center=False, bold=False):
    cell.font = F(bold=bold)
    cell.alignment = CENTER if center else WRAP
    cell.border = BORDER


def title(ws, t, s):
    ws["A1"] = t
    ws["A1"].font = F(size=16, bold=True, color=NAVY)
    ws["A2"] = s
    ws["A2"].font = F(italic=True, color="595959")


def grav_cf(ws, rng):
    for val, fill in (("Critique", RED), ("Élevée", ORANGE), ("Moyenne", YELLOW), ("Faible", GREEN)):
        ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=[f'"{val}"'], fill=fill))


# ------------------------------------------------------------ 0. Lisez-moi
ws = wb.active
ws.title = "0_Lisez-moi"
title(ws, "MediSoft — Revue des accès du 4e trimestre 2026",
      "Module 3 du projet GRC. Revue réalisée le 15/12/2026 selon MS-POL-02 §7. Données fictives.")
ws.column_dimensions["A"].width = 30
ws.column_dimensions["B"].width = 90
ws.column_dimensions["C"].width = 14
r = 4
for lab, val in [("Périmètre", "Annuaire Microsoft Entra ID, AWS IAM Identity Center (5 comptes AWS), organisation GitHub"),
                 ("Source de vérité", "Export RH du 15/12/2026 (salariés actifs, départs, mobilités, prestataires, absences longues)"),
                 ("Référentiel", "Matrice des rôles (onglet 1) et registre des comptes techniques"),
                 ("Méthode", "Rapprochement automatique par le script access_review.py (13 règles), puis validation des anomalies par les managers et le RSSI en réunion de revue"),
                 ("Participants", "RSSI (animation), Resp. Ops, CTO, DRH, managers Support, Commercial, R&D, Finance, Juridique")]:
    ws.cell(r, 1, lab).font = F(bold=True)
    ws.cell(r, 2, val).alignment = WRAP
    r += 1
r += 1
ws.cell(r, 1, "Paramètres").font = F(size=12, bold=True, color=NAVY)
r += 1
params = {}
for lab, val, name in [("Date de la revue", date(2026, 12, 15), "DATE_REVUE"),
                       ("Date du point de suivi", date(2026, 12, 29), "DATE_SUIVI")]:
    ws.cell(r, 1, lab).font = F(bold=True)
    c = ws.cell(r, 3, val)
    c.number_format = "DD/MM/YYYY"
    c.font = F(color="0000FF")
    c.fill = FILL_INPUT
    c.border = BORDER
    wb.defined_names[name] = DefinedName(name, attr_text=f"'0_Lisez-moi'!$C${r}")
    r += 1
r += 1
ws.cell(r, 1, "Délais de correction").font = F(size=12, bold=True, color=NAVY)
r += 1
delai_start = r
for g, j, txt in [("Critique", 1, "Risque d'accès illégitime en cours ou d'accès aux données de santé : correction sous 24 h"),
                  ("Élevée", 7, "Accès sensible injustifié : correction sous 7 jours"),
                  ("Moyenne", 30, "Écart sans accès sensible : correction sous 30 jours"),
                  ("Faible", 90, "Écart mineur ou exception à documenter : sous 90 jours")]:
    ws.cell(r, 1, g).font = F(bold=True)
    ws.cell(r, 2, txt)
    c = ws.cell(r, 3, j)
    c.font = F(color="0000FF")
    c.fill = FILL_INPUT
    c.border = BORDER
    r += 1
delai_end = r - 1
wb.defined_names["GRAVITES"] = DefinedName("GRAVITES", attr_text=f"'0_Lisez-moi'!$A${delai_start}:$A${delai_end}")
wb.defined_names["DELAIS"] = DefinedName("DELAIS", attr_text=f"'0_Lisez-moi'!$C${delai_start}:$C${delai_end}")
r += 1
ws.cell(r, 1, "Règles de contrôle").font = F(size=12, bold=True, color=NAVY)
regles = [
    ("R01", "Départ non traité : personne sortie dont le compte est actif (critique si connexion après la sortie)"),
    ("R02", "Accès résiduel après départ : droits AWS ou GitHub toujours présents après une sortie ou une fin de mission"),
    ("R03", "Prestataire terminé encore actif"),
    ("R04", "Compte orphelin (sans fiche RH) ou compte générique partagé"),
    ("R05", "Compte invité sans référence RH ni sponsor"),
    ("R06", "Compte en doublon pour une même personne"),
    ("R07", "Groupe Entra ID hors matrice des rôles (dont droits cumulés après mobilité)"),
    ("R08", "Droit AWS hors matrice (AdministratorAccess réservé aux comptes d'urgence)"),
    ("R09", "Rôle GitHub hors matrice"),
    ("R10", "MFA non enregistré"),
    ("R11", "Compte inactif depuis plus de 90 jours"),
    ("R12", "Compte de service utilisé en connexion interactive"),
    ("R13", "Authentification à deux facteurs GitHub désactivée"),
]
for code, txt in regles:
    r += 1
    ws.cell(r, 1, code).font = F(bold=True)
    ws.cell(r, 2, txt).alignment = WRAP
for row in ws.iter_rows(min_row=4, max_row=r):
    for cell in row:
        if cell.font.name != FONT:
            cell.font = F(bold=cell.font.bold)

# ------------------------------------------------------------ 1. Matrice des rôles
ws = wb.create_sheet("1_Matrice_roles")
title(ws, "Matrice des rôles (RBAC)", "Seuls les droits listés ici sont autorisés. Tout autre droit est signalé comme excédentaire.")
cols = ["Rôle", "Libellé", "Groupes Entra ID", "Droits AWS (compte : jeu d'autorisations)", "Rôle GitHub", "Console MediSoft Care"]
header(ws, 4, cols, [12, 30, 42, 58, 20, 20])
i = 5
for code, (lib, grp, aws_d, gh_r, console) in MATRICE.items():
    for j, v in enumerate([code, lib, "\n".join(grp), "\n".join(aws_d) or "—", gh_r, console], start=1):
        body(ws.cell(i, j, v), center=j in (1, 5, 6), bold=j == 1)
    i += 1
i += 1
ws.cell(i, 1, "Comptes techniques déclarés").font = F(size=12, bold=True, color=NAVY)
i += 1
header(ws, i, ["Compte", "Usage", "Propriétaire", "Droits AWS", "", ""], [12, 30, 42, 58, 20, 20])
for upn, (lib, owner, droits) in COMPTES_TECHNIQUES.items():
    i += 1
    for j, v in enumerate([upn, lib, owner, "\n".join(droits) or "—"], start=1):
        body(ws.cell(i, j, v))
ws.freeze_panes = "C5"

# ------------------------------------------------------------ 2. Anomalies et décisions
ws = wb.create_sheet("2_Anomalies")
title(ws, "Anomalies détectées et décisions",
      "Colonnes A à I : sortie du script. Colonnes J à N : décisions de la réunion de revue et suivi. Date limite et statut calculés.")
cols = ["ID", "Règle", "Gravité", "Système", "Compte", "Personne", "Constat", "Recommandation", "Décideur",
        "Décision", "Justification / commentaire", "Responsable correction", "Date limite", "Date de correction", "Statut"]
header(ws, 4, cols, [7, 24, 10, 9, 28, 26, 55, 40, 14, 18, 48, 16, 11, 12, 18])
start = 5
for i, rw in enumerate(rows, start=start):
    dec, just, resp, dcorr = DECISIONS[rw["id"]]
    vals = [rw["id"], rw["regle"], rw["gravite"], rw["systeme"], rw["compte"], rw["personne"], rw["constat"],
            rw["recommandation"], rw["decideur"], dec, just, resp, None, dcorr, None]
    for j, v in enumerate(vals, start=1):
        body(ws.cell(i, j, v), center=j in (1, 3, 4, 9, 13, 14, 15), bold=j == 1)
    ws.cell(i, 13, f"=DATE_REVUE+INDEX(DELAIS,MATCH(C{i},GRAVITES,0))").number_format = "DD/MM/YYYY"
    ws.cell(i, 14).number_format = "DD/MM/YYYY"
    ws.cell(i, 15, f'=IF(N{i}="",IF(DATE_SUIVI>M{i},"En retard","À corriger"),IF(N{i}<=M{i},"Corrigé dans les délais","Corrigé hors délai"))')
    for j in (10, 11, 12, 14):
        ws.cell(i, j).fill = FILL_INPUT
        ws.cell(i, j).font = F(color="0000FF")
end = start + len(rows) - 1
grav_cf(ws, f"C{start}:C{end}")
for val, fill in (("Corrigé dans les délais", GREEN), ("Corrigé hors délai", YELLOW), ("En retard", RED), ("À corriger", GREY)):
    ws.conditional_formatting.add(f"O{start}:O{end}", CellIsRule(operator="equal", formula=[f'"{val}"'], fill=fill))
dv = DataValidation(type="list", formula1='"Désactiver,Désactiver + incident,Désactiver puis supprimer,Désactiver temporairement,Supprimer,Retirer le droit,Retirer les accès,Retirer — élévation à la demande,Rétrograder,Corriger,Conserver avec expiration,Conserver (justifié)"', allow_blank=True)
ws.add_data_validation(dv)
dv.add(f"J{start}:J{end}")
ws.freeze_panes = "F5"
ws.auto_filter.ref = f"A4:O{end}"
rngA = lambda col: f"'2_Anomalies'!${col}${start}:${col}${end}"

# ------------------------------------------------------------ 3. Synthèse
ws = wb.create_sheet("3_Synthese")
title(ws, "Synthèse de la revue des accès — T4 2026", "Indicateurs calculés à partir de l'onglet 2.")
ws.column_dimensions["A"].width = 46
for col in "BCDEFG":
    ws.column_dimensions[col].width = 14
ws["A4"] = "Indicateurs clés"
ws["A4"].font = F(size=12, bold=True, color=NAVY)
kpis = [
    ("Comptes Entra ID revus", NB["export_entra_id.csv"], "0", True),
    ("Affectations AWS revues", NB["export_aws_identity_center.csv"], "0", True),
    ("Membres GitHub revus", NB["export_github.csv"], "0", True),
    ("Anomalies détectées", f"=COUNTA({rngA('A')})", "0", False),
    ("dont critiques", f'=COUNTIF({rngA("C")},"Critique")', "0", False),
    ("Anomalies corrigées au point de suivi", f'=COUNTIF({rngA("O")},"Corrigé*")', "0", False),
    ("Taux de correction", "=IFERROR(B10/B8,0)", "0%", False),
    ("Corrections dans les délais", f'=IFERROR(COUNTIF({rngA("O")},"Corrigé dans les délais")/B10,0)', "0%", False),
    ("Anomalies en retard", f'=COUNTIF({rngA("O")},"En retard")', "0", False),
    ("Incidents de sécurité ouverts suite à la revue", f'=COUNTIF({rngA("J")},"*incident*")', "0", False),
]
for k, (lab, val, fmt, is_input) in enumerate(kpis, start=5):
    a = ws.cell(k, 1, lab)
    body(a, bold=True)
    b = ws.cell(k, 2, val)
    body(b, center=True)
    b.number_format = fmt
    b.font = F(color="0000FF") if is_input else F(bold=True, size=11, color=NAVY)
    if is_input:
        b.fill = FILL_INPUT
ws.cell(15, 1, "Les trois premiers chiffres sont saisis à partir des exports (nombre de lignes) ; les autres sont calculés.").font = F(italic=True, size=9, color="595959")

t0 = 17
ws.cell(t0 - 1, 1, "Anomalies par gravité et par système").font = F(size=12, bold=True, color=NAVY)
header(ws, t0, ["Gravité", "Entra ID", "AWS", "GitHub", "Total", "Corrigées", "En retard"], [46, 14, 14, 14, 14, 14, 14])
for k, g in enumerate(["Critique", "Élevée", "Moyenne", "Faible"], start=t0 + 1):
    body(ws.cell(k, 1, g), bold=True)
    for j, s in enumerate(["Entra ID", "AWS", "GitHub"], start=2):
        body(ws.cell(k, j, f'=COUNTIFS({rngA("C")},$A{k},{rngA("D")},"{s}")'), center=True)
    body(ws.cell(k, 5, f"=SUM(B{k}:D{k})"), center=True, bold=True)
    body(ws.cell(k, 6, f'=COUNTIFS({rngA("C")},$A{k},{rngA("O")},"Corrigé*")'), center=True)
    body(ws.cell(k, 7, f'=COUNTIFS({rngA("C")},$A{k},{rngA("O")},"En retard")'), center=True)
grav_cf(ws, f"A{t0+1}:A{t0+4}")
tot = t0 + 5
body(ws.cell(tot, 1, "Total"), bold=True)
for j in range(2, 8):
    L = ws.cell(tot, j).column_letter
    c = ws.cell(tot, j, f"=SUM({L}{t0+1}:{L}{tot-1})")
    body(c, center=True, bold=True)
for j in range(1, 8):
    ws.cell(tot, j).fill = FILL_LIGHT

r0 = tot + 3
ws.cell(r0 - 1, 1, "Anomalies par règle").font = F(size=12, bold=True, color=NAVY)
header(ws, r0, ["Règle", "Nombre"], [46, 14])
codes = ["R01", "R02", "R03", "R04", "R05", "R06", "R07", "R08", "R09", "R10", "R11", "R12", "R13"]
lib = dict(regles)
for k, code in enumerate(codes, start=r0 + 1):
    body(ws.cell(k, 1, f"{code} — {lib[code].split(":")[0].strip()}"), bold=True)
    body(ws.cell(k, 2, f'=COUNTIF({rngA("B")},"{code}*")'), center=True)
rend = r0 + len(codes)

ch = BarChart()
ch.type = "bar"
ch.title = "Anomalies par règle"
ch.legend = None
ch.add_data(Reference(ws, min_col=2, min_row=r0, max_row=rend), titles_from_data=True)
ch.set_categories(Reference(ws, min_col=1, min_row=r0 + 1, max_row=rend))
ch.height, ch.width = 9, 16
ws.add_chart(ch, "I4")

ch2 = BarChart()
ch2.type = "col"
ch2.grouping = "stacked"
ch2.overlap = 100
ch2.title = "Anomalies par gravité et système"
ch2.add_data(Reference(ws, min_col=2, max_col=4, min_row=t0, max_row=t0 + 4), titles_from_data=True)
ch2.set_categories(Reference(ws, min_col=1, min_row=t0 + 1, max_row=t0 + 4))
ch2.height, ch2.width = 8, 16
ws.add_chart(ch2, "I23")

for w in wb.worksheets:
    w.sheet_view.showGridLines = False
    w.page_setup.orientation = "landscape"
    w.sheet_properties.pageSetUpPr.fitToPage = True
    w.page_setup.fitToWidth = 1
    w.page_setup.fitToHeight = 0
wb.save(OUT)
print("saved", OUT)
