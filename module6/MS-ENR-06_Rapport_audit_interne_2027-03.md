# Rapport d'audit interne — Audit « à blanc » ISO 27001 et HDS v2.0

| Référence | MS-ENR-06-2027-03 | Classification | C2 — Confidentiel |
|---|---|---|---|
| Dates | Du 15 au 19/03/2027 | Auditeurs | Cabinet Audit & Conformité (2 auditeurs) — indépendants des activités auditées |
| Commanditaire | Directeur général | Pilote interne | RSSI |

## 1. Objectifs

1. Vérifier si le SMSI de MediSoft est prêt pour l'**audit de certification HDS v2.0**, qui repose sur l'ISO 27001.
2. Satisfaire l'exigence d'**audit interne** de l'ISO 27001 (clause 9.2).
3. Identifier les non-conformités à corriger avant l'audit de certification.

## 2. Périmètre et méthode

**Périmètre :** celui du SMSI (PSSI §3) : plateforme MediSoft Care, application MediSoft Patient, équipes R&D, Ops et Support, infrastructure AWS.

**Méthode :**
- revue documentaire des 13 politiques et procédures ;
- 14 entretiens : DG, RSSI, DPO, CTO, Resp. Ops, DRH, 2 développeurs, 2 Ops, 2 agents de support, 2 commerciaux ;
- **échantillonnage** pour vérifier l'application réelle des règles : 20 changements en production, 15 départs et arrivées, 10 accès support aux dossiers patients, 25 vulnérabilités critiques, 5 fournisseurs ;
- observations techniques : console AWS, accès conditionnel Entra ID, CI GitHub.

**Classement des écarts :**
- **Non-conformité majeure** : exigence non satisfaite qui remet en cause la capacité du SMSI à atteindre ses objectifs. **Bloque la certification.**
- **Non-conformité mineure** : écart ponctuel qui ne remet pas en cause le système.
- **Observation** : point d'amélioration ou risque de non-conformité future.

## 3. Conclusion générale

> En un trimestre, MediSoft est passée d'une absence totale de dispositif à un **SMSI documenté, piloté et en partie appliqué**. La direction est impliquée, la documentation est complète et cohérente, et la première revue des accès comme le traitement des incidents démontrent que les règles sont **appliquées et pas seulement écrites**.
>
> **En l'état, l'audit de certification échouerait** en raison de 2 non-conformités majeures. Les corriger d'ici fin mai rend l'objectif d'un audit de certification en juin 2027 réaliste.

## 4. Points forts

- **Engagement de la direction** : PSSI signée par le DG, comités sécurité tenus, objectifs mesurables suivis.
- **Revue des accès** exemplaire pour une première : rapprochement automatisé, décisions des managers tracées, causes racines traitées (MS-ENR-01).
- **Gestion des incidents** : 2 incidents découverts, traités et documentés de bout en bout, y compris la justification de non-notification à la CNIL (MS-ENR-05).
- **MFA** sur 100 % des comptes à privilèges ; elle a déjà bloqué une tentative d'intrusion réelle.
- **Évaluation des fournisseurs** rigoureuse, avec une décision nuancée sur l'outil d'IA (MS-ENR-02).

## 5. Écarts constatés

| N° | Type | Exigence | Constat | Preuve observée |
|---|---|---|---|---|
| NC-2027-01 | **Majeure** | A.5.30, HDS | Le plan de reprise d'activité n'a jamais été testé. Le RTO de 4 h annoncé dans la PSSI et aux clients n'est pas démontré | Aucun PV de test de PRA ; seul un test de restauration de base existe |
| NC-2027-02 | **Majeure** | A.8.15, HDS | Sur 10 accès de test aux dossiers patients via l'**API mobile**, aucun n'apparaît dans le journal des accès. La traçabilité exigée pour les données de santé n'est pas assurée | Test réalisé par les auditeurs avec un compte de démonstration |
| NC-2027-03 | Mineure | A.8.8 | 18 vulnérabilités critiques sur 25 corrigées en moins de 7 jours (72 %) ; cible de la politique : 90 % | Rapports du scanner de février et mars |
| NC-2027-04 | Mineure | A.5.9 | L'inventaire des actifs n'inclut pas les outils SaaS | Inventaire du 01/03/2027 |
| NC-2027-05 | Mineure | Cl. 7.2 | La matrice de compétences ne couvre pas l'équipe Ops ni le prestataire Ops | Matrice du 15/02/2027 |
| NC-2027-06 | Mineure | Cl. 7.5 | 2 documents publiés sans date d'approbation | Espace documentaire du SMSI |
| NC-2027-07 | Mineure | A.8.32 | 2 changements en production sur 20 sans ticket d'approbation (correctifs de nuit) | Historique des déploiements |
| OBS-2027-01 | Observation | MS-PRO-01 | L'instruction de la dérogation DER-2026-004 dure depuis plus de 2 mois | Registre des dérogations |
| OBS-2027-02 | Observation | Cl. 9.1 | Les indicateurs sont collectés à la main, avec un risque d'erreur | Tableau de bord |

**Bilan : 2 non-conformités majeures, 5 mineures, 2 observations.** Les actions correctives sont suivies dans l'onglet `5_Non_conformites` du tableau de bord.

## 6. Ce que disent les échantillons

| Échantillon | Résultat | Commentaire |
|---|---|---|
| 15 arrivées et départs | 15 / 15 conformes | Le processus corrigé après la revue des accès fonctionne |
| 10 accès du support aux dossiers patients | 10 / 10 avec ticket et accord du client | Mais 0 / 10 journalisés lorsque l'accès passe par l'API mobile (NC-2027-02) |
| 20 changements en production | 18 / 20 avec ticket | NC-2027-07 |
| 25 vulnérabilités critiques | 18 / 25 corrigées dans les délais | NC-2027-03 |
| 5 fournisseurs Tier 1 | 5 / 5 évalués ; 2 / 5 avec un plan de sortie | Point déjà identifié au plan d'action (PA-13) |

## 7. Programme d'audit interne 2027

| Audit | Périmètre | Date | Auditeur |
|---|---|---|---|
| Audit à blanc ISO 27001 / HDS (ce rapport) | Ensemble du SMSI | Mars 2027 | Cabinet externe |
| Audit de suivi des non-conformités majeures | NC-2027-01 et 02 | Juin 2027, avant la certification | RSSI |
| Audit thématique : fournisseurs et continuité | A.5.19 à A.5.23, A.5.29, A.5.30 | Septembre 2027 | Cabinet externe |
| Audit thématique : développement sécurisé | A.8.25 à A.8.33 | Novembre 2027 | Cabinet externe |

Sur un cycle de 3 ans, l'ensemble des clauses et des mesures applicables sera audité au moins une fois.

---

| Rapport validé par | Date |
|---|---|
| Responsable de l'audit (Cabinet Audit & Conformité) | 26/03/2027 |
| RSSI (réception) | 26/03/2027 |
