# Procédure de gestion des arrivées, mobilités et départs (JML)

| Référence | MS-PRO-03 | Version | 1.1 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité |
| Date d'approbation | 22/12/2026 | Prochaine revue | 22/12/2027 |

> Procédure d'application de MS-POL-02 §3. La version 1.1 intègre les causes racines identifiées lors de la revue des accès du T4 2026 (MS-ENR-01).

## 1. Objet

Garantir que chaque personne dispose des bons accès **le jour de son arrivée**, les **adapte** quand son poste change, et les **perd le jour de son départ**. Le terme anglais courant est JML : *Joiner, Mover, Leaver*.

**Mesures couvertes :** A.5.16, A.5.18, A.6.1, A.6.5, A.5.11, A.8.2.

## 2. Principe clé : la RH est la source de vérité

Un accès n'existe que s'il correspond à une personne présente dans le SIRH, avec un rôle de la matrice des rôles. Tout compte sans correspondance RH est une anomalie.

```
SIRH (arrivée, mobilité, départ)
      │  synchronisation quotidienne
      ▼
Microsoft Entra ID ── groupes dynamiques selon le rôle
      │  SSO + provisionnement automatique (SCIM)
      ├──► AWS IAM Identity Center
      ├──► GitHub (SSO SAML imposé)
      └──► Outils SaaS
```

**Conséquence :** désactiver la personne dans Entra ID coupe l'accès à tous les outils raccordés. La revue du T4 2026 a montré que GitHub n'était pas raccordé au SSO : 4 personnes parties y avaient encore accès.

## 3. Arrivée

| N° | Étape | Acteur | Délai |
|---|---|---|---|
| 1 | Saisie du nouvel arrivant dans le SIRH : rôle de la matrice, date d'entrée, manager, type de contrat, date de fin pour les CDD, stagiaires, alternants et prestataires | DRH | J-10 |
| 2 | Création automatique du compte Entra ID et rattachement aux groupes du rôle | Automatique | J-5 |
| 3 | Vérifications préalables pour les rôles à privilèges (Ops, admin) : références, signature de la charte | DRH + manager | J-5 |
| 4 | Préparation et enrôlement du poste dans le MDM | Support IT | J-2 |
| 5 | Remise des identifiants en main propre, enregistrement de la MFA, signature de la charte (MS-POL-09) et de l'accord de confidentialité | Support IT + DRH | J0 |
| 6 | Droits supplémentaires hors rôle : sur ticket, validés par le manager et le propriétaire de l'application | Manager | Après J0 |

**Règles :** aucun accès aux données de santé avant la formation sécurité ; les comptes des prestataires, stagiaires, alternants et invités ont **toujours une date d'expiration**, égale à la date de fin du contrat ; un invité a toujours un sponsor interne.

## 4. Mobilité

| N° | Étape | Acteur | Délai |
|---|---|---|---|
| 1 | Saisie du changement de rôle et de la date dans le SIRH | DRH | J-5 |
| 2 | Retrait automatique des groupes de l'ancien rôle et ajout de ceux du nouveau rôle, **le même jour** | Automatique | J0 |
| 3 | Retrait des affectations AWS et du rôle GitHub de l'ancien rôle | Automatique (SCIM) | J0 |
| 4 | Si un droit de l'ancien poste reste nécessaire temporairement (passation) : demande de dérogation de 30 jours maximum | Ancien manager | J0 |
| 5 | Contrôle à J+7 par le RSSI | RSSI | J+7 |

La revue du T4 2026 a révélé deux mobilités dont les anciens droits n'avaient pas été retirés, dont un accès aux dossiers patients conservé 3 mois par un commercial.

## 5. Départ

| N° | Étape | Acteur | Délai |
|---|---|---|---|
| 1 | Saisie de la date de sortie dans le SIRH dès qu'elle est connue | DRH | Dès la démission ou la notification |
| 2 | Désactivation automatique du compte Entra ID à la date et à l'heure de sortie, et révocation des sessions | Automatique | J0, 18 h |
| 3 | Désactivation dans les outils raccordés (SCIM), retrait de l'organisation GitHub | Automatique | J0 |
| 4 | Révocation des clés et jetons personnels (clés SSH, jetons GitHub, clés d'accès AWS) et rotation des secrets partagés auxquels la personne avait accès | Resp. Ops / CTO | J0 |
| 5 | Restitution du matériel selon la check-list ; effacement du poste via le MDM | Support IT | J0 |
| 6 | Transfert des données professionnelles au manager | Manager | J+7 |
| 7 | Suppression définitive du compte | Resp. Ops | J+90 |

**Départ sensible** (licenciement, conflit, accès à privilèges) : désactivation **à l'heure de l'entretien**, sur demande de la DRH au RSSI.

**Fin de mission d'un prestataire** : traitée comme un départ. Le manager du prestataire confirme la date de fin au moins 10 jours avant.

## 6. Check-list de départ

| Élément | Vérifié |
|---|---|
| Compte Entra ID désactivé et sessions révoquées | ☐ |
| Affectations AWS supprimées, aucune clé d'accès IAM personnelle | ☐ |
| Retiré de l'organisation GitHub, jetons révoqués | ☐ |
| Outils SaaS non raccordés au SSO : comptes supprimés | ☐ |
| Secrets partagés connus de la personne changés | ☐ |
| Poste, téléphone, badge et clé FIDO2 restitués | ☐ |
| Boîte mail : réponse automatique et redirection vers le manager (30 jours) | ☐ |
| Rappel écrit de l'obligation de confidentialité et du secret professionnel | ☐ |

## 7. Contrôles

- **Contrôle mensuel** (script `access_review.py`) : rapprochement automatique RH / Entra ID / AWS / GitHub, centré sur les règles R01 à R04 (départs et comptes orphelins).
- **Revue complète trimestrielle** des accès à privilèges et aux données de santé (MS-POL-02 §7).
- **Indicateurs :** délai moyen de désactivation après départ (cible : 0 jour) ; nombre d'accès résiduels détectés (cible : 0) ; part des mobilités traitées le jour même (cible : 100 %).

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/12/2026 | RSSI | Création |
| 1.1 | 22/12/2026 | RSSI | Raccordement de GitHub au SSO, retrait automatique des droits en mobilité, date d'expiration obligatoire pour les invités, contrôle mensuel (suites de la revue T4 2026) |
