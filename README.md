# MediSoft — Projet GRC complet : mise en conformité d'un éditeur de logiciel de santé

> Projet personnel d'**Elie MEHINTO**, étudiant en Master 2 Cybersécurité & Réseaux, **en recherche de stage de fin d'études et d'alternance en cybersécurité (GRC, SOC)**.

## En une phrase

J'ai mis en place, de A à Z, le **système de management de la sécurité** d'une entreprise fictive mais réaliste, **MediSoft**, éditeur SaaS de dossier patient informatisé : depuis l'analyse des obligations réglementaires jusqu'à la préparation de l'audit de certification.

## Pourquoi ce projet

Ce projet est construit à partir des **missions réelles d'offres de stage GRC** (banque, assurance, éditeurs) : analyse des obligations réglementaires, mise à jour des politiques, gestion des accès, dérogations, qualification des incidents, sensibilisation, préparation d'audit, tableaux de bord. Chaque module reproduit ces missions et produit les livrables qu'un stagiaire ou un alternant GRC rédige en entreprise.

## L'entreprise

| | |
|---|---|
| Activité | Dossier patient informatisé en SaaS (MediSoft Care), application mobile pour les patients, module tiers payant pour les mutuelles |
| Taille | 85 salariés, environ 120 établissements de santé clients et 3 mutuelles |
| Hébergement | AWS, région Paris |
| Point de départ | Pas de RSSI, pas de PSSI, pas de procédure ; analyse de risques EBIOS RM réalisée ([dépôt dédié](https://github.com/eliemehintookou/ebios-rm-risk-analysis)) |
| Cadre réglementaire | RGPD, hébergement de données de santé (HDS v2.0), secret médical, NIS2, DORA (via les clients assureurs), Cyber Resilience Act, ISO 27001 |

## Les 6 modules

| Module | Sujet | Livrables principaux | Missions couvertes |
|---|---|---|---|
| [1](module1/) | **Conformité réglementaire et analyse d'écarts** | Registre de 12 textes ; analyse d'écarts des clauses 4 à 10 ; déclaration d'applicabilité des 93 mesures ISO 27001 ; plan d'action en 18 chantiers | Analyser les obligations (DORA, RGPD…) et leurs impacts ; veille réglementaire |
| [2](module2/) | **Gouvernance documentaire** | PSSI ; organisation et RACI ; 8 politiques ; charte ; procédure de dérogation ; gestion documentaire | Mettre à jour les référentiels (politiques, procédures) ; formaliser les dérogations |
| [3](module3/) | **Accès et habilitations** | Matrice des rôles ; script Python de revue des accès (13 règles, 32 anomalies) ; décisions et PV ; procédure arrivées / mobilités / départs | Gestion des accès et habilitations ; revue des droits |
| [4](module4/) | **Projets et fournisseurs** | Politique et registre des fournisseurs ; évaluation d'un outil d'IA ; check-list projet ; clauses DORA ; cahier des charges de pentest ; comparatif des prestations | Vérifier la conformité des outils SaaS ; check-lists pour les chefs de projet ; préparer les pentests ; étudier les prestations cyber du marché |
| [5](module5/) | **Incidents et sensibilisation** | Procédure d'incident et de notification ; 4 playbooks ; qualification de messages signalés ; 2 rapports d'incident ; programme de sensibilisation ; newsletter, alerte, guide, veille | Qualifier les incidents (phishing) ; sensibilisation et communication cyber ; veille |
| [6](module6/) | **Pilotage et audit** | Tableau de bord (18 KPI) ; rapport d'audit interne ; revue de direction ; dossier de preuves ; registre des non-conformités | Tableaux de bord et indicateurs ; contribuer aux audits ; collecter les preuves |

## L'histoire du projet en chiffres

| Étape | Résultat |
|---|---|
| **Novembre 2026 — État des lieux** | Maturité ISO 27001 de 1,0 sur 5 ; 5 % de conformité ; certificat HDS obsolète ; 42 mesures prioritaires |
| **Décembre 2026 — Première revue des accès** | 32 anomalies, dont 7 critiques ; **2 accès après départ** qui deviennent des incidents de sécurité |
| **Janvier 2027 — Fournisseurs et sensibilisation** | Outil d'IA refusé pour les données de santé, accepté pour une FAQ publique ; 1re campagne de phishing simulé : 24 % de clics |
| **Mars 2027 — Audit interne** | Maturité de 1,9 sur 5 ; 2 non-conformités majeures à lever avant la certification |
| **Avril 2027 — Revue de direction** | 10 décisions, dont le maintien de l'audit de certification HDS en juin 2027 |

## Compétences mises en œuvre

**Référentiels :** ISO/IEC 27001:2022 et 27002, EBIOS Risk Manager, guide d'hygiène de l'ANSSI, OWASP ASVS, WSTG et MASVS, CIS AWS Foundations.
**Réglementation :** RGPD, HDS v2.0, NIS2, DORA (art. 28 à 30), Cyber Resilience Act, secret médical.
**GRC :** analyse d'écarts, déclaration d'applicabilité, rédaction de politiques, RACI, dérogations, revue des accès, évaluation des fournisseurs, gestion des incidents, indicateurs, audit interne, revue de direction.
**Technique au service de la GRC :** Python (rapprochement de données, détection d'anomalies), Excel avancé (formules, tableaux de bord), AWS, Entra ID, GitHub.

## Parcours de lecture rapide (10 minutes)

1. [Synthèse du module 1](module1/README.md) : le point de départ et les constats majeurs
2. [La PSSI](module2/MS-POL-00_PSSI.md) : le document de tête
3. [Le PV de revue des accès](module3/MS-ENR-01_PV_revue_acces_T4-2026.md) : quand une anomalie devient un incident
4. [L'évaluation de l'outil d'IA](module4/MS-ENR-02_Evaluation_SaaS_HelpBot.md) : une décision nuancée
5. [La qualification des signalements](module5/MS-ENR-04_Qualification_signalements.md) : l'arbre de décision du phishing
6. [La revue de direction](module6/MS-ENR-07_Revue_de_direction_2027-04.md) : les décisions de la direction

## Avertissement

MediSoft, ses salariés, ses clients, ses fournisseurs fictifs, ses incidents et ses chiffres sont **inventés** à des fins d'apprentissage. Les références réglementaires et normatives sont réelles ; les dates d'application sont celles connues en novembre 2026 et doivent être revérifiées. Les noms de fournisseurs réels (AWS, Microsoft, GitHub, Google, Slack) sont utilisés pour le réalisme : leurs certifications sont à vérifier sur leurs portails de confiance.

---

📫 Contact : emploielie@gmail.com · Je recherche un **stage de fin d'études (6 mois, à partir de janvier / février 2027)** ou une **alternance** en cybersécurité, GRC ou SOC.
