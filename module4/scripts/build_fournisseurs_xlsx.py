# -*- coding: utf-8 -*-
"""Registre des fournisseurs et questionnaire d'évaluation SaaS — MediSoft (module 4)."""
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName

OUT = Path(__file__).resolve().parent.parent / "output" / "Registre_fournisseurs_MediSoft.xlsx"
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
        ws.column_dimensions[cell.column_letter].width = w
    ws.row_dimensions[row].height = 36


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


# ------------------------------------------------------------------ 0. Lisez-moi
ws = wb.active
ws.title = "0_Lisez-moi"
title(ws, "MediSoft — Registre des fournisseurs et évaluation sécurité",
      "Module 4 du projet GRC. Application de MS-POL-10 (gestion des fournisseurs). Données fictives, situation au 20/01/2027.")
ws.column_dimensions["A"].width = 30
ws.column_dimensions["B"].width = 95
ws.column_dimensions["C"].width = 14
r = 4
ws.cell(r, 1, "Date de référence").font = F(bold=True)
c = ws.cell(r, 3, date(2027, 1, 20))
c.number_format = "DD/MM/YYYY"
body(c, center=True, inp=True)
wb.defined_names["DATE_REF"] = DefinedName("DATE_REF", attr_text="'0_Lisez-moi'!$C$4")
r += 2
ws.cell(r, 1, "Criticité (calculée)").font = F(size=12, bold=True, color=NAVY)
for t, d in [("Tier 1 — Critique", "Le fournisseur traite des données de santé (C3) OU a un accès à la production. Évaluation complète, revue annuelle, clauses renforcées, plan de sortie obligatoire."),
             ("Tier 2 — Important", "Le fournisseur traite des données confidentielles (C2). Questionnaire, revue tous les 2 ans, clauses standard."),
             ("Tier 3 — Standard", "Données publiques ou internes uniquement. Vérification simple, revue tous les 3 ans.")]:
    r += 1
    ws.cell(r, 1, t).font = F(bold=True)
    ws.cell(r, 2, d).alignment = WRAP
    ws.row_dimensions[r].height = 28
r += 2
ws.cell(r, 1, "Onglets").font = F(size=12, bold=True, color=NAVY)
for t, d in [("1_Registre", "Tous les fournisseurs, leur criticité, les preuves collectées, l'état des clauses et la date de prochaine revue"),
             ("2_Evaluation_HelpBot", "Questionnaire pondéré appliqué à un outil SaaS candidat, selon deux scénarios d'usage"),
             ("3_Synthese", "Indicateurs du programme de gestion des fournisseurs")]:
    r += 1
    ws.cell(r, 1, t).font = F(bold=True)
    ws.cell(r, 2, d).alignment = WRAP
r += 2
ws.cell(r, 1, "Notation du questionnaire").font = F(size=12, bold=True, color=NAVY)
for t, d in [("Note 2", "Exigence satisfaite, avec preuve"), ("Note 1", "Partiellement satisfaite, ou déclarative sans preuve"),
             ("Note 0", "Non satisfaite ou pas de réponse"), ("Poids 1 à 3", "Importance de la question (3 = essentielle)"),
             ("Bloquant", "Une note 0 sur une question bloquante entraîne un avis défavorable, quel que soit le score")]:
    r += 1
    ws.cell(r, 1, t).font = F(bold=True)
    ws.cell(r, 2, d)

# ------------------------------------------------------------------ 1. Registre
ws = wb.create_sheet("1_Registre")
title(ws, "Registre des fournisseurs", "Criticité, prochaine revue, statut et complétude contractuelle calculés automatiquement.")
cols = ["ID", "Fournisseur", "Service rendu", "Données traitées (niveau max)", "Accès à la production", "Criticité",
        "Localisation des données", "Attestations attendues", "Preuves collectées", "Dernière évaluation",
        "Revue tous les (mois)", "Prochaine revue", "Statut", "Clauses RGPD art. 28", "Clauses sécurité",
        "Plan de sortie", "Complétude contractuelle", "Actions / commentaires"]
