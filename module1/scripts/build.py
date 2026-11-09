# -*- coding: utf-8 -*-
"""Construit le classeur du module 1 (conformité réglementaire + ISO 27001) de MediSoft."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule, ColorScaleRule, FormulaRule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.chart import BarChart, Reference
from openpyxl.utils import get_column_letter

from data_registre import CONTEXTE, REGISTRE, PLAN_ACTION
from data_iso import CLAUSES, A, THEMES

OUT = "../MediSoft_M1_Conformite_ISO27001.xlsx"
FONT = "Arial"
NAVY = "1F3864"
LIGHT = "D9E2F3"
thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="top", wrap_text=True)

F_BASE = Font(name=FONT, size=10)
F_BOLD = Font(name=FONT, size=10, bold=True)
F_HEAD = Font(name=FONT, size=10, bold=True, color="FFFFFF")
F_TITLE = Font(name=FONT, size=16, bold=True, color=NAVY)
F_SUB = Font(name=FONT, size=12, bold=True, color=NAVY)
F_INPUT = Font(name=FONT, size=10, color="0000FF")
FILL_HEAD = PatternFill("solid", fgColor=NAVY)
FILL_LIGHT = PatternFill("solid", fgColor=LIGHT)
FILL_INPUT = PatternFill("solid", fgColor="FFF2CC")

GREEN = PatternFill("solid", fgColor="C6EFCE")
ORANGE = PatternFill("solid", fgColor="FFEB9C")
RED = PatternFill("solid", fgColor="FFC7CE")
GREY = PatternFill("solid", fgColor="E7E6E6")

wb = Workbook()


def title(ws, text, sub=None):
    ws["A1"] = text
    ws["A1"].font = F_TITLE
    if sub:
        ws["A2"] = sub
        ws["A2"].font = Font(name=FONT, size=10, italic=True, color="595959")


def header(ws, row, cols, widths=None):
    for i, c in enumerate(cols, start=1):
        cell = ws.cell(row=row, column=i, value=c)
        cell.font = F_HEAD
        cell.fill = FILL_HEAD
        cell.alignment = CENTER
        cell.border = BORDER
    if widths:
        for i, w in enumerate(widths, start=1):
            ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[row].height = 32


def body(cell, center=False, bold=False):
    cell.font = F_BOLD if bold else F_BASE
    cell.alignment = CENTER if center else WRAP
    cell.border = BORDER


def status_cf(ws, rng):
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Conforme"'], fill=GREEN))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Partiellement conforme"'], fill=ORANGE))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Non conforme"'], fill=RED))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Non applicable"'], fill=GREY))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"Non évalué"'], fill=GREY))


def prio_cf(ws, rng):
    first = rng.split(":")[0]
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'LEFT({first},2)="P1"'], fill=RED, font=Font(name=FONT, bold=True, color="9C0006")))
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'LEFT({first},2)="P2"'], fill=ORANGE))
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'LEFT({first},2)="P3"'], fill=GREEN))


def mat_cf(ws, rng):
    ws.conditional_formatting.add(rng, ColorScaleRule(start_type="num", start_value=0, start_color="F8696B",
                                                      mid_type="num", mid_value=2, mid_color="FFEB84",
                                                      end_type="num", end_value=4, end_color="63BE7B"))


# ---------------------------------------------------------------- 0. Lisez-moi
ws = wb.active
ws.title = "0_Lisez-moi"
title(ws, "MediSoft — Module 1 : conformité réglementaire et analyse d'écarts ISO/IEC 27001:2022",
      "Projet GRC « fil rouge » — entreprise fictive. Réalisé par Elie MEHINTO. Situation au 9 novembre 2026.")
ws.column_dimensions["A"].width = 28
ws.column_dimensions["B"].width = 95
ws.column_dimensions["C"].width = 14
r = 4
ws.cell(r, 1, "Objectif").font = F_SUB
r += 1
ws.cell(r, 1, "Pourquoi ce module ?").font = F_BOLD
ws.cell(r, 2, "Identifier les textes qui s'appliquent à MediSoft, mesurer l'écart entre la situation actuelle et la norme ISO 27001 (socle du HDS v2.0 et réponse à l'essentiel de NIS2), puis prioriser les actions. Les modules 2 à 6 du projet traitent ensuite chaque chantier du plan d'action.").alignment = WRAP
ws.row_dimensions[r].height = 45
r += 2
ws.cell(r, 1, "Onglets").font = F_SUB
tabs = [
    ("1_Contexte", "Hypothèses sur l'entreprise fictive (cohérentes avec l'analyse EBIOS RM)"),
    ("2_Registre", "Registre des obligations légales, réglementaires et contractuelles, avec leur impact et les preuves attendues"),
    ("3_Clauses_4-10", "Écarts sur les exigences du système de management (clauses 4 à 10 de l'ISO 27001)"),
    ("4_SoA_AnnexeA", "Déclaration d'applicabilité (DdA / SoA) : 93 mesures de l'annexe A, statut, écart, action"),
    ("5_Synthese", "Indicateurs calculés automatiquement et graphiques"),
    ("6_Plan_action", "Plan d'action priorisé, regroupé par chantier et relié aux modules du projet"),
]
for t, d in tabs:
    r += 1
    ws.cell(r, 1, t).font = F_BOLD
    ws.cell(r, 2, d).alignment = WRAP
r += 2
ws.cell(r, 1, "Paramètre").font = F_SUB
r += 1
ws.cell(r, 1, "Maturité cible").font = F_BOLD
ws.cell(r, 2, "Niveau minimal attendu pour qu'une exigence soit jugée conforme (modifiable). Toutes les colonnes Statut et la synthèse se recalculent.").alignment = WRAP
c = ws.cell(r, 3, 3)
c.font = F_INPUT
c.fill = FILL_INPUT
c.alignment = CENTER
c.border = BORDER
target_ref = f"'0_Lisez-moi'!$C${r}"
wb.defined_names["CIBLE_MATURITE"] = DefinedName("CIBLE_MATURITE", attr_text=target_ref)
r += 2
ws.cell(r, 1, "Échelle de maturité").font = F_SUB
scale = [
    (0, "Inexistant : rien n'est en place"),
    (1, "Initial : pratiques ponctuelles, non documentées"),
    (2, "Reproductible : pratique en place mais non formalisée ou incomplète"),
    (3, "Défini : documenté, validé et appliqué (niveau cible)"),
    (4, "Géré : mesuré par des indicateurs et contrôlé"),
    (5, "Optimisé : amélioration continue"),
]
for lvl, txt in scale:
    r += 1
    ws.cell(r, 1, lvl).alignment = Alignment(horizontal="left")
    ws.cell(r, 2, txt)
r += 2
ws.cell(r, 1, "Statut (calculé)").font = F_SUB
for s, d in [("Conforme", "Maturité ≥ cible"), ("Partiellement conforme", "Maturité entre 1 et cible − 1"),
             ("Non conforme", "Maturité = 0"), ("Non applicable", "Mesure exclue, avec justification")]:
    r += 1
    ws.cell(r, 1, s).font = F_BOLD
    ws.cell(r, 2, d)
r += 2
ws.cell(r, 1, "Justification (SoA)").font = F_SUB
for s, d in [("L", "Exigence légale ou réglementaire (RGPD, HDS, NIS2…)"), ("C", "Exigence contractuelle (clients, DORA)"),
             ("R", "Risque identifié dans l'analyse EBIOS RM"), ("B", "Bonne pratique")]:
    r += 1
    ws.cell(r, 1, s).font = F_BOLD
    ws.cell(r, 2, d)
r += 2
ws.cell(r, 1, "Priorités").font = F_SUB
for s, d in [("P1", "Critique : à traiter au premier trimestre (obligation légale ou risque majeur)"),
             ("P2", "Important : dans l'année"), ("P3", "Amélioration : selon les ressources")]:
    r += 1
    ws.cell(r, 1, s).font = F_BOLD
    ws.cell(r, 2, d)
r += 2
ws.cell(r, 1, "Codes couleur").font = F_SUB
r += 1
ws.cell(r, 1, "Texte bleu sur fond jaune").font = F_BOLD
ws.cell(r, 2, "Cellules de saisie : maturité, applicabilité, priorité. Tout le reste est calculé ou descriptif.")
r += 2
ws.cell(r, 1, "Sources").font = F_SUB
for s in [
    "ISO/IEC 27001:2022 et amendement 1:2024 ; ISO/IEC 27002:2022 (intitulés des mesures).",
    "HDS : référentiel de certification v2.0 (arrêté du 26/04/2024), esante.gouv.fr ; échéance de transition au 16/05/2026.",
    "NIS2 : directive (UE) 2022/2555 ; état de la transposition : leto.legal (examen à l'Assemblée nationale à partir du 09/11/2026), CNB (27/08/2026).",
    "DORA : règlement (UE) 2022/2554, art. 28 à 30. CRA : règlement (UE) 2024/2847. EHDS : règlement (UE) 2025/327.",
    "Les dates de mise en application du CRA, de l'EHDS et des référentiels ANS sont à revérifier lors de chaque revue du registre.",
]:
    r += 1
    ws.cell(r, 2, s).alignment = WRAP
for row in ws.iter_rows(min_row=4, max_row=r):
    for cell in row:
        if cell.font == Font() or cell.font.name != FONT:
            cell.font = Font(name=FONT, size=10, bold=cell.font.bold, color=cell.font.color)

# ---------------------------------------------------------------- 1. Contexte
ws = wb.create_sheet("1_Contexte")
title(ws, "Contexte et hypothèses — MediSoft", "Entreprise fictive. Ces hypothèses déterminent l'applicabilité des textes du registre.")
header(ws, 4, ["Élément", "Valeur retenue", "Source / commentaire"], [26, 80, 55])
for i, (a, b, cmt) in enumerate(CONTEXTE, start=5):
    for j, v in enumerate((a, b, cmt), start=1):
        body(ws.cell(i, j, v), bold=(j == 1))
ws.freeze_panes = "A5"

# ---------------------------------------------------------------- 2. Registre
ws = wb.create_sheet("2_Registre")
title(ws, "Registre des obligations légales, réglementaires et contractuelles",
      "Exigence ISO 27001 A.5.31. À revoir chaque semestre et à chaque évolution réglementaire.")
cols = ["ID", "Texte", "Référence", "Statut au 09/11/2026", "S'applique ?", "Rôle de MediSoft",
        "Pourquoi (critère d'applicabilité)", "Exigences clés", "Impact pour MediSoft",
        "Preuves attendues en audit", "Conformité actuelle", "Priorité", "Échéance", "Mesures ISO 27001 liées"]
header(ws, 4, cols, [8, 22, 30, 30, 13, 32, 42, 55, 45, 38, 16, 10, 16, 26])
start = 5
for i, row in enumerate(REGISTRE, start=start):
    for j, v in enumerate(row, start=1):
        body(ws.cell(i, j, v), center=j in (1, 5, 11, 12), bold=j == 2)
end_reg = start + len(REGISTRE) - 1
status_cf(ws, f"K{start}:K{end_reg}")
prio_cf(ws, f"L{start}:L{end_reg}")
ws.freeze_panes = "C5"
ws.auto_filter.ref = f"A4:N{end_reg}"
dv = DataValidation(type="list", formula1='"Conforme,Partiellement conforme,Non conforme,Non applicable,Non évalué"', allow_blank=True)
ws.add_data_validation(dv)
dv.add(f"K{start}:K{end_reg}")

# ---------------------------------------------------------------- 3. Clauses 4-10
ws = wb.create_sheet("3_Clauses_4-10")
title(ws, "Analyse d'écarts — exigences du SMSI (clauses 4 à 10)",
      "Un auditeur ISO 27001 commence par ces clauses : sans système de management, les mesures de l'annexe A ne suffisent pas.")
cols = ["Clause", "Chapitre", "Exigence", "État actuel chez MediSoft", "Maturité (0-5)", "Écart à la cible",
        "Statut", "Action recommandée", "Priorité", "Module du projet"]
header(ws, 4, cols, [8, 22, 38, 50, 11, 11, 20, 50, 10, 11])
chap = {"4": "4 - Contexte", "5": "5 - Leadership", "6": "6 - Planification", "7": "7 - Support",
        "8": "8 - Fonctionnement", "9": "9 - Évaluation", "10": "10 - Amélioration"}
start = 5
for i, (cid, req, etat, mat, act, prio, mod) in enumerate(CLAUSES, start=start):
    vals = [cid, chap[cid.split(".")[0]], req, etat, mat, None, None, act, prio, mod]
    for j, v in enumerate(vals, start=1):
        body(ws.cell(i, j, v), center=j in (1, 5, 6, 7, 9, 10))
    ws.cell(i, 6, f'=IF(E{i}="","",MAX(0,CIBLE_MATURITE-E{i}))')
    ws.cell(i, 7, f'=IF(E{i}="","À évaluer",IF(E{i}>=CIBLE_MATURITE,"Conforme",IF(E{i}>=1,"Partiellement conforme","Non conforme")))')
    for j in (5, 9):
        ws.cell(i, j).font = F_INPUT
        ws.cell(i, j).fill = FILL_INPUT
end_cl = start + len(CLAUSES) - 1
status_cf(ws, f"G{start}:G{end_cl}")
prio_cf(ws, f"I{start}:I{end_cl}")
mat_cf(ws, f"E{start}:E{end_cl}")
dv = DataValidation(type="whole", operator="between", formula1="0", formula2="5", allow_blank=True)
ws.add_data_validation(dv)
dv.add(f"E{start}:E{end_cl}")
dvp = DataValidation(type="list", formula1='"P1,P2,P3"', allow_blank=True)
ws.add_data_validation(dvp)
dvp.add(f"I{start}:I{end_cl}")
ws.freeze_panes = "D5"
ws.auto_filter.ref = f"A4:J{end_cl}"

# ---------------------------------------------------------------- 4. SoA
ws = wb.create_sheet("4_SoA_AnnexeA")
title(ws, "Déclaration d'applicabilité (SoA) — 93 mesures de l'annexe A de l'ISO/IEC 27001:2022",
      "Pour chaque mesure : applicable ou non (et pourquoi), état actuel, maturité, statut calculé, action. Constats EBIOS n° 1 à 11 repris.")
cols = ["Mesure", "Thème", "Intitulé", "Applicable", "Justification (L/C/R/B)", "État actuel chez MediSoft",
        "Maturité (0-5)", "Écart à la cible", "Statut", "Action recommandée", "Priorité", "Référence réglementaire", "Module du projet"]
header(ws, 4, cols, [8, 18, 40, 11, 13, 50, 11, 11, 20, 50, 10, 26, 11])
start = 5
for i, (cid, name, app, just, etat, mat, act, prio, reg, mod) in enumerate(A, start=start):
    theme = f"{cid.split('.')[0]} - {THEMES[cid.split('.')[0]]}"
    vals = [f"A.{cid}", theme, name, app, just, etat, mat, None, None, act, prio, reg, mod]
    for j, v in enumerate(vals, start=1):
        body(ws.cell(i, j, v), center=j in (1, 4, 5, 7, 8, 9, 11, 13))
    ws.cell(i, 8, f'=IF(OR(D{i}="Non",G{i}=""),"",MAX(0,CIBLE_MATURITE-G{i}))')
    ws.cell(i, 9, f'=IF(D{i}="Non","Non applicable",IF(G{i}="","À évaluer",IF(G{i}>=CIBLE_MATURITE,"Conforme",IF(G{i}>=1,"Partiellement conforme","Non conforme"))))')
    for j in (4, 7, 11):
        ws.cell(i, j).font = F_INPUT
        ws.cell(i, j).fill = FILL_INPUT
end_soa = start + len(A) - 1
status_cf(ws, f"I{start}:I{end_soa}")
prio_cf(ws, f"K{start}:K{end_soa}")
mat_cf(ws, f"G{start}:G{end_soa}")
dv = DataValidation(type="whole", operator="between", formula1="0", formula2="5", allow_blank=True)
ws.add_data_validation(dv)
dv.add(f"G{start}:G{end_soa}")
dva = DataValidation(type="list", formula1='"Oui,Non"', allow_blank=False)
ws.add_data_validation(dva)
dva.add(f"D{start}:D{end_soa}")
dvp = DataValidation(type="list", formula1='"P1,P2,P3,—"', allow_blank=True)
ws.add_data_validation(dvp)
dvp.add(f"K{start}:K{end_soa}")
ws.freeze_panes = "D5"
ws.auto_filter.ref = f"A4:M{end_soa}"

# ---------------------------------------------------------------- 5. Synthèse
ws = wb.create_sheet("5_Synthese")
title(ws, "Synthèse de la conformité — MediSoft", "Tous les chiffres sont calculés à partir des onglets 2, 3 et 4.")
S = "'4_SoA_AnnexeA'"
C = "'3_Clauses_4-10'"
R = "'2_Registre'"
rngS = lambda col: f"{S}!${col}${start}:${col}${end_soa}"
rngC = lambda col: f"{C}!${col}$5:${col}${end_cl}"
rngR = lambda col: f"{R}!${col}$5:${col}${end_reg}"

# Indicateurs clés
ws["A4"] = "Indicateurs clés"
ws["A4"].font = F_SUB
kpis = [
    ("Mesures de l'annexe A applicables", f'=COUNTIF({rngS("D")},"Oui")', "0"),
    ("Mesures exclues (justifiées)", f'=COUNTIF({rngS("D")},"Non")', "0"),
    ("Taux de conformité annexe A", f'=IFERROR(COUNTIF({rngS("I")},"Conforme")/B5,0)', "0.0%"),
    ("Maturité moyenne annexe A (/5)", f'=IFERROR(AVERAGEIF({rngS("D")},"Oui",{rngS("G")}),0)', "0.0"),
    ("Maturité moyenne clauses 4-10 (/5)", f'=IFERROR(AVERAGE({rngC("E")}),0)', "0.0"),
    ("Mesures en priorité P1", f'=COUNTIF({rngS("K")},"P1")', "0"),
    ("Textes applicables (hors « non » et « recommandé »)", f'=COUNTA({rngR("E")})-COUNTIF({rngR("E")},"Non")-COUNTIF({rngR("E")},"Recommandé")', "0"),
    ("Textes non conformes", f'=COUNTIF({rngR("K")},"Non conforme")', "0"),
]
for i, (lab, f, fmt) in enumerate(kpis, start=5):
    a = ws.cell(i, 1, lab)
    body(a, bold=True)
    b = ws.cell(i, 2, f)
    body(b, center=True)
    b.number_format = fmt
    b.font = Font(name=FONT, size=11, bold=True, color=NAVY)
kpi_end = 5 + len(kpis) - 1

# Table par thème
t0 = kpi_end + 3
ws.cell(t0 - 1, 1, "Annexe A — résultats par thème").font = F_SUB
header(ws, t0, ["Thème", "Nb mesures", "Applicables", "Conformes", "Partiellement", "Non conformes",
                "Taux de conformité", "Maturité moyenne", "Cible", "Mesures P1"])
themes = [f"{k} - {v}" for k, v in THEMES.items()]
for i, th in enumerate(themes, start=t0 + 1):
    q = f'$A{i}'
    vals = [th,
            f'=COUNTIF({rngS("B")},{q})',
            f'=COUNTIFS({rngS("B")},{q},{rngS("D")},"Oui")',
            f'=COUNTIFS({rngS("B")},{q},{rngS("I")},"Conforme")',
            f'=COUNTIFS({rngS("B")},{q},{rngS("I")},"Partiellement conforme")',
            f'=COUNTIFS({rngS("B")},{q},{rngS("I")},"Non conforme")',
            f'=IFERROR(D{i}/C{i},0)',
            f'=IFERROR(AVERAGEIFS({rngS("G")},{rngS("B")},{q},{rngS("D")},"Oui"),0)',
            '=CIBLE_MATURITE',
            f'=COUNTIFS({rngS("B")},{q},{rngS("K")},"P1")']
    for j, v in enumerate(vals, start=1):
        body(ws.cell(i, j, v), center=j > 1, bold=j == 1)
    ws.cell(i, 7).number_format = "0.0%"
    ws.cell(i, 8).number_format = "0.0"
tot = t0 + len(themes) + 1
ws.cell(tot, 1, "Total")
for j in range(2, 7):
    L = get_column_letter(j)
    ws.cell(tot, j, f"=SUM({L}{t0+1}:{L}{tot-1})")
ws.cell(tot, 7, f"=IFERROR(D{tot}/C{tot},0)")
ws.cell(tot, 8, f'=IFERROR(AVERAGEIF({rngS("D")},"Oui",{rngS("G")}),0)')
ws.cell(tot, 9, "=CIBLE_MATURITE")
ws.cell(tot, 10, f"=SUM(J{t0+1}:J{tot-1})")
for j in range(1, 11):
    c = ws.cell(tot, j)
    body(c, center=j > 1, bold=True)
    c.fill = FILL_LIGHT
ws.cell(tot, 7).number_format = "0.0%"
ws.cell(tot, 8).number_format = "0.0"
status_check = tot  # used for verification

# Table clauses par chapitre
c0 = tot + 3
ws.cell(c0 - 1, 1, "Clauses 4 à 10 — résultats par chapitre").font = F_SUB
header(ws, c0, ["Chapitre", "Nb exigences", "Conformes", "Partiellement", "Non conformes", "Maturité moyenne", "Cible"])
for i, ch in enumerate(chap.values(), start=c0 + 1):
    q = f"$A{i}"
    vals = [ch,
            f'=COUNTIF({rngC("B")},{q})',
            f'=COUNTIFS({rngC("B")},{q},{rngC("G")},"Conforme")',
            f'=COUNTIFS({rngC("B")},{q},{rngC("G")},"Partiellement conforme")',
            f'=COUNTIFS({rngC("B")},{q},{rngC("G")},"Non conforme")',
            f'=IFERROR(AVERAGEIF({rngC("B")},{q},{rngC("E")}),0)',
            '=CIBLE_MATURITE']
    for j, v in enumerate(vals, start=1):
        body(ws.cell(i, j, v), center=j > 1, bold=j == 1)
    ws.cell(i, 6).number_format = "0.0"
cend = c0 + len(chap)

# Table registre
g0 = cend + 3
ws.cell(g0 - 1, 1, "Registre réglementaire — conformité des textes").font = F_SUB
header(ws, g0, ["Conformité", "Nombre de textes"])
for i, s in enumerate(["Conforme", "Partiellement conforme", "Non conforme", "Non évalué", "Non applicable"], start=g0 + 1):
    body(ws.cell(i, 1, s), bold=True)
    body(ws.cell(i, 2, f'=COUNTIF({rngR("K")},$A{i})'), center=True)
status_cf(ws, f"A{g0+1}:A{g0+5}")

for col, w in zip("ABCDEFGHIJ", [44, 14, 13, 13, 14, 14, 16, 16, 9, 12]):
    ws.column_dimensions[col].width = w

# Graphiques
ch1 = BarChart()
ch1.type = "bar"
ch1.title = "Annexe A : maturité moyenne par thème (cible en comparaison)"
ch1.y_axis.title = "Maturité (0-5)"
ch1.y_axis.scaling.min = 0
ch1.y_axis.scaling.max = 5
data = Reference(ws, min_col=8, max_col=9, min_row=t0, max_row=t0 + len(themes))
cats = Reference(ws, min_col=1, min_row=t0 + 1, max_row=t0 + len(themes))
ch1.add_data(data, titles_from_data=True)
ch1.set_categories(cats)
ch1.height, ch1.width = 7.5, 16
ws.add_chart(ch1, "L4")

ch2 = BarChart()
ch2.type = "bar"
ch2.title = "Clauses 4 à 10 : maturité moyenne par chapitre"
ch2.y_axis.scaling.min = 0
ch2.y_axis.scaling.max = 5
data = Reference(ws, min_col=6, max_col=7, min_row=c0, max_row=cend)
cats = Reference(ws, min_col=1, min_row=c0 + 1, max_row=cend)
ch2.add_data(data, titles_from_data=True)
ch2.set_categories(cats)
ch2.height, ch2.width = 8.5, 16
ws.add_chart(ch2, "L21")

# ---------------------------------------------------------------- 6. Plan d'action
ws = wb.create_sheet("6_Plan_action")
title(ws, "Plan d'action priorisé — MediSoft",
      "Chantiers regroupant les écarts des onglets 2 à 4. Le module indique où le chantier est traité dans la suite du projet.")
cols = ["ID", "Chantier", "Actions", "Mesures / clauses ISO", "Exigence réglementaire", "Porteur",
        "Priorité", "Échéance", "Module du projet", "Statut", "Avancement"]
header(ws, 4, cols, [8, 22, 60, 30, 30, 18, 9, 12, 11, 12, 11])
start_pa = 5
for i, row in enumerate(PLAN_ACTION, start=start_pa):
    vals = list(row) + ["À lancer", 0]
    for j, v in enumerate(vals, start=1):
        body(ws.cell(i, j, v), center=j in (1, 7, 8, 9, 10, 11), bold=j == 2)
    ws.cell(i, 11).number_format = "0%"
    for j in (10, 11):
        ws.cell(i, j).font = F_INPUT
        ws.cell(i, j).fill = FILL_INPUT
end_pa = start_pa + len(PLAN_ACTION) - 1
prio_cf(ws, f"G{start_pa}:G{end_pa}")
dvs = DataValidation(type="list", formula1='"À lancer,En cours,Terminé,Bloqué"', allow_blank=True)
ws.add_data_validation(dvs)
dvs.add(f"J{start_pa}:J{end_pa}")
tp = end_pa + 2
ws.cell(tp, 2, "Avancement global du plan").font = F_BOLD
c = ws.cell(tp, 3, f"=IFERROR(AVERAGE(K{start_pa}:K{end_pa}),0)")
c.number_format = "0%"
c.font = Font(name=FONT, size=11, bold=True, color=NAVY)
ws.cell(tp + 1, 2, "Chantiers P1").font = F_BOLD
ws.cell(tp + 1, 3, f'=COUNTIF(G{start_pa}:G{end_pa},"P1")').font = F_BOLD
ws.freeze_panes = "C5"
ws.auto_filter.ref = f"A4:K{end_pa}"

for w in wb.worksheets:
    w.sheet_view.showGridLines = False
    w.sheet_properties.pageSetUpPr.fitToPage = True
    w.page_setup.orientation = "landscape"
    w.page_setup.fitToWidth = 1
    w.page_setup.fitToHeight = 0

wb.save(OUT)
print("saved", OUT, "soa rows", start, end_soa, "clauses", end_cl, "reg", end_reg)
