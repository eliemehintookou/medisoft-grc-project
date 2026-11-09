# Module 6 — Pilotage de la sécurité et préparation de l'audit

> Projet GRC « fil rouge » sur **MediSoft**, éditeur fictif de logiciel de santé en SaaS.
> Ce module traite les chantiers **PA-02 (certification HDS v2.0)** et **PA-17 (pilotage du SMSI)** du plan d'action du [module 1](../module1/), ainsi que les clauses 9 et 10 de l'ISO 27001.

## Objectif

Les modules 1 à 5 ont construit le système de management de la sécurité. Ce dernier module répond à la question de la direction : **« Où en est-on, et sommes-nous prêts pour l'audit de certification ? »** Il boucle la roue de l'amélioration continue : mesurer, auditer, décider, corriger.

```
   Planifier (module 1, 2)  →  Faire (modules 3, 4, 5)
          ↑                              ↓
   Agir (revue de direction,  ←  Vérifier (KPI, audit interne)
   actions correctives)
```

## Contenu

| Document | Ce qu'il apporte |
|---|---|
| [Tableau_de_bord_securite_MediSoft.xlsx](output/Tableau_de_bord_securite_MediSoft.xlsx) | Tableau de bord en 6 onglets : synthèse pour la direction, 18 KPI avec statut et tendance calculés, évolution de la maturité, suivi des 18 chantiers, dossier de preuves pour l'audit, registre des non-conformités |
| [MS-ENR-06](MS-ENR-06_Rapport_audit_interne_2027-03.md) — Rapport d'audit interne | Audit « à blanc » ISO 27001 / HDS : méthode par échantillonnage, points forts, 2 non-conformités majeures, 5 mineures, programme d'audit 2027 |
| [MS-ENR-07](MS-ENR-07_Revue_de_direction_2027-04.md) — Revue de direction | Compte rendu structuré selon la clause 9.3 : 7 éléments d'entrée examinés, 10 décisions |

## Résultats clés (fin du T1 2027)

| Indicateur | Valeur |
|---|---|
| KPI | 7 atteints, 9 en progrès, 2 en retard |
| Maturité annexe A (moyenne des thèmes) | 1,2 → **1,9** / 5 |
| Maturité clauses 4 à 10 | 0,7 → **1,8** / 5 |
| Avancement du plan d'action | 66 % (5 chantiers P1 en retard) |
| Préparation du dossier de preuves | 80 % (2 preuves manquantes) |
| Audit interne | **2 non-conformités majeures** (PRA non testé ; accès aux dossiers patients non journalisés sur l'API mobile), 5 mineures |
| Décision de la direction | Audit de certification HDS v2.0 maintenu en juin 2027, sous condition de lever les 2 majeures |

## Points clés à savoir expliquer

- **Un bon KPI a une cible, un seuil d'alerte, une source et un sens.** Sans cible, un chiffre ne dit rien. Sans source, il n'est pas crédible.
- **Le taux de signalement et le délai de désactivation parlent plus à la direction que le nombre de règles de pare-feu.** On choisit des indicateurs qui mesurent un risque, pas une activité.
- **L'audit interne vérifie l'application, pas seulement l'écrit** : par échantillonnage. C'est l'échantillon de 10 accès via l'API mobile qui a révélé la non-conformité majeure, invisible dans les documents.
- **Majeure ou mineure ?** Une majeure remet en cause le système et bloque la certification. Une mineure est un écart ponctuel.
- **La revue de direction a un contenu imposé** (clause 9.3) et doit produire des **décisions**. Un compte rendu sans décision ne prouve rien.
- **Être honnête dans le tableau de bord** : 5 chantiers en retard, c'est un signal utile. Un tableau de bord tout vert ne sert à rien.

## Reproduire le classeur

```bash
cd scripts
python build_dashboard_xlsx.py   # nécessite openpyxl
```

---
*Entreprise, chiffres et audits fictifs, réalisés dans un but d'apprentissage.*