header(ws, 4, cols, [7, 22, 30, 13, 11, 17, 18, 26, 11, 12, 10, 12, 16, 11, 11, 10, 12, 45])
D = lambda y, m, dd: date(y, m, dd)
FOURN = [
    ("F01", "Amazon Web Services", "Hébergement de la production (IaaS / PaaS), sauvegardes", "C3", "Oui", "UE — Paris (eu-west-3)",
     "ISO 27001, HDS activités 1 à 4, SOC 2", "Oui", D(2027, 1, 12), "Oui", "Oui", "Non",
     "Attestations téléchargées sur AWS Artifact. Plan de sortie à rédiger (exigence DORA des clients)"),
    ("F02", "Microsoft (Entra ID, Intune)", "Annuaire, SSO, gestion des postes", "C2", "Oui", "UE",
     "ISO 27001, SOC 2", "Oui", D(2027, 1, 14), "Oui", "Oui", "Non", "Fournisseur d'identité : son indisponibilité bloque tous les accès. Procédure de bris de glace en place"),
    ("F03", "GitHub", "Code source, CI/CD", "C2", "Oui", "États-Unis / UE",
     "SOC 2, ISO 27001", "Oui", D(2027, 1, 14), "Oui", "Oui", "Non", "Accès à la production via la CI/CD. SSO SAML activé suite à la revue des accès (module 3)"),
    ("F04", "Google Workspace", "Messagerie, bureautique", "C2", "Non", "UE / États-Unis",
     "ISO 27001, SOC 2", "Non", None, "Oui", "Non", "Non", "Interdiction de stocker des données de santé (MS-POL-07). Évaluation à planifier"),
    ("F05", "Slack", "Messagerie instantanée", "C2", "Non", "États-Unis",
     "ISO 27001, SOC 2", "Non", None, "Oui", "Non", "Non", "Rappel : aucune donnée de santé dans les canaux"),
    ("F06", "Studio Kappa (freelance)", "Développement de l'application mobile", "C2", "Non", "France",
     "Aucune — questionnaire + clauses", "Non", None, "Non", "Non", "Non", "Contrat sans clause de sécurité (constat module 1, A.8.30). Avenant à signer : MS-MOD-03 §2"),
    ("F07", "NuageOps SAS", "Infogérance Ops en renfort (astreinte)", "C3", "Oui", "France",
     "ISO 27001 ou questionnaire complet", "Oui", D(2027, 1, 18), "Oui", "Oui", "Oui", "Questionnaire complet reçu, score 78 %. Accès production uniquement par élévation à la demande"),
    ("F08", "Cabinet Audit & Conformité", "Audit interne ISO 27001", "C2", "Non", "France",
     "Accord de confidentialité", "Oui", D(2026, 9, 1), "Oui", "Oui", "N/A", "Comptes invités expirant au 31/01/2027 (revue des accès F-023)"),
    ("F09", "HelpBot AI", "Chatbot et résumé de tickets par IA (candidat)", "C3", "Non", "UE — Irlande ; modèle d'IA d'un sous-traitant américain",
     "ISO 27001, HDS si données de santé, SOC 2", "Oui", D(2027, 1, 19), "Non", "Non", "Non", "En évaluation : voir onglet 2 et MS-ENR-02. Avis défavorable pour les tickets du support N2"),
    ("F10", "CyberQuiz", "Plateforme de sensibilisation (e-learning, phishing simulé)", "C1", "Non", "France",
     "Questionnaire simplifié", "Non", None, "Oui", "Non", "Non", "Traite nom, prénom et e-mail des salariés"),
    ("F11", "InfoMaintenance", "Maintenance des postes de travail", "C2", "Non", "France",
     "Accord de confidentialité", "Non", None, "Non", "Non", "N/A", "Maintenance non tracée (constat module 1, A.7.13)"),
]
start = 5
for i, f in enumerate(FOURN, start=start):
    (fid, nom, svc, cls, prod, loc, att, preuve, last, rgpd, secu, sortie, act) = f
    vals = [fid, nom, svc, cls, prod, None, loc, att, preuve, last, None, None, None, rgpd, secu, sortie, None, act]
    for j, v in enumerate(vals, start=1):
        body(ws.cell(i, j, v), center=j in (1, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17), bold=j == 2,
             inp=j in (4, 5, 9, 10, 14, 15, 16))
    ws.cell(i, 6, f'=IF(OR(D{i}="C3",E{i}="Oui"),"Tier 1 — Critique",IF(D{i}="C2","Tier 2 — Important","Tier 3 — Standard"))')
    ws.cell(i, 10).number_format = "DD/MM/YYYY"
    ws.cell(i, 11, f'=IF(LEFT(F{i},6)="Tier 1",12,IF(LEFT(F{i},6)="Tier 2",24,36))')
    ws.cell(i, 12, f'=IF(J{i}="","À évaluer",EDATE(J{i},K{i}))')
    ws.cell(i, 12).number_format = "DD/MM/YYYY"
    ws.cell(i, 13, f'=IF(J{i}="","Jamais évalué",IF(L{i}<DATE_REF,"Revue en retard","À jour"))')
    ws.cell(i, 17, f'=IFERROR(COUNTIF(N{i}:P{i},"Oui")/(3-COUNTIF(N{i}:P{i},"N/A")),0)')
    ws.cell(i, 17).number_format = "0%"
