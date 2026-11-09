# Module 1 — Conformité réglementaire et analyse d'écarts ISO/IEC 27001:2022

> Projet GRC « fil rouge » sur **MediSoft**, éditeur fictif de logiciel de santé en SaaS (85 salariés, hébergé sur AWS Paris).
> Ce module fait suite à l'analyse de risques [EBIOS RM](https://github.com/eliemehintookou/ebios-rm-risk-analysis) et ouvre la série de modules du projet.
> Situation arrêtée au 9 novembre 2026.

## Objectif

Répondre à trois questions qu'un RSSI ou un auditeur pose dès sa prise de poste :

1. **Quelles règles s'appliquent à l'entreprise, et pourquoi ?** → registre des obligations
2. **Où en est-elle par rapport à la norme ISO 27001 ?** → analyse d'écarts sur les clauses 4 à 10 et les 93 mesures de l'annexe A (déclaration d'applicabilité)
3. **Par quoi commencer ?** → plan d'action priorisé

## Livrable

[`MediSoft_M1_Conformite_ISO27001.xlsx`](MediSoft_M1_Conformite_ISO27001.xlsx), avec 7 onglets (reproductible avec `scripts/build.py`) :

| Onglet | Contenu |
|---|---|
| 0_Lisez-moi | Méthode, échelle de maturité, légende, sources, maturité cible (paramètre modifiable) |
| 1_Contexte | Hypothèses sur l'entreprise, qui déterminent les textes applicables |
| 2_Registre | 12 textes analysés : rôle de MediSoft, critère d'applicabilité, exigences, impact, preuves attendues |
| 3_Clauses_4-10 | 25 exigences du système de management (SMSI) |
| 4_SoA_AnnexeA | 93 mesures : applicabilité justifiée, état actuel, maturité, statut calculé, action |
| 5_Synthese | Indicateurs et graphiques calculés par formules |
| 6_Plan_action | 18 chantiers priorisés, avec porteur, échéance et module du projet qui les traite |

Les statuts, écarts et indicateurs sont **calculés automatiquement** : si on modifie une maturité ou la cible, tout se met à jour.

## Méthode

- **Applicabilité des textes** : pour chaque texte, je pars du rôle juridique de MediSoft (sous-traitant RGPD, hébergeur infogéreur HDS, prestataire TIC au sens de DORA, fabricant au sens du CRA), puis je déduis les exigences et les preuves qu'un auditeur demanderait.
- **Maturité** : échelle de 0 (inexistant) à 5 (optimisé). Une exigence est conforme à partir du niveau 3 (documenté, validé et appliqué).
- **Justification de chaque mesure de la SoA** : L = légale, C = contractuelle, R = risque issu de l'EBIOS RM, B = bonne pratique. Les 11 constats de l'atelier 1 de l'EBIOS RM sont repris et rattachés aux mesures correspondantes.
- **Une exclusion justifiée** : A.7.6 (travail dans les zones sécurisées). Aucune donnée n'est hébergée dans les locaux, et le datacenter relève d'AWS (modèle de responsabilité partagée).

## Résultats clés

| Indicateur | Valeur |
|---|---|
| Mesures de l'annexe A applicables | 92 / 93 |
| Taux de conformité annexe A | 5,4 % |
| Maturité moyenne annexe A | 1,0 / 5 |
| Maturité moyenne clauses 4-10 | 0,7 / 5 |
| Mesures en priorité P1 | 42 |
| Textes applicables / non conformes | 10 / 6 |

**Les 5 constats majeurs :**

1. **HDS : non-conformité critique.** MediSoft administre la plateforme qui héberge les données de santé de ses clients. Elle est donc hébergeur infogéreur (activités 5 et 6), et le certificat HDS d'AWS ne la couvre pas. Son certificat v1.1 est obsolète depuis le 16/05/2026, date limite de passage au référentiel v2.0.
2. **Pas de système de management.** Pas de RSSI, pas de DPO, pas de PSSI, aucun indicateur, aucun audit. Les clauses 9 et 10 sont à 0.
3. **DORA s'applique indirectement.** Trois clients sont des assureurs santé soumis à DORA : ils doivent imposer à MediSoft des clauses (audit, PCA testé, réversibilité, notification des incidents). Aujourd'hui, MediSoft ne pourrait pas y répondre.
4. **NIS2 est à anticiper.** La loi française n'est pas encore promulguée (examen à l'Assemblée nationale à partir du 9 novembre 2026), mais MediSoft sera probablement entité importante. Ses clients du secteur santé lui imposeront de toute façon des exigences de sécurité de la chaîne d'approvisionnement.
5. **Le CRA est déjà en vigueur pour l'appli mobile.** L'obligation de signaler les vulnérabilités activement exploitées s'applique depuis le 11/09/2026.

## Suite du projet

| Module | Missions d'offres de stage couvertes |
|---|---|
| M2 — Gouvernance documentaire | PSSI, politiques, procédures, processus de dérogation |
| M3 — Accès et habilitations | Matrice des rôles, revue des accès, arrivées et départs |
| M4 — Sécurité des projets | Check-lists projet, évaluation d'un outil SaaS, cahier des charges de pentest |
| M5 — Incidents et sensibilisation | Qualification du phishing, playbooks, guide de bonnes pratiques |
| M6 — Pilotage et audit | Tableau de bord KPI, suivi du plan d'action, dossier de preuves |

## Points clés à savoir expliquer

- **Pourquoi l'ISO 27001 ?** C'est le socle du référentiel HDS v2.0, elle couvre l'essentiel de l'article 21 de NIS2, et deux clients l'exigent. Un seul système de management répond donc à trois obligations.
- **Clauses 4 à 10 et annexe A :** les clauses décrivent le système de management, l'annexe A liste les mesures. On peut avoir de bonnes mesures techniques et échouer à l'audit faute de système de management.
- **Une mesure exclue doit être justifiée dans la SoA.** Ici, A.7.6, car il n'y a aucune zone sécurisée sur site.
- **DORA ne s'applique pas directement à MediSoft**, mais à ses clients financiers, qui le lui imposent par contrat (article 30).

---
*Entreprise et données fictives, réalisées dans un but d'apprentissage. Références : ISO/IEC 27001:2022 et amendement 1:2024, référentiel HDS v2.0, directive NIS2, règlements DORA, CRA et EHDS.*
