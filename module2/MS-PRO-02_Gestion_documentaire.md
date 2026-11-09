# Procédure de gestion documentaire du SMSI

| Référence | MS-PRO-02 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité |
| Date d'approbation | 01/12/2026 | Prochaine revue | 01/12/2027 |

## 1. Objet

Garantir que chaque document de sécurité est à jour, validé, accessible aux bonnes personnes et traçable (ISO 27001 clause 7.5, mesure A.5.37). Lors d'un audit, c'est cette procédure qui permet de prouver que la version présentée est bien la version en vigueur.

## 2. Structure documentaire

| Niveau | Type | Contenu | Approbateur | Exemple |
|---|---|---|---|---|
| 1 | Politique générale | Engagements et principes | Directeur général | MS-POL-00 PSSI |
| 2 | Politiques thématiques | Règles par domaine (le « quoi ») | Comité sécurité | MS-POL-02 Contrôle d'accès |
| 3 | Procédures | Étapes et responsabilités (le « qui » et le « comment ») | RSSI | MS-PRO-01 Dérogations |
| 4 | Modes opératoires, modèles | Instructions techniques détaillées | Propriétaire du processus | Mode opératoire de restauration |
| 5 | Enregistrements | Preuves que les règles sont appliquées | — | PV de test, comptes rendus, exports de revue des accès |

## 3. Identification

- Référence unique : `MS-POL-NN` (politique), `MS-PRO-NN` (procédure), `MS-MOP-NN` (mode opératoire), `MS-ENR-NN` (modèle d'enregistrement).
- Chaque document comporte un cartouche : référence, version, classification, statut, propriétaire, approbateur, date d'approbation, date de prochaine revue, et un historique des versions.
- Versions : `0.x` pour un brouillon, `1.0` à la première approbation, `1.1` pour une modification mineure (forme), `2.0` pour une modification de fond.

## 4. Cycle de vie

| Étape | Qui | Règle |
|---|---|---|
| Rédaction | Propriétaire du document | À partir du modèle de document |
| Relecture | Personnes consultées selon la matrice RACI (MS-POL-01) | Commentaires tracés |
| Approbation | Selon le niveau (section 2) | Approbation datée, conservée dans le compte rendu du comité |
| Publication | RSSI | Publié dans l'espace documentaire du SMSI ; l'ancienne version est archivée |
| Diffusion | RSSI + managers | Communication aux personnes concernées ; signature pour la charte |
| Revue | Propriétaire | Au moins une fois par an, et après un incident majeur, un audit ou une évolution réglementaire |
| Archivage | RSSI | Versions obsolètes conservées 5 ans en lecture seule, marquées « Obsolète » |

## 5. Stockage et accès

- Espace documentaire unique du SMSI, avec gestion des versions et des droits.
- Documents C1 : lecture pour tous les collaborateurs ; modification réservée au propriétaire et au RSSI.
- Documents C2 (rapports d'audit, analyse de risques) : accès restreint.
- Aucune copie locale ou imprimée ne fait foi : seule la version publiée est valable.

## 6. Liste des documents en vigueur

| Référence | Titre | Version | Propriétaire | Prochaine revue |
|---|---|---|---|---|
| MS-POL-00 | Politique de sécurité des systèmes d'information | 1.0 | RSSI | 01/12/2027 |
| MS-POL-01 | Organisation de la sécurité et matrice RACI | 1.0 | RSSI | 01/12/2027 |
| MS-POL-02 | Contrôle d'accès et authentification | 1.0 | RSSI | 01/12/2027 |
| MS-POL-03 | Cryptographie et gestion des clés | 1.0 | RSSI | 01/12/2027 |
| MS-POL-04 | Sauvegarde et restauration | 1.0 | Resp. Ops | 01/12/2027 |
| MS-POL-05 | Sécurité du cloud | 1.0 | RSSI | 01/12/2027 |
| MS-POL-06 | Développement sécurisé | 1.0 | CTO | 01/12/2027 |
| MS-POL-07 | Classification, manipulation et conservation | 1.0 | RSSI | 01/12/2027 |
| MS-POL-08 | Postes de travail, mobiles et télétravail | 1.0 | RSSI | 01/12/2027 |
| MS-POL-09 | Charte d'utilisation du SI | 2.0 | RSSI | 01/12/2027 |
| MS-PRO-01 | Gestion des dérogations | 1.0 | RSSI | 01/12/2027 |
| MS-PRO-02 | Gestion documentaire du SMSI | 1.0 | RSSI | 01/12/2027 |

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/12/2026 | RSSI | Création |
