# Compte rendu de la revue de direction du SMSI — Avril 2027

| Référence | MS-ENR-07-2027-04 | Classification | C2 — Confidentiel |
|---|---|---|---|
| Date | 15/04/2027 | Président | Directeur général |
| Participants | DG, RSSI, DPO, CTO, Resp. Ops, DRH, DAF, Directeur commercial | Rédacteur | RSSI |

> La revue de direction (ISO 27001 clause 9.3) est le moment où la direction examine l'ensemble du SMSI et prend des décisions. La norme impose les éléments à examiner (entrées, 9.3.2) et ce qui doit en sortir (décisions, 9.3.3). Ce compte rendu en est la preuve pour l'auditeur.

---

## Partie 1 — Éléments examinés (clause 9.3.2)

### a) Suite donnée aux décisions précédentes

Première revue de direction. Les décisions du comité sécurité de janvier 2027 ont été mises en œuvre : nomination du RSSI et du DPO, budget sécurité voté, publication de la PSSI.

### b) Évolutions des enjeux externes et internes

| Enjeu | Évolution |
|---|---|
| NIS2 | La loi de transposition a été examinée par l'Assemblée nationale à partir de novembre 2026 ; MediSoft se prépare à être qualifiée d'entité importante |
| HDS | Le certificat v1.1 est obsolète depuis mai 2026 : la certification v2.0 est la priorité absolue |
| Clients assureurs | Les 3 mutuelles ont transmis leurs projets d'avenants DORA |
| Interne | Recrutement de 2 Ops prévu au T2 ; projet d'assistant IA pour le support (scénario B validé) |

### c) Évolutions des besoins et attentes des parties intéressées

Deux grands clients exigent désormais un **certificat ISO 27001** au renouvellement de leur contrat (fin 2027). Les établissements demandent des preuves de traçabilité des accès aux dossiers de leurs patients.

### d) Performance de la sécurité

| Élément | Résultat | Tendance |
|---|---|---|
| **Indicateurs** | 7 atteints, 9 en progrès, 2 en retard (postes gérés par le MDM ; délais de correction des vulnérabilités) | ↗ 16 indicateurs sur 18 en amélioration ou atteints |
| **Maturité ISO 27001** | Annexe A : de 1,2 à 1,9 sur 5 (moyenne des thèmes) ; clauses 4 à 10 : de 0,7 à 1,8 | ↗ forte progression, surtout documentaire |
| **Plan d'action** | Avancement global de 66 % ; 5 chantiers P1 en retard sur l'échéance du 31/03 | Ambition du T1 trop forte : échéances à recaler |
| **Audit interne** | 2 non-conformités majeures, 5 mineures, 2 observations (MS-ENR-06) | Premier audit |
| **Non-conformités** | 2 mineures closes ; 7 écarts en cours de traitement | — |
| **Objectifs de la PSSI** | O1 (MFA) atteint ; O2 (chiffrement) à 92 % ; O3 (formation) à 64 % ; O4 (vulnérabilités) à 72 % ; O5 (restaurations) 1 sur 4 | En ligne, sauf O4 |

### e) Retours des parties intéressées

Un client a signalé que son nom avait été usurpé dans un message de phishing visant MediSoft (signalement S-03) : il a apprécié d'avoir été prévenu rapidement. Les auditeurs internes soulignent l'implication de la direction.

### f) Résultats de l'appréciation des risques et état du plan de traitement

L'analyse EBIOS RM de novembre 2026 reste valable. Deux évolutions :

- le risque « **accès illégitime par un compte non désactivé** » est passé de *probable* à *peu probable* grâce à la revue des accès et au processus de départ corrigé ;
- un **nouveau risque** est ajouté : « **fuite de données de santé via un outil d'IA externe** », traité par la politique de classification (interdiction) et l'évaluation des outils (MS-ENR-02).

Risques résiduels présentés pour acceptation : voir décision D6.

### g) Opportunités d'amélioration

Automatisation de la collecte des indicateurs ; synchronisation SIRH → Entra ID ; mutualisation des preuves ISO 27001, HDS et NIS2 dans un seul référentiel de contrôles.

---

## Partie 2 — Décisions (clause 9.3.3)

| N° | Décision | Responsable | Échéance |
|---|---|---|---|
| D1 | **Audit de certification HDS v2.0 maintenu en juin 2027**, à condition que les 2 non-conformités majeures soient levées et vérifiées par un audit de suivi fin mai | RSSI | 30/06/2027 |
| D2 | **Test complet du PRA** le 20/05/2027, en invitant un client assureur (exigence DORA) | Resp. Ops | 20/05/2027 |
| D3 | **Gel des nouvelles fonctionnalités de l'API mobile** jusqu'à la mise en place de la journalisation des accès aux dossiers patients | CTO | 30/04/2027 |
| D4 | **Créneau hebdomadaire de correction des vulnérabilités**, prioritaire sur les évolutions | CTO | Immédiat |
| D5 | **Budget complémentaire** : test d'intrusion PASSI (mai) et automatisation des indicateurs | DAF | 30/04/2027 |
| D6 | **Acceptation des risques résiduels** de la SoA présentés par le RSSI, à l'exception de ceux liés à la continuité, qui seront réexaminés après le test du PRA | DG | 15/04/2027 |
| D7 | **Recalage des échéances** des 5 chantiers P1 en retard au 30/06/2027 | RSSI | 30/04/2027 |
| D8 | **Certification ISO 27001** visée au T4 2027, pour répondre aux exigences des 2 grands clients | DG | 31/12/2027 |
| D9 | Réponse aux avenants DORA des mutuelles : signature, en annonçant les dates de réalisation du plan de sortie et du test du PRA (MS-MOD-03 partie 3) | Juridique + RSSI | 31/05/2027 |
| D10 | Mise à jour de la PSSI : objectif O4 maintenu ; ajout d'un objectif sur la journalisation (100 % des accès aux données de santé tracés) | RSSI | 31/05/2027 |

**Ressources :** recrutement de 2 Ops confirmé ; temps du RSSI à 100 % sur la sécurité.

**Prochaine revue de direction :** octobre 2027.

---

| Approuvé par | Date |
|---|---|
| Directeur général | 15/04/2027 |
