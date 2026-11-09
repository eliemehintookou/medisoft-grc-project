# Clauses de sécurité types pour les contrats

| Référence | MS-MOD-03 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | Responsable juridique | Approbateur | RSSI + DPO |
| Date d'approbation | 15/01/2027 | Prochaine revue | 15/01/2028 |

> Modèle à adapter par le service juridique. Il couvre deux situations : MediSoft **cliente** de ses fournisseurs (partie 1 et 2), et MediSoft **fournisseur** de clients soumis à DORA (partie 3).

---

## Partie 1 — Clauses minimales selon la criticité du fournisseur

| N° | Clause | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|---|
| C1 | Confidentialité, y compris après la fin du contrat | ✔ | ✔ | ✔ |
| C2 | Contrat de sous-traitance RGPD (art. 28) si données personnelles | ✔ | ✔ | ✔ |
| C3 | Respect de la PSSI de MediSoft pour les personnes intervenant sur son SI | ✔ | ✔ | |
| C4 | Mesures de sécurité minimales (chiffrement, MFA, journalisation, correctifs) | ✔ | ✔ | |
| C5 | Localisation des données dans l'EEE ; information préalable de tout changement | ✔ | ✔ | |
| C6 | Liste des sous-traitants ultérieurs ; accord préalable de MediSoft pour tout ajout | ✔ | ✔ | |
| C7 | Notification des incidents de sécurité | 24 h | 48 h | 72 h |
| C8 | Droit d'audit (sur pièces et sur site) ou rapport d'audit indépendant annuel | ✔ | Sur pièces | |
| C9 | Engagement de niveau de service (disponibilité, délais) | ✔ | ✔ | |
| C10 | Plan de continuité testé | ✔ | | |
| C11 | Réversibilité : restitution des données dans un format standard puis suppression attestée | ✔ | ✔ | ✔ |
| C12 | Certification HDS si données de santé | ✔ | | |
| C13 | Interdiction d'utiliser les données de MediSoft pour entraîner des modèles d'IA | ✔ | ✔ | ✔ |
| C14 | Assurance responsabilité civile professionnelle et cyber | ✔ | ✔ | |
| C15 | Participation aux tests de continuité de MediSoft si nécessaire | ✔ | | |

## Partie 2 — Rédaction type

**C7 — Notification des incidents.** « Le Prestataire notifie à MediSoft, à l'adresse securite@medisoft.example, tout incident de sécurité affectant ou susceptible d'affecter les données ou les services de MediSoft, dans un délai maximal de vingt-quatre (24) heures après en avoir eu connaissance. La notification précise la nature de l'incident, les données et services concernés, les mesures prises et un point de contact. Le Prestataire fournit un rapport complet sous dix (10) jours ouvrés. »

> Pourquoi 24 h : MediSoft doit elle-même prévenir ses clients responsables de traitement « dans les meilleurs délais » (RGPD art. 33.2), ses clients assureurs (DORA) et, le cas échéant, l'ANSSI sous 24 h (NIS2). Un fournisseur qui notifie sous 72 h rend ces engagements impossibles à tenir.

