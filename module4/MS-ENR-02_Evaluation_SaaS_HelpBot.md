# Fiche d'évaluation sécurité — HelpBot AI

| Référence | MS-ENR-02-2027-01 | Classification | C2 — Confidentiel |
|---|---|---|---|
| Date | 19/01/2027 | Évaluateurs | RSSI, DPO |
| Demandeur | Responsable Support | Criticité | Tier 1 — Critique (données de santé) |

## 1. Contexte de la demande

Le support veut adopter **HelpBot AI** (éditeur fictif), un service SaaS d'intelligence artificielle, pour deux usages :

- **Scénario A** : résumer automatiquement les tickets du support niveau 2 et proposer des réponses. Ces tickets contiennent régulièrement des **extraits de dossiers patients** envoyés par les établissements.
- **Scénario B** : un chatbot sur le site public de MediSoft, qui répond aux questions fréquentes des prospects et utilisateurs (fonctionnalités, tarifs, documentation). **Aucune donnée de santé.**

Gain attendu : environ 20 % de temps en moins sur le traitement des tickets.

## 2. Méthode

Questionnaire de 24 questions réparties en 6 domaines, chaque question ayant un poids de 1 à 3 et une note de 0 à 2. Les réponses s'appuient sur la documentation de l'éditeur, son rapport SOC 2 et un entretien avec son responsable sécurité. Le détail figure dans l'onglet `2_Evaluation_HelpBot` du registre des fournisseurs.

## 3. Résultats

| | Scénario A — tickets N2 | Scénario B — chatbot FAQ public |
|---|---|---|
| Score pondéré | **63,8 %** | **68,2 %** |
| Exigences bloquantes non satisfaites | **1** (certification HDS) | 0 |
| **Avis** | **Défavorable** | **Favorable sous conditions** |

### Points forts

- Rapport SOC 2 Type II récent ; test d'intrusion annuel par un tiers
- Données stockées dans l'EEE (Irlande), chiffrées au repos et en transit
- Contrat de sous-traitance RGPD disponible ; liste des sous-traitants publiée
- Journaux d'audit exportables ; réversibilité par export complet

### Points faibles

| Point faible | Pourquoi c'est un problème |
|---|---|
| **Pas de certification HDS** | Héberger des données de santé pour le compte de tiers sans certification HDS est illégal (CSP art. L.1111-8). **Bloquant pour le scénario A** |
| Modèle d'IA fourni par un sous-traitant américain ; support de nuit depuis les États-Unis | Risque d'accès depuis un pays hors EEE, à documenter pour HDS et à évaluer pour le RGPD |
| Non-utilisation des données pour l'entraînement des modèles **seulement sur l'offre Enterprise** | Sur l'offre standard, les données de MediSoft pourraient améliorer le modèle |
| Masquage partiel : les informations médicales ne sont pas masquées | Un patient pourrait être identifié à partir du contenu d'un ticket |
| Notification d'incident sous 72 h | Incompatible avec les engagements de MediSoft (24 h, clause C7) |
| Pas de tests spécifiques d'injection de prompt | Un chatbot public peut être manipulé pour divulguer des informations ou tenir des propos inappropriés au nom de MediSoft |
| Pas d'audit sur site ; plan de continuité non communiqué | Engagements DORA de MediSoft difficiles à répercuter |

## 4. Décision

**Scénario A — Refusé.** Aucun ticket contenant des données de santé ne doit être transmis à HelpBot AI. La décision sera réexaminée si l'éditeur obtient la certification HDS. Alternative étudiée : une solution d'IA hébergée chez un hébergeur certifié HDS ou déployée dans l'infrastructure AWS de MediSoft.

**Scénario B — Accepté sous conditions :**

1. Souscription de l'**offre Enterprise** (SSO avec MFA, non-utilisation des données pour l'entraînement inscrite au contrat)
2. Signature du contrat de sous-traitance RGPD et des clauses MS-MOD-03 : notification sous 24 h, interdiction d'usage pour l'IA (C13), réversibilité
3. Base de connaissances du chatbot limitée à la **documentation publique** ; aucun raccordement aux tickets ni à MediSoft Care
4. Message d'avertissement sur le chatbot : ne pas saisir de données de santé ; détection et blocage des numéros de sécurité sociale et des termes médicaux
5. Tests d'injection de prompt réalisés par MediSoft avant l'ouverture au public
6. Revue après 3 mois d'utilisation (étape 5 de la check-list projet)

**Risque résiduel accepté par :** Responsable Support (propriétaire du risque), après avis du RSSI et du DPO.

## 5. Suivi

| Action | Responsable | Échéance |
|---|---|---|
| Négociation de l'offre Enterprise et des clauses | Juridique | 15/02/2027 |
| Tests d'injection de prompt | RSSI | 28/02/2027 |
| Mise en service du chatbot | Resp. Support | 15/03/2027 |
| Revue à 3 mois | RSSI | 15/06/2027 |
| Suivi de la certification HDS de l'éditeur | RSSI | Revue annuelle |