end = start + len(FOURN) - 1
for val, fill in (("Tier 1 — Critique", RED), ("Tier 2 — Important", YELLOW), ("Tier 3 — Standard", GREEN)):
    ws.conditional_formatting.add(f"F{start}:F{end}", CellIsRule(operator="equal", formula=[f'"{val}"'], fill=fill))
for val, fill in (("À jour", GREEN), ("Jamais évalué", RED), ("Revue en retard", ORANGE)):
    ws.conditional_formatting.add(f"M{start}:M{end}", CellIsRule(operator="equal", formula=[f'"{val}"'], fill=fill))
ws.conditional_formatting.add(f"Q{start}:Q{end}", CellIsRule(operator="lessThan", formula=["1"], fill=ORANGE))
for rng, lst in ((f"D{start}:D{end}", '"C0,C1,C2,C3"'), (f"E{start}:E{end}", '"Oui,Non"'),
                 (f"I{start}:I{end}", '"Oui,Non"'), (f"N{start}:P{end}", '"Oui,Non,N/A"')):
    dv = DataValidation(type="list", formula1=lst, allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(rng)
ws.freeze_panes = "C5"
ws.auto_filter.ref = f"A4:R{end}"
REG = lambda col: f"'1_Registre'!${col}${start}:${col}${end}"

# ------------------------------------------------------------------ 2. Évaluation HelpBot
ws = wb.create_sheet("2_Evaluation_HelpBot")
title(ws, "Évaluation sécurité — HelpBot AI (outil SaaS candidat)",
      "Scénario A : résumé des tickets du support N2 (données de santé). Scénario B : chatbot FAQ du site public (aucune donnée de santé).")
cols = ["N°", "Domaine", "Question", "Poids", "Bloquant", "Réponse du fournisseur", "Note (0-2)",
        "Applicable A", "Applicable B", "Points A", "Max A", "Points B", "Max B"]
header(ws, 4, cols, [6, 20, 50, 7, 9, 48, 8, 10, 10, 8, 8, 8, 8])
Q = [
    ("Gouvernance", "Certification ISO 27001 couvrant le service ?", 2, "Non", "Non : certification prévue en 2027", 0, "Oui", "Oui"),
    ("Gouvernance", "Rapport SOC 2 Type II de moins de 12 mois ?", 2, "Non", "Oui, rapport 2026 transmis sous accord de confidentialité", 2, "Oui", "Oui"),
    ("Gouvernance", "Contact sécurité identifié ?", 1, "Non", "Oui, adresse dédiée et RSSI nommé", 2, "Oui", "Oui"),
    ("Gouvernance", "Politique de sécurité communiquée ?", 1, "Non", "Résumé de 2 pages uniquement", 1, "Oui", "Oui"),
    ("Hébergement", "Certification HDS (obligatoire si données de santé) ?", 3, "Oui", "Non", 0, "Oui", "Non"),
    ("Hébergement", "Données stockées dans l'EEE ?", 3, "Oui", "Oui, Irlande", 2, "Oui", "Oui"),
    ("Hébergement", "Aucun traitement ni accès depuis un pays hors EEE ?", 3, "Non", "Modèle d'IA fourni par un sous-traitant américain (inférence en UE) ; support de nuit depuis les États-Unis", 0, "Oui", "Oui"),
    ("Hébergement", "Liste des sous-traitants ultérieurs fournie et tenue à jour ?", 2, "Non", "Oui, avec préavis de 30 jours avant changement", 2, "Oui", "Oui"),
    ("RGPD", "Contrat de sous-traitance (art. 28) disponible ?", 3, "Oui", "Oui, DPA standard", 2, "Oui", "Oui"),
    ("RGPD", "Les données des clients ne servent pas à entraîner les modèles ?", 3, "Oui", "Désactivable, uniquement sur l'offre Enterprise", 1, "Oui", "Oui"),
    ("RGPD", "Suppression des données en fin de contrat, durée de conservation paramétrable ?", 2, "Non", "Oui, suppression sous 30 jours", 2, "Oui", "Oui"),
    ("RGPD", "Masquage des données personnelles avant envoi au modèle d'IA ?", 2, "Non", "Partiel : e-mails et téléphones masqués, pas les informations médicales", 1, "Oui", "Oui"),
    ("Sécurité technique", "SSO (SAML / OIDC) et MFA ?", 2, "Non", "SSO uniquement sur l'offre Enterprise ; MFA disponible", 1, "Oui", "Oui"),
    ("Sécurité technique", "Chiffrement au repos et en transit ?", 2, "Non", "AES-256 au repos, TLS 1.2 minimum", 2, "Oui", "Oui"),
    ("Sécurité technique", "Journaux d'audit exportables vers notre SIEM ?", 2, "Non", "Oui, par API", 2, "Oui", "Oui"),
    ("Sécurité technique", "Test d'intrusion annuel par un tiers ?", 2, "Non", "Oui, synthèse 2026 fournie", 2, "Oui", "Oui"),
    ("Sécurité technique", "Délais de correction des vulnérabilités ?", 1, "Non", "Critiques sous 30 jours", 1, "Oui", "Oui"),
    ("Sécurité technique", "Protection contre l'injection de prompt et les fuites entre clients ?", 2, "Non", "Cloisonnement logique par client ; pas de tests spécifiques d'injection de prompt", 1, "Oui", "Oui"),
    ("Incidents et continuité", "Notification d'incident sous 24 h ?", 2, "Non", "Sous 72 heures", 1, "Oui", "Oui"),
    ("Incidents et continuité", "Engagement de disponibilité adapté ?", 1, "Non", "99,5 % par mois", 1, "Oui", "Oui"),
    ("Incidents et continuité", "Réversibilité : export complet des données ?", 2, "Non", "Export JSON complet", 2, "Oui", "Oui"),
    ("Incidents et continuité", "Plan de continuité testé ?", 1, "Non", "Non communiqué", 0, "Oui", "Oui"),
    ("Contractuel", "Droit d'audit du client ?", 2, "Non", "Questionnaire annuel uniquement, pas d'audit sur site", 1, "Oui", "Oui"),
    ("Contractuel", "Assurance cyber et responsabilité ?", 1, "Non", "Assurance cyber de 5 M€", 2, "Oui", "Oui"),
]
qs = 5
for i, (dom, q, w, blo, rep, note, a, b) in enumerate(Q, start=qs):
    vals = [i - qs + 1, dom, q, w, blo, rep, note, a, b]
    for j, v in enumerate(vals, start=1):
        body(ws.cell(i, j, v), center=j in (1, 4, 5, 7, 8, 9), inp=j in (4, 5, 6, 7, 8, 9))
    ws.cell(i, 10, f'=IF(H{i}="Oui",D{i}*G{i},0)')
    ws.cell(i, 11, f'=IF(H{i}="Oui",D{i}*2,0)')
    ws.cell(i, 12, f'=IF(I{i}="Oui",D{i}*G{i},0)')
    ws.cell(i, 13, f'=IF(I{i}="Oui",D{i}*2,0)')
    for j in range(10, 14):
        body(ws.cell(i, j), center=True)
qe = qs + len(Q) - 1
ws.conditional_formatting.add(f"G{qs}:G{qe}", CellIsRule(operator="equal", formula=["0"], fill=RED))
ws.conditional_formatting.add(f"G{qs}:G{qe}", CellIsRule(operator="equal", formula=["1"], fill=YELLOW))
ws.conditional_formatting.add(f"G{qs}:G{qe}", CellIsRule(operator="equal", formula=["2"], fill=GREEN))
ws.conditional_formatting.add(f"A{qs}:I{qe}", FormulaRule(formula=[f'AND($E{qs}="Oui",$G{qs}=0,$H{qs}="Oui")'], font=F(bold=True, color="9C0006")))
dv = DataValidation(type="whole", operator="between", formula1="0", formula2="2")
ws.add_data_validation(dv)
dv.add(f"G{qs}:G{qe}")

s = qe + 2
ws.cell(s, 2, "Résultat").font = F(size=12, bold=True, color=NAVY)
header_row = s + 1
for j, h in enumerate(["", "Indicateur", "Scénario A — tickets N2", "", "", "Scénario B — chatbot FAQ public"], start=1):
    if h:
        c = ws.cell(header_row, j, h)
        c.font = F(bold=True, color="FFFFFF")
        c.fill = FILL_HEAD
        c.alignment = CENTER
lines = [
    ("Score pondéré", f"=IFERROR(SUM(J{qs}:J{qe})/SUM(K{qs}:K{qe}),0)", f"=IFERROR(SUM(L{qs}:L{qe})/SUM(M{qs}:M{qe}),0)", "0.0%"),
    ("Questions bloquantes non satisfaites", f'=COUNTIFS(E{qs}:E{qe},"Oui",G{qs}:G{qe},0,H{qs}:H{qe},"Oui")',
     f'=COUNTIFS(E{qs}:E{qe},"Oui",G{qs}:G{qe},0,I{qs}:I{qe},"Oui")', "0"),
]
for k, (lab, fa, fb, fmt) in enumerate(lines, start=header_row + 1):
    body(ws.cell(k, 2, lab), bold=True)
    ca = ws.cell(k, 3, fa)
    cb = ws.cell(k, 6, fb)
    for c in (ca, cb):
        body(c, center=True, bold=True)
        c.number_format = fmt
avis = header_row + 3
body(ws.cell(avis, 2, "Avis"), bold=True)
for col, sc, bl in ((3, f"C{header_row+1}", f"C{header_row+2}"), (6, f"F{header_row+1}", f"F{header_row+2}")):
    c = ws.cell(avis, col, f'=IF({bl}>0,"Défavorable (exigence bloquante)",IF({sc}>=0.8,"Favorable",IF({sc}>=0.6,"Favorable sous conditions","Défavorable")))')
    body(c, center=True, bold=True)
ws.merge_cells(start_row=avis, start_column=3, end_row=avis, end_column=5)
for rr in (header_row + 1, header_row + 2):
    ws.merge_cells(start_row=rr, start_column=3, end_row=rr, end_column=5)
for val, fill in (("Favorable", GREEN), ("Favorable sous conditions", YELLOW)):
    ws.conditional_formatting.add(f"C{avis}:F{avis}", CellIsRule(operator="equal", formula=[f'"{val}"'], fill=fill))
ws.conditional_formatting.add(f"C{avis}:F{avis}", FormulaRule(formula=[f'LEFT(C{avis},11)="Défavorabl"'], fill=RED))
ws.cell(avis + 1, 2, "Seuils : ≥ 80 % favorable ; 60 à 80 % favorable sous conditions ; < 60 % défavorable. Toute exigence bloquante non satisfaite rend l'avis défavorable.").font = F(italic=True, size=9, color="595959")
ws.freeze_panes = "D5"
EV = (header_row, avis)

# ------------------------------------------------------------------ 3. Synthèse
ws = wb.create_sheet("3_Synthese")
title(ws, "Synthèse — programme de gestion des fournisseurs", "Indicateurs calculés à partir des onglets 1 et 2.")
ws.column_dimensions["A"].width = 55
ws.column_dimensions["B"].width = 18
k = 4
items = [
    ("Fournisseurs recensés", f"=COUNTA({REG('A')})", "0"),
    ("dont Tier 1 — Critique", f'=COUNTIF({REG("F")},"Tier 1*")', "0"),
    ("dont Tier 2 — Important", f'=COUNTIF({REG("F")},"Tier 2*")', "0"),
    ("dont Tier 3 — Standard", f'=COUNTIF({REG("F")},"Tier 3*")', "0"),
    ("Fournisseurs Tier 1 évalués et à jour", f'=COUNTIFS({REG("F")},"Tier 1*",{REG("M")},"À jour")', "0"),
    ("Taux d'évaluation des fournisseurs Tier 1", "=IFERROR(B9/B6,0)", "0%"),
    ("Fournisseurs jamais évalués", f'=COUNTIF({REG("M")},"Jamais évalué")', "0"),
    ("Fournisseurs avec clauses RGPD art. 28 signées (hors N/A)", f'=COUNTIF({REG("N")},"Oui")', "0"),
    ("Fournisseurs Tier 1 sans plan de sortie", f'=COUNTIFS({REG("F")},"Tier 1*",{REG("P")},"Non")', "0"),
    ("Complétude contractuelle moyenne", f"=IFERROR(AVERAGE({REG('Q')}),0)", "0%"),
    ("Évaluation HelpBot AI — avis scénario A", f"='2_Evaluation_HelpBot'!C{EV[1]}", "@"),
    ("Évaluation HelpBot AI — avis scénario B", f"='2_Evaluation_HelpBot'!F{EV[1]}", "@"),
]
for k, (lab, f, fmt) in enumerate(items, start=5):
    body(ws.cell(k, 1, lab), bold=True)
    c = ws.cell(k, 2, f)
    body(c, center=True, bold=True)
    c.number_format = fmt
    c.font = F(bold=True, size=11, color=NAVY)
ws.column_dimensions["B"].width = 34

for w in wb.worksheets:
    w.sheet_view.showGridLines = False
    w.page_setup.orientation = "landscape"
    w.sheet_properties.pageSetUpPr.fitToPage = True
    w.page_setup.fitToWidth = 1
    w.page_setup.fitToHeight = 0
wb.save(OUT)
print("saved", OUT)
