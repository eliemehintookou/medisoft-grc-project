# Politique de contrôle d'accès et d'authentification

| Référence | MS-POL-02 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité |
| Date d'approbation | 01/12/2026 | Prochaine revue | 01/12/2027 |

## 1. Objet et périmètre

Encadrer l'attribution, l'usage, la revue et le retrait des accès à tous les systèmes de MediSoft : comptes AWS, annuaire Entra ID, GitHub, outils SaaS, plateforme MediSoft Care (accès internes et accès des clients).

**Mesures couvertes :** A.5.15 à A.5.18, A.6.5, A.8.2 à A.8.5, A.8.15. **Constats EBIOS traités :** n° 1 (MFA), 2 (moindre privilège), 9 (revue des accès).

## 2. Principes

1. **Moindre privilège** : un accès est accordé pour un besoin précis et pour la durée de ce besoin.
2. **Accès fondé sur les rôles** : les droits sont attribués à des rôles (profils), jamais directement à des personnes.
3. **Un compte = une personne** : les comptes partagés ou génériques sont interdits, sauf compte technique documenté.
4. **Séparation des comptes** : un administrateur dispose d'un compte personnel pour l'usage courant et d'un compte d'administration distinct.

## 3. Cycle de vie des accès (arrivée, mobilité, départ)

| Étape | Déclencheur | Règle | Délai |
|---|---|---|---|
| Arrivée | Demande de la DRH | Création du compte à partir du profil du poste, validé par le manager | Avant le premier jour |
| Demande d'accès supplémentaire | Ticket | Validation du manager, et du propriétaire de l'application pour les accès sensibles | 2 jours ouvrés |
| Mobilité | Changement de poste notifié par la DRH | Retrait des anciens droits **avant** l'attribution des nouveaux | 5 jours ouvrés |
| Départ | Notification de la DRH | Désactivation de tous les comptes (annuaire, AWS, GitHub, SaaS) et révocation des jetons et clés | **Le jour du départ** |
| Prestataire | Fin de mission | Comptes créés avec une date d'expiration automatique | Expiration à la date de fin |

Les comptes inactifs depuis 90 jours sont désactivés automatiquement.

## 4. Authentification

| Population | Exigence |
|---|---|
| Tous les collaborateurs | SSO Entra ID + **MFA** (application d'authentification ou clé FIDO2) |
| Comptes d'administration (AWS, annuaire, GitHub) | MFA résistant à l'hameçonnage (clé FIDO2) obligatoire |
| Compte root AWS | MFA matériel, utilisé uniquement en cas d'urgence (procédure « bris de glace »), toute connexion déclenche une alerte |
| Utilisateurs professionnels de santé (clients) | Authentification forte : Pro Santé Connect (e-CPS) ou MFA équivalent |
| Comptes techniques | Pas de mot de passe statique quand c'est possible (rôles IAM) ; sinon secret stocké dans AWS Secrets Manager avec rotation |

**Mots de passe** (lorsqu'ils restent nécessaires) : 12 caractères minimum avec plusieurs types de caractères, ou phrase de passe de 16 caractères minimum ; vérification contre les listes de mots de passe compromis ; pas d'expiration périodique imposée, mais changement obligatoire en cas de suspicion de compromission ; gestionnaire de mots de passe d'entreprise fourni.

## 5. Accès à privilèges

- Pas de droits d'administration permanents sur AWS : élévation **à la demande** via AWS IAM Identity Center, pour une durée maximale de 8 heures, avec ticket justificatif.
- La politique `AdministratorAccess` n'est attribuée qu'aux 2 comptes « bris de glace ».
- Toutes les actions d'administration sont journalisées (CloudTrail) et conservées 1 an.
- Les développeurs n'ont **aucun accès en écriture à la production** : les déploiements passent par la chaîne CI/CD.

## 6. Accès aux données de santé

- Le support n'accède aux données d'un client que **sur ticket**, avec l'accord du client et pour une durée limitée.
- Chaque consultation d'un dossier patient est journalisée (qui, quoi, quand, depuis où) et ce journal est consultable par le client.
- Les extractions massives de données sont interdites sans validation du RSSI et du DPO.

## 7. Revue des accès

| Périmètre | Fréquence | Réalisée par | Validée par |
|---|---|---|---|
| Comptes à privilèges (AWS, annuaire, GitHub admin) | Trimestrielle | Resp. Ops | RSSI |
| Accès à la production et aux données de santé | Trimestrielle | Resp. Ops | RSSI |
| Autres accès (outils SaaS, partages) | Semestrielle | Managers | RSSI |
| Comptes des prestataires | À chaque fin de mission + trimestrielle | Managers | RSSI |

Chaque revue produit une preuve (export des comptes, décisions de maintien ou de retrait, date de correction) conservée pour l'audit.

## 8. Indicateurs

- Taux de comptes à privilèges sous MFA (cible : 100 %)
- Délai moyen de désactivation après un départ (cible : 0 jour)
- Nombre de comptes orphelins détectés lors des revues
- Taux de revues réalisées dans les délais (cible : 100 %)

## 9. Exceptions

Toute exception passe par la procédure de dérogation MS-PRO-01.

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/12/2026 | RSSI | Création |