**C8 — Droit d'audit.** « MediSoft, ou un auditeur indépendant mandaté par elle et tenu au secret, peut vérifier le respect des présentes obligations, une fois par an et en cas d'incident significatif, avec un préavis de quinze (15) jours ouvrés (sans préavis en cas d'incident). À défaut d'audit sur site, le Prestataire remet annuellement un rapport d'audit indépendant (ISO 27001, SOC 2 Type II) couvrant les services fournis. »

**C11 — Réversibilité.** « À la fin du contrat, quelle qu'en soit la cause, le Prestataire restitue à MediSoft l'intégralité de ses données dans un format standard et documenté, dans un délai de trente (30) jours, puis procède à leur suppression définitive, y compris dans ses sauvegardes, et en remet une attestation écrite. Le Prestataire assure la continuité du service pendant une période de transition de trois (3) mois au moins. »

**C13 — Intelligence artificielle.** « Le Prestataire s'interdit d'utiliser les données de MediSoft, y compris sous forme anonymisée ou agrégée, pour entraîner, améliorer ou évaluer des modèles d'intelligence artificielle, les siens ou ceux de tiers. »

**Développement externalisé (A.8.30, avenant pour Studio Kappa).** « Le Prestataire respecte la politique de développement sécurisé de MediSoft (MS-POL-06). Le code est livré exclusivement dans les dépôts de MediSoft et soumis à ses contrôles automatiques et à sa revue de code. Le Prestataire signale toute vulnérabilité découverte sous 24 h, n'utilise aucune donnée réelle de patient, et cède à MediSoft les droits sur le code livré, y compris la liste des composants tiers utilisés (SBOM). »

---

## Partie 3 — Annexe DORA pour les contrats avec les clients assureurs

Les mutuelles et assureurs clients de MediSoft sont des entités financières soumises à DORA. L'article 30 leur impose d'inclure certaines dispositions dans leurs contrats avec leurs prestataires de services TIC. Le module tiers payant soutenant une **fonction importante** de ces clients, les exigences renforcées de l'article 30.3 s'appliquent aussi.

Le tableau sert de grille pour négocier l'avenant et vérifier que MediSoft peut tenir ses engagements.

| Exigence DORA | Article | Engagement proposé par MediSoft | MediSoft peut-elle le tenir aujourd'hui ? |
|---|---|---|---|
| Description claire des services et conditions de sous-traitance | 30.2.a | Annexe de description du service ; liste des sous-traitants (AWS, NuageOps) | Oui |
| Lieux de prestation et de traitement des données ; information préalable des changements | 30.2.b | Données en France (AWS Paris), réplication dans l'EEE ; préavis de 3 mois | Oui |
| Disponibilité, authenticité, intégrité, confidentialité, protection des données personnelles | 30.2.c | Référence au plan d'assurance sécurité et au DPA | Partiellement : PSSI publiée, mesures en cours (module 1) |
| Accès, récupération et restitution des données (fin de contrat, insolvabilité…) | 30.2.d | Export complet sous 30 jours ; plan de réversibilité | Non : plan de sortie à rédiger (registre F01) |
| Niveaux de service | 30.2.e | Disponibilité 99,8 % ; RTO 4 h ; RPO 1 h | Partiellement : RTO non encore testé |
| Assistance en cas d'incident TIC, sans surcoût ou à coût prédéfini | 30.2.f | Assistance incluse ; notification sous 4 h pour un incident majeur | Partiellement : procédure d'incident en cours (module 5) |
| Coopération avec les autorités compétentes | 30.2.g | Coopération pleine avec l'ACPR et les autorités désignées | Oui |
| Droits de résiliation et préavis minimum | 30.2.h | Selon le contrat cadre | Oui |
| Participation aux programmes de sensibilisation et formations du client | 30.2.i | Participation sur demande | Oui |
| Objectifs de performance quantitatifs et qualitatifs précis | 30.3.a | Indicateurs mensuels transmis au client | Partiellement : tableau de bord en construction (module 6) |
| Préavis et obligations de reporting | 30.3.b | Rapport trimestriel de service et de sécurité | Partiellement |
| Plans de continuité mis en œuvre et testés ; mesures de sécurité TIC | 30.3.c | Test annuel du PRA, auquel le client peut assister | Non : premier test prévu en 2027 (MS-POL-04) |
| Participation aux tests de pénétration fondés sur la menace (TLPT) du client | 30.3.d | Coopération pleine | Oui (engagement de principe) |
| Droits illimités d'accès, d'inspection et d'audit | 30.3.e | Audit sur site ou sur pièces, une fois par an et en cas d'incident | Oui, mais **dépend des fournisseurs de MediSoft** : les grands fournisseurs cloud comme AWS n'ouvrent en général pas leurs datacenters aux audits de clients et fournissent des rapports d'audit indépendants à la place : à vérifier dans les conditions contractuelles d'AWS |
| Stratégie de sortie avec période de transition | 30.3.f | Transition de 6 mois ; réversibilité documentée | Non : plan à rédiger |

**Conclusion pour la direction :** MediSoft peut signer l'avenant DORA, mais **3 engagements ne sont pas tenables aujourd'hui** : plan de sortie, PRA testé et objectifs de performance mesurés. Ils sont inscrits au plan d'action (PA-12, PA-13, PA-17) avec une échéance au T2 2027, qu'il faut annoncer aux clients plutôt que de signer des engagements non tenus.

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 15/01/2027 | Juridique + RSSI | Création |
