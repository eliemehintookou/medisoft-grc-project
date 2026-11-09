# Procès-verbal de la revue des accès — 4e trimestre 2026

| Référence | MS-ENR-01-2026T4 | Classification | C2 — Confidentiel |
|---|---|---|---|
| Date de la revue | 15/12/2026 | Point de suivi | 29/12/2026 |
| Animateur | RSSI | Référentiel | MS-POL-02 §7, matrice des rôles v1.0 |

## 1. Participants

RSSI (animation), Responsable Ops, CTO, DRH, managers Support, Commercial, R&D, Finance et Juridique. Le DPO a été consulté sur les anomalies impliquant des données de santé (F-004, F-006).

## 2. Périmètre et méthode

| Source | Volume revu |
|---|---|
| Export RH (source de vérité) | 96 personnes : 85 salariés actifs, 6 départs en 2026, 5 prestataires |
| Microsoft Entra ID | 105 comptes |
| AWS IAM Identity Center | 125 affectations sur 5 comptes AWS |
| GitHub | 47 membres de l'organisation |

Les exports ont été rapprochés automatiquement par le script `access_review.py`, qui applique 13 règles de contrôle à partir de la matrice des rôles. Chaque anomalie a ensuite été présentée au manager concerné, qui a décidé de la conserver, de la corriger ou de la retirer. Le RSSI a validé les décisions.

## 3. Résultats

**32 anomalies** détectées : **7 critiques**, 15 élevées, 9 moyennes, 1 faible.

| Système | Critique | Élevée | Moyenne | Faible | Total |
|---|---|---|---|---|---|
| Entra ID | 5 | 6 | 9 | 1 | 21 |
| AWS | 2 | 3 | 0 | 0 | 5 |
| GitHub | 0 | 6 | 0 | 0 | 6 |
| **Total** | **7** | **15** | **9** | **1** | **32** |

### Anomalies critiques

| ID | Constat | Décision | Corrigé le |
|---|---|---|---|
| F-001 | Développeur sorti le 30/09, compte actif et **utilisé le 02/10** | Désactivation + incident INC-2026-014 | 15/12 |
| F-003 | Prestataire en fin de mission le 30/06, compte actif et **utilisé le 18/09** | Désactivation + incident INC-2026-015 | 15/12 |
| F-002 | Ops sorti le 14/08, accès OpsEngineer à la **production AWS** toujours affecté | Affectations supprimées, aucune clé IAM trouvée | 15/12 |
| F-004 | Compte partagé `support@`, sans MFA, avec accès aux **dossiers patients** | Comptes nominatifs créés, compte supprimé | 16/12 |
| F-005 | Compte `test.admin` sans propriétaire, **administrateur de l'annuaire**, sans MFA | Désactivé, suppression au 15/01/2027 | 15/12 |
| F-006 | Commercial (ancien support N2) ayant conservé l'**accès aux dossiers patients** | Droit retiré ; journaux vérifiés : aucun accès constaté | 15/12 |
| F-007 | Développeur avec **AdministratorAccess en production** | Droit retiré | 16/12 |

### Situation au point de suivi du 29/12/2026

| Statut | Nombre |
|---|---|
| Corrigées dans les délais | 25 (78 %) |
| À corriger, dans les délais | 5 (MFA imposé le 05/01/2027, comptes inactifs) |
| **En retard** | **2** : F-016 et F-017 (AdministratorAccess du Resp. Ops et du CTO). Retrait lié à la mise en place de l'élévation à la demande prévue le 10/01/2027 ; dérogation DER-2026-004 en cours d'instruction pour le CTO |

Le détail des 32 anomalies, des décisions et des justifications figure dans le classeur `Revue_acces_T4-2026_MediSoft.xlsx`.

## 4. Causes racines

| Cause | Anomalies liées | Action |
|---|---|---|
| Les départs ne sont pas transmis automatiquement de la DRH à l'IT | F-001, F-008 | Synchronisation SIRH → Entra ID (MS-PRO-03 v1.1) |
| GitHub n'est pas raccordé au SSO : désactiver le compte Entra ne coupe pas GitHub | F-009 à F-012 | SSO SAML imposé sur l'organisation GitHub |
| La désactivation d'un compte Entra ne supprime pas les affectations AWS | F-002 | Provisionnement automatique (SCIM) entre Entra ID et AWS Identity Center |
| Les mobilités ne déclenchent pas le retrait des anciens droits | F-006, F-015, F-018, F-025 | Groupes dynamiques basés sur le rôle RH |
| Les comptes externes n'ont pas de date d'expiration | F-003, F-023, F-024 | Expiration obligatoire et sponsor pour tout compte externe |
| Droits « temporaires » accordés sans échéance | F-007, F-014, F-019 | Élévation à la demande (AWS) ; demandes de droits avec date de fin |
| MFA non imposé techniquement | F-020, F-026 à F-029 | Accès conditionnel Entra ID exigeant la MFA pour tous |

## 5. Constats à remonter

- **Deux incidents de sécurité** ouverts (INC-2026-014 et INC-2026-015) pour des connexions après départ. Ils sont suivis selon la procédure de gestion des incidents (module 5). Si une donnée personnelle a été consultée, le DPO évaluera la nécessité de notifier les clients concernés (RGPD art. 33).
- **Le constat n° 9 de l'EBIOS RM** (« revue des accès jamais réalisée ») est levé : la première revue a eu lieu. La mesure A.5.18 passe de la maturité 0 à 2. Elle atteindra le niveau 3 lorsque la revue sera réalisée chaque trimestre et que ses preuves seront conservées.

## 6. Prochaine revue

Revue des accès à privilèges et aux données de santé : **mars 2027**. Contrôle mensuel des départs et comptes orphelins : à partir de janvier 2027.

---

| Validé par | Fonction | Date |
|---|---|---|
| | RSSI | 29/12/2026 |
| | Responsable Ops | 29/12/2026 |
| | Directeur général (information) | 29/12/2026 |
