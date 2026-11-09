# Check-list sécurité pour les chefs de projet

| Référence | MS-MOD-01 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité |
| Date d'approbation | 15/01/2027 | Prochaine revue | 15/01/2028 |

> Outil de la mesure A.5.8 (sécurité dans la gestion de projet). À remplir par le chef de projet, avec l'appui du RSSI. Elle s'applique aux projets produit (nouvelle fonctionnalité de MediSoft Care) comme aux projets internes (nouvel outil SaaS).

## Étape 0 — Quel niveau d'accompagnement ?

Répondre aux 6 questions. **Une seule réponse « oui » aux questions 1 à 3 → projet sensible.**

| N° | Question | Oui / Non |
|---|---|---|
| 1 | Le projet traite-t-il des **données de santé** (C3) ? | |
| 2 | Le projet est-il **exposé sur Internet** ou modifie-t-il l'authentification ? | |
| 3 | Le projet fait-il intervenir un **nouveau fournisseur** Tier 1 (accès production ou données de santé) ? | |
| 4 | Le projet traite-t-il d'autres données personnelles ? | |
| 5 | Le projet modifie-t-il l'infrastructure de production ? | |
| 6 | Le projet utilise-t-il un service d'IA ? | |

| Niveau | Condition | Accompagnement |
|---|---|---|
| **Sensible** | Oui à l'une des questions 1 à 3 | RSSI associé dès le cadrage ; analyse de menaces ; pentest avant mise en production ; validation formelle du RSSI |
| **Standard** | Oui aux questions 4 à 6 uniquement | Check-list complète, revue par le RSSI aux étapes 1 et 3 |
| **Léger** | Non partout | Check-list auto-déclarative, sans revue |

## Étape 1 — Cadrage

| N° | Point de contrôle | Réf. | Fait |
|---|---|---|---|
| 1.1 | Les données traitées sont identifiées et classées (C0 à C3) | MS-POL-07 | ☐ |
| 1.2 | Le DPO est consulté si des données personnelles sont traitées ; une analyse d'impact (AIPD) est faite si nécessaire, ou l'aide aux clients pour la leur est prévue | RGPD art. 35 | ☐ |
| 1.3 | Les obligations applicables sont identifiées (HDS, RGPD, exigences des clients, DORA, CRA) | Registre module 1 | ☐ |
| 1.4 | Tout nouveau fournisseur ou outil SaaS est évalué avant signature | MS-POL-10 | ☐ |
| 1.5 | Un budget et du temps sont prévus pour la sécurité (tests, corrections) | — | ☐ |

## Étape 2 — Conception

| N° | Point de contrôle | Réf. | Fait |
|---|---|---|---|
| 2.1 | Les exigences de sécurité sont rédigées (OWASP ASVS niveau 2 pour les applications) | MS-POL-06 | ☐ |
| 2.2 | Pour un projet sensible : analyse de menaces (qui pourrait attaquer, comment, avec quel impact) | A.8.25 | ☐ |
| 2.3 | Les accès sont définis par rôle et ajoutés à la matrice des rôles | MS-POL-02 | ☐ |
| 2.4 | Authentification : SSO et MFA pour les utilisateurs internes ; Pro Santé Connect ou MFA pour les professionnels de santé | MS-POL-02 §4 | ☐ |
| 2.5 | Chiffrement prévu au repos et en transit | MS-POL-03 | ☐ |
| 2.6 | Journalisation des événements de sécurité et des accès aux données de santé | MS-POL-05 | ☐ |
| 2.7 | Hébergement dans l'EEE, chez un hébergeur certifié HDS si données de santé | MS-POL-05 | ☐ |
| 2.8 | Durée de conservation et suppression des données définies | MS-POL-07 | ☐ |

## Étape 3 — Réalisation et recette

| N° | Point de contrôle | Réf. | Fait |
|---|---|---|---|
| 3.1 | Revue de code et contrôles automatiques de la CI au vert (SAST, dépendances, secrets) | MS-POL-06 | ☐ |
| 3.2 | Aucune donnée réelle de patient en développement ni en recette | A.8.33 | ☐ |
| 3.3 | Tests de sécurité réalisés : DAST ; **pentest pour un projet sensible** (cahier des charges MS-MOD-02) | A.8.29 | ☐ |
| 3.4 | Vulnérabilités critiques et élevées corrigées ; les autres acceptées formellement par le propriétaire du risque | — | ☐ |
| 3.5 | Contrat fournisseur signé avec les clauses de sécurité | MS-MOD-03 | ☐ |

## Étape 4 — Mise en production (go / no-go sécurité)

| N° | Point de contrôle | Réf. | Fait |
|---|---|---|---|
| 4.1 | Comptes de test et accès temporaires supprimés | MS-POL-02 | ☐ |
| 4.2 | Sauvegarde configurée et restauration testée | MS-POL-04 | ☐ |
| 4.3 | Alertes de sécurité raccordées au SIEM | — | ☐ |
| 4.4 | Documentation d'exploitation rédigée | A.5.37 | ☐ |
| 4.5 | Utilisateurs informés et formés si nécessaire | A.6.3 | ☐ |
| 4.6 | Inscription au registre des actifs et, le cas échéant, au registre des traitements | A.5.9 | ☐ |
| 4.7 | **Validation du RSSI** pour un projet sensible, ou dérogation pour les points non conformes | MS-PRO-01 | ☐ |

## Étape 5 — Après la mise en production

| N° | Point de contrôle | Fait |
|---|---|---|
| 5.1 | Revue à 3 mois : incidents, alertes, droits d'accès réellement utilisés | ☐ |
| 5.2 | Ajout du périmètre au prochain pentest annuel | ☐ |

---

**Exemple d'application :** le projet « assistant IA pour le support » est **sensible** (questions 1, 3 et 6). L'étape 1.4 a conduit à l'évaluation de HelpBot AI (MS-ENR-02), qui a abouti à un avis défavorable pour les tickets contenant des données de santé.

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 15/01/2027 | RSSI | Création |
