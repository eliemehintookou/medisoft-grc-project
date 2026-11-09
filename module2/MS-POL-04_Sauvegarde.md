# Politique de sauvegarde et de restauration

| Référence | MS-POL-04 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | Responsable Ops | Approbateur | RSSI |
| Date d'approbation | 01/12/2026 | Prochaine revue | 01/12/2027 |

## 1. Objet et périmètre

Garantir qu'en cas de suppression, de corruption ou de rançongiciel, les données peuvent être restaurées dans les délais promis aux clients.

**Mesures couvertes :** A.8.13, A.8.14, A.5.30. **Obligations :** HDS (activité 6, sauvegarde externalisée), exigences contractuelles DORA des clients assureurs. **Constat EBIOS traité :** n° 7 (sauvegardes jamais testées).

## 2. Objectifs de reprise

| Système | RPO (perte de données maximale) | RTO (durée d'interruption maximale) |
|---|---|---|
| MediSoft Care (base de production) | 1 heure | 4 heures |
| Documents des patients (S3) | 1 heure | 8 heures |
| Code source et configuration (GitHub, Terraform) | 24 heures | 24 heures |
| Outils internes | 24 heures | 72 heures |

## 3. Règles

| Élément | Règle |
|---|---|
| Base de production | Sauvegardes automatiques continues (restauration à la minute près) conservées 35 jours + snapshot quotidien |
| Documents S3 | Versionnage activé + réplication vers une seconde région de l'EEE |
| Copie de sécurité | Copie quotidienne dans un **compte AWS de sauvegarde séparé**, avec verrouillage (AWS Backup Vault Lock) : non supprimable, même par un administrateur, pendant 35 jours |
| Conservation longue | Snapshot mensuel conservé 12 mois |
| Chiffrement | Toutes les sauvegardes sont chiffrées (MS-POL-03) |
| Localisation | Uniquement dans l'EEE (exigence HDS) |
| Accès | Séparé des accès de production ; restauration réservée aux Ops, sur ticket |

C'est l'application de la règle **3-2-1** : trois copies, deux supports ou emplacements, une copie isolée et non modifiable.

## 4. Tests de restauration

- **Trimestriels**, sur un échantillon représentatif (une base complète et un lot de documents), dans un environnement isolé.
- Chaque test mesure le temps réel de restauration et vérifie l'intégrité des données.
- Un procès-verbal est rédigé : date, périmètre, durée, résultat, anomalies, actions.
- Un test raté ouvre une non-conformité suivie par le RSSI.
- **Test annuel du plan de reprise** : restauration complète de MediSoft Care dans une autre zone ; les clients assureurs peuvent y participer (exigence DORA).

## 5. Indicateurs

- Taux de sauvegardes réussies (cible : ≥ 99 %)
- Nombre de tests de restauration réussis par an (cible : 4)
- Écart entre le RTO mesuré et le RTO cible

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/12/2026 | Resp. Ops | Création |
