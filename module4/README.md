# Module 4 — Sécurité des projets et des fournisseurs

> Projet GRC « fil rouge » sur **MediSoft**, éditeur fictif de logiciel de santé en SaaS.
> Ce module traite les chantiers **PA-13 (fournisseurs et contrats)** et **PA-14 (développement sécurisé)** du plan d'action du [module 1](../module1/), ainsi que les mesures A.5.8, A.5.19 à A.5.23, A.8.29, A.8.30 et A.8.34.

## Objectif

La sécurité de MediSoft dépend aussi de ce qui entre de l'extérieur : de **nouveaux projets**, de **nouveaux outils** et de **nouveaux fournisseurs**. Ce module donne aux équipes les outils pour intégrer la sécurité **avant** qu'une décision soit prise, plutôt que de découvrir les problèmes après.

## Contenu

| Document | Type | Ce qu'il apporte |
|---|---|---|
| [MS-POL-10](MS-POL-10_Gestion_fournisseurs.md) | Politique | Classement des fournisseurs en 3 niveaux de criticité, cycle de vie en 8 étapes, exigences bloquantes, répercussion de DORA sur les fournisseurs de MediSoft |
| [Registre_fournisseurs_MediSoft.xlsx](output/Registre_fournisseurs_MediSoft.xlsx) | Classeur | 11 fournisseurs, criticité, prochaine revue et complétude contractuelle calculées ; questionnaire pondéré ; indicateurs |
| [MS-MOD-01](MS-MOD-01_Checklist_securite_projet.md) | Modèle | Check-list sécurité en 5 étapes pour les chefs de projet, avec un tri en 6 questions (projet léger, standard ou sensible) |
| [MS-ENR-02](MS-ENR-02_Evaluation_SaaS_HelpBot.md) | Enregistrement | Évaluation complète d'un outil d'IA candidat, selon deux scénarios d'usage, avec une décision argumentée |
| [MS-MOD-03](MS-MOD-03_Clauses_securite_contrats.md) | Modèle | 15 clauses types par niveau de criticité, rédaction des clauses clés, et grille DORA art. 30 pour les contrats avec les clients assureurs |
| [MS-MOD-02](MS-MOD-02_Cahier_des_charges_pentest.md) | Modèle | Cahier des charges d'un test d'intrusion : périmètre, règles d'engagement, livrables, critères de choix |
| [MS-ENR-03](MS-ENR-03_Benchmark_tests_securite.md) | Étude | Comparatif de 7 façons de tester la sécurité et recommandation sur 2 ans |

## Résultats clés

**Registre des fournisseurs (au 20/01/2027)**

| Indicateur | Valeur |
|---|---|
| Fournisseurs recensés | 11 (5 Tier 1, 5 Tier 2, 1 Tier 3) |
| Fournisseurs Tier 1 évalués et à jour | 5 / 5 |
| Fournisseurs jamais évalués | 5 |
| Fournisseurs Tier 1 sans plan de sortie | 4 |
| Complétude contractuelle moyenne | 45 % |

**Évaluation de HelpBot AI**

| Scénario | Score | Avis |
|---|---|---|
| A — Résumé des tickets du support N2 (données de santé) | 63,8 % | **Défavorable** : pas de certification HDS (exigence bloquante) |
| B — Chatbot FAQ sur le site public | 68,2 % | **Favorable sous conditions** (6 conditions) |

**Contrats DORA avec les clients assureurs :** sur 15 exigences de l'article 30, **3 ne sont pas tenables aujourd'hui** (plan de sortie, PRA testé, objectifs de performance mesurés). Recommandation : les annoncer avec une date plutôt que de signer des engagements impossibles à tenir.

## Points clés à savoir expliquer

- **Le même outil peut être acceptable pour un usage et interdit pour un autre.** HelpBot AI est refusé pour les tickets contenant des données de santé et accepté pour une FAQ publique. On évalue un usage, pas seulement un fournisseur.
- **Une exigence bloquante prime sur le score.** 68 % ou 95 %, peu importe : sans HDS, on ne confie pas de données de santé.
- **DORA ne s'applique pas à MediSoft, mais MediSoft doit le répercuter sur ses propres fournisseurs.** Si AWS ne s'engage pas sur un point, MediSoft ne peut pas s'y engager envers ses clients.
- **La sécurité intervient au cadrage d'un projet, pas à la mise en production.** Corriger une architecture coûte beaucoup plus cher qu'intégrer une exigence dès le départ.
- **PASSI** : qualification délivrée par l'ANSSI aux prestataires d'audit. Elle garantit le niveau des auditeurs et rassure les clients.
- **On ne commande pas une red team sans équipe de détection.** Chaque type de test correspond à un niveau de maturité.

## Suite

- **Module 5 — Incidents et sensibilisation** : procédure de gestion des incidents et de notification (RGPD, NIS2, DORA, CRA), qualification du phishing, playbooks, programme de sensibilisation et traitement des incidents INC-2026-014 et 015 issus de la revue des accès.

---
*Entreprise, fournisseurs « HelpBot AI », « Studio Kappa », « NuageOps », « CyberQuiz », « InfoMaintenance » et « Cabinet Audit & Conformité » fictifs, réalisés dans un but d'apprentissage. Les certifications des fournisseurs réels (AWS, Microsoft, GitHub, Google, Slack) sont à vérifier sur leurs portails de confiance.*
