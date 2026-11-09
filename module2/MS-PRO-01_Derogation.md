# Procédure de gestion des dérogations de sécurité

| Référence | MS-PRO-01 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité |
| Date d'approbation | 01/12/2026 | Prochaine revue | 01/12/2027 |

## 1. Objet

Une règle de sécurité ne peut pas toujours être appliquée immédiatement : contrainte technique, exigence d'un client, système ancien en cours de remplacement. Cette procédure permet de **traiter ces situations de façon encadrée** plutôt que de laisser la règle contournée en silence.

Une dérogation n'est **pas** une autorisation définitive : c'est l'acceptation temporaire d'un risque connu, maîtrisé par des mesures compensatoires et suivi jusqu'à sa fin.

## 2. Principes

1. Toute non-application d'une règle de la PSSI ou d'une politique doit être couverte par une dérogation approuvée.
2. Une dérogation est **limitée dans le temps** : 6 mois maximum, renouvelable une fois. Au-delà, il faut soit corriger, soit modifier la politique.
3. Elle s'accompagne de **mesures compensatoires** qui réduisent le risque.
4. Elle comporte un **plan de retour à la conformité** avec une date.
5. Elle est inscrite au **registre des dérogations**.
6. Certaines règles **ne peuvent faire l'objet d'aucune dérogation** :
   - stockage de données de santé hors de l'EEE ou chez un hébergeur non certifié HDS ;
   - envoi de données de santé par e-mail non chiffré ;
   - utilisation de données réelles de patients hors production ;
   - compte à privilèges sans MFA exposé sur Internet.

## 3. Processus

| Étape | Acteur | Action | Délai |
|---|---|---|---|
| 1. Demande | Demandeur (avec son manager) | Remplit le formulaire (section 5) : règle concernée, motif, périmètre, durée, mesures compensatoires proposées | — |
| 2. Recevabilité | RSSI | Vérifie que la règle peut faire l'objet d'une dérogation et que le dossier est complet | 2 jours ouvrés |
| 3. Analyse de risque | RSSI (avec le DPO si des données personnelles sont concernées) | Évalue la vraisemblance et la gravité, avec les mêmes échelles que l'EBIOS RM ; détermine le risque résiduel après mesures compensatoires | 5 jours ouvrés |
| 4. Décision | Selon le niveau de risque (section 4) | Accord, accord sous conditions, ou refus motivé | 5 jours ouvrés |
| 5. Enregistrement | RSSI | Inscription au registre, communication de la décision | 1 jour |
| 6. Suivi | RSSI | Vérifie la mise en place des mesures compensatoires ; relance 30 jours avant l'échéance | Continu |
| 7. Clôture | RSSI | Constate le retour à la conformité, ou instruit un renouvellement | À l'échéance |

## 4. Niveaux d'approbation

| Risque résiduel | Qui approuve | Durée maximale |
|---|---|---|
| Faible | RSSI | 6 mois |
| Modéré | RSSI + propriétaire du risque (CTO ou Resp. Ops) | 6 mois |
| Élevé | Directeur général, après avis du comité sécurité | 3 mois |
| Critique | **Refus** : la situation doit être corrigée | — |

Le comité sécurité examine chaque trimestre l'ensemble des dérogations ouvertes.

## 5. Formulaire de demande

| Champ | À remplir |
|---|---|
| N° de dérogation | DER-AAAA-NNN (attribué par le RSSI) |
| Demandeur / service | |
| Règle concernée | Référence du document et article (ex. MS-POL-03 §2) |
| Description de la situation | Qu'est-ce qui ne respecte pas la règle ? |
| Motif | Pourquoi la règle ne peut-elle pas être appliquée maintenant ? |
| Périmètre | Systèmes, données (niveau de classification), utilisateurs concernés |
| Durée demandée | Date de début et date de fin |
| Mesures compensatoires | Ce qui réduit le risque pendant la dérogation |
| Plan de retour à la conformité | Actions, responsable, date |
| Analyse de risque (RSSI) | Vraisemblance, gravité, risque résiduel |
| Avis du DPO | Si des données personnelles sont concernées |
| Décision | Accord / accord sous conditions / refus, date, signature |

## 6. Exemple : DER-2026-001

| Champ | Contenu |
|---|---|
| Demandeur | Responsable Ops, à la demande du service commercial |
| Règle concernée | MS-POL-03 §2 : échanges de fichiers avec les clients par SFTP avec authentification par clé ; MS-POL-02 §4 : pas de mot de passe statique |
| Situation | Une mutuelle cliente transmet chaque nuit un fichier de remboursements (données C3) par SFTP. Son système, en cours de remplacement, ne sait s'authentifier que par **mot de passe**, pas par clé SSH |
| Motif | Le nouveau système du client sera en service le 30/04/2027 ; couper le flux bloquerait le tiers payant de ses adhérents |
| Périmètre | Un compte SFTP dédié, un seul flux, dépôt dans un répertoire isolé |
| Durée demandée | Du 01/12/2026 au 31/05/2027 |
| Mesures compensatoires | Accès SFTP filtré sur les **2 adresses IP** du client ; mot de passe de 32 caractères aléatoires, stocké dans le gestionnaire de secrets et changé tous les mois ; compte limité au dépôt (pas de lecture ni d'exécution) ; fichiers chiffrés en PGP par le client avant envoi ; alerte en cas de connexion hors plage horaire ou d'échecs répétés |
| Plan de retour | Passage à l'authentification par clé dès la mise en service du nouveau système du client ; jalon de suivi au 31/03/2027 |
| Analyse de risque | Vraisemblance : faible (filtrage IP, mot de passe fort) · Gravité : importante (données de santé) · **Risque résiduel : modéré** |
| Avis du DPO | Favorable, sous réserve du chiffrement PGP des fichiers |
| Décision | **Accordée sous conditions** par le RSSI et le Resp. Ops (propriétaire du risque), le 01/12/2026, jusqu'au 31/05/2027 |

## 7. Registre des dérogations

| N° | Règle | Objet | Risque résiduel | Approbateur | Début | Échéance | Statut |
|---|---|---|---|---|---|---|---|
| DER-2026-001 | MS-POL-03 §2 / MS-POL-02 §4 | SFTP par mot de passe pour une mutuelle | Modéré | RSSI + Resp. Ops | 01/12/2026 | 31/05/2027 | En cours |
| DER-2026-002 | MS-POL-08 §2 (USB bloqué) | Clé USB chiffrée pour le transfert de pilotes vers un équipement d'un client sans réseau | Faible | RSSI | 05/12/2026 | 05/03/2027 | En cours |
| DER-2026-003 | MS-POL-05 §3 (ports d'administration fermés) | SSH ouvert sur Internet pour un bastion « pratique » | Élevé avant mesures, aucune mesure compensatoire suffisante | — | — | — | **Refusée** : migration vers Session Manager imposée sous 15 jours |

## 8. Indicateurs

- Nombre de dérogations ouvertes et leur répartition par niveau de risque
- Dérogations échues non clôturées (cible : 0)
- Dérogations renouvelées plus d'une fois (cible : 0)

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/12/2026 | RSSI | Création |
