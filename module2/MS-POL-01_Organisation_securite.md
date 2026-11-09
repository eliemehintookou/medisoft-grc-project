# Organisation de la sécurité et matrice RACI

| Référence | MS-POL-01 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Directeur général |
| Date d'approbation | 01/12/2026 | Prochaine revue | 01/12/2027 |

## 1. Objet

Définir qui fait quoi en matière de sécurité, comment les décisions sont prises et comment elles remontent à la direction (ISO 27001 clause 5.3, mesures A.5.2, A.5.3 et A.5.4).

## 2. Rôles et responsabilités

| Rôle | Responsabilités principales |
|---|---|
| **Directeur général (DG)** | Responsable en dernier ressort. Approuve la PSSI, le budget sécurité et les risques résiduels élevés. Préside le comité sécurité et la revue de direction. Suit la formation des dirigeants (NIS2 art. 20) |
| **RSSI** | Pilote le SMSI, rédige et maintient la documentation, conduit l'analyse de risques, suit le plan d'action, coordonne la gestion des incidents, instruit les dérogations, produit le tableau de bord. Rattaché au DG, indépendant de la DSI et de la R&D |
| **DPO** | Conseille et contrôle le respect du RGPD, tient le registre des traitements, aide les clients pour leurs analyses d'impact (AIPD), est le point de contact de la CNIL. Désigné auprès de la CNIL |
| **CTO** | Applique la sécurité dans le développement (cycle de développement sécurisé, revue de code, tests). Propriétaire des risques liés au produit |
| **Responsable Ops** | Applique la sécurité de l'infrastructure AWS : accès, chiffrement, sauvegardes, journalisation, correctifs. Propriétaire des risques liés à l'hébergement |
| **DRH** | Intègre la sécurité aux processus RH : clauses des contrats, arrivées et départs, sensibilisation, procédure disciplinaire |
| **Responsable juridique** | Clauses de sécurité des contrats fournisseurs et clients (RGPD, DORA, HDS) |
| **Managers** | Valident les demandes d'accès et participent à la revue des accès de leur équipe |
| **Collaborateurs** | Appliquent la charte informatique, suivent les formations, signalent tout incident |

**Séparation des tâches** (A.5.3) : la personne qui demande un accès ne peut pas l'approuver ; celle qui développe un changement ne peut pas l'approuver seule pour la production ; le RSSI qui instruit une dérogation ne l'approuve pas seul lorsque le risque est élevé.

## 3. Instances de gouvernance

| Instance | Participants | Fréquence | Rôle |
|---|---|---|---|
| **Comité sécurité** | DG (président), RSSI, DPO, CTO, Resp. Ops, DRH | Trimestriel | Suivi du plan d'action et des indicateurs, décisions budgétaires, validation des documents, arbitrage des dérogations à risque élevé |
| **Revue de direction** | DG, RSSI, DPO, comité de direction | Annuelle | Revue complète du SMSI (clause 9.3) : résultats d'audit, incidents, objectifs, besoins de changement |
| **Point sécurité opérationnel** | RSSI, Resp. Ops, CTO | Mensuel | Vulnérabilités, alertes, incidents, changements à risque |
| **Cellule de crise** | DG, RSSI, DPO, CTO, Resp. Ops, communication | Sur incident majeur | Pilotage de la crise et des notifications (module 5) |

Chaque réunion fait l'objet d'un compte rendu conservé comme preuve d'audit.

## 4. Matrice RACI

**R** = réalise · **A** = approuve et rend des comptes · **C** = consulté · **I** = informé

| Activité | DG | RSSI | DPO | CTO | Ops | DRH | Jur. | Managers |
|---|---|---|---|---|---|---|---|---|
| Approuver la PSSI | A | R | C | C | C | C | C | I |
| Rédiger et maintenir les politiques | I | A/R | C | C | C | C | C | I |
| Analyse de risques EBIOS RM | A | R | C | C | C | I | I | I |
| Accepter les risques résiduels élevés | A | R | C | C | C | | | |
| Tenir le registre des obligations | I | A/R | R | | | | C | |
| Registre des traitements RGPD | I | C | A/R | C | C | C | C | |
| Accorder un accès | | C | | | R | | | A |
| Revue des accès | I | A | | C | R | | | R |
| Chiffrement et gestion des clés | | A | C | C | R | | | |
| Sauvegardes et tests de restauration | | A | | | R | | | |
| Cycle de développement sécurisé | | C | | A/R | C | | | |
| Gestion des vulnérabilités | | A | | R | R | | | |
| Gestion d'un incident | I | A/R | C | R | R | I | C | I |
| Notification CNIL / ANSSI / clients | A | R | R | | | | C | |
| Évaluation des fournisseurs | I | A/R | C | C | C | | C | |
| Clauses sécurité des contrats | A | C | C | | | | R | |
| Sensibilisation et formation | I | A | C | | | R | | I |
| Arrivées et départs (accès) | | C | | | R | A | | R |
| Dérogation (risque faible ou modéré) | I | A | C | C | C | | | R |
| Dérogation (risque élevé) | A | R | C | C | C | | | C |
| Audit interne | I | A | C | C | C | | | |
| Tableau de bord sécurité | I | A/R | C | C | C | | | |

## 5. Contacts avec les autorités et les communautés

Le RSSI tient à jour l'annuaire des contacts (A.5.5 et A.5.6) : CNIL, ANSSI / CERT-FR, CERT Santé (ANS), ARS, police ou gendarmerie (dépôt de plainte), assureur cyber, CLUSIF ou CESIN.

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/12/2026 | RSSI | Création |
