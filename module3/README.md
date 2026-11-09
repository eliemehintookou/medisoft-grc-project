# Module 3 — Gestion des accès et des habilitations

> Projet GRC « fil rouge » sur **MediSoft**, éditeur fictif de logiciel de santé en SaaS.
> Ce module met en œuvre la politique de contrôle d'accès [MS-POL-02](../module2/MS-POL-02_Controle_acces.md) et traite le chantier **PA-04 (identités et accès)** du plan d'action du [module 1](../module1/).

## Objectif

Réaliser la **première revue des accès** de MediSoft. Le constat n° 9 de l'EBIOS RM indiquait qu'elle n'avait jamais été faite. Concrètement :

1. Définir **qui doit avoir accès à quoi** : la matrice des rôles.
2. Comparer ce qui **existe réellement** dans l'annuaire, AWS et GitHub avec la source de vérité RH.
3. Faire décider les managers, corriger, et **prouver** que c'est fait.
4. Corriger les **causes** pour que les anomalies ne reviennent pas : la procédure arrivées, mobilités et départs.

## Contenu

```
module3/
├── README.md
├── MS-PRO-03_Arrivees_mobilites_departs.md   Procédure JML (v1.1, enrichie après la revue)
├── MS-ENR-01_PV_revue_acces_T4-2026.md       Procès-verbal de la revue
├── data/                                     Exports fictifs (CSV, séparateur ;)
│   ├── export_rh.csv                         Source de vérité : 96 personnes
│   ├── export_entra_id.csv                   105 comptes
│   ├── export_aws_identity_center.csv        125 affectations
│   ├── export_github.csv                     47 membres
│   └── matrice_roles.csv                     17 rôles
├── scripts/
│   ├── matrice.py                            Matrice des rôles et comptes techniques
│   ├── gen_data.py                           Génère les exports (avec anomalies volontaires)
│   ├── access_review.py                      Revue automatique : 13 règles de contrôle
│   └── build_review_xlsx.py                  Construit le classeur de revue
└── output/
    ├── anomalies.csv                         32 anomalies détectées
    └── Revue_acces_T4-2026_MediSoft.xlsx     Matrice, anomalies et décisions, synthèse
```

## Utilisation

```bash
cd scripts
python gen_data.py                 # régénère les exports fictifs
python access_review.py            # détecte les anomalies → output/anomalies.csv
python build_review_xlsx.py        # classeur de revue (nécessite openpyxl)
```

`access_review.py` n'utilise que la bibliothèque standard de Python. On peut lui passer une date de référence : `python access_review.py 2027-03-15`.

## Les 13 règles de contrôle

| Règle | Ce qui est vérifié | Pourquoi c'est important |
|---|---|---|
| R01 | Personne sortie avec un compte actif | Accès d'un ancien salarié, peut-être mécontent |
| R02 | Droits AWS ou GitHub restants après un départ | Désactiver l'annuaire ne suffit pas si un outil n'y est pas raccordé |
| R03 | Prestataire en fin de mission encore actif | Les prestataires sont souvent oubliés : ils ne passent pas par la paie |
| R04 | Compte orphelin ou générique partagé | Aucune imputabilité : impossible de savoir qui a fait quoi |
| R05 | Invité sans sponsor ni date d'expiration | Accès externe sans responsable |
| R06 | Doublon | Un second compte souvent moins protégé (sans MFA) |
| R07 | Groupe hors matrice, dont droits cumulés après mobilité | Accumulation de droits avec le temps |
| R08 | Droit AWS hors matrice | AdministratorAccess en production hors comptes d'urgence |
| R09 | Rôle GitHub hors matrice | Un owner peut désactiver toute la sécurité de l'organisation |
| R10 | MFA non enregistré | Mot de passe seul : vulnérable à l'hameçonnage |
| R11 | Inactivité de plus de 90 jours | Compte inutile, donc surface d'attaque inutile |
| R12 | Compte de service utilisé en interactif | Identifiants techniques partagés entre humains |
| R13 | 2FA GitHub désactivée | Accès au code source avec un mot de passe seul |

## Résultats

**32 anomalies, dont 7 critiques.** Deux ont donné lieu à l'ouverture d'un **incident de sécurité** : un ancien développeur et une ancienne prestataire se sont connectés **après leur départ**. Au point de suivi, 78 % des anomalies étaient corrigées, toutes dans les délais, et 2 étaient en retard (droits d'administration du CTO et du Resp. Ops, en attente de l'élévation à la demande).

### Corrigé : anomalies introduites volontairement dans les exports

| Anomalie introduite | Détectée par |
|---|---|
| Développeur sorti, compte actif et utilisé après le départ | F-001 (R01, critique) |
| Commercial sorti, compte actif | F-008 (R01) |
| Ops sorti : compte désactivé, mais droits AWS production et GitHub conservés | F-002 (R02, critique) + F-011 |
| 3 prestataires terminés toujours sur GitHub (constat du module 1) | F-009, F-010, F-012 |
| Une prestataire terminée avec compte actif et utilisé après la fin de mission | F-003 (R03, critique) |
| Compte partagé `support@` avec accès aux dossiers patients | F-004 (R04, critique) |
| Compte `test.admin` administrateur de l'annuaire, sans propriétaire | F-005 (R04, critique) |
| Mobilité Support N2 → Commercial : accès aux dossiers patients conservé | F-006 (R07, critique) + F-025 |
| Mobilité Ops → Dev : groupe Ops et accès production conservés | F-015 + F-018 |
| AdministratorAccess en production : un développeur, le CTO, le Resp. Ops | F-007 (critique), F-017, F-016 |
| Commercial ajouté au groupe Ops | F-014 |
| Compte en doublon d'une développeuse | F-013 |
| Stagiaire owner de l'organisation GitHub | F-019 |
| 5 comptes sans MFA, dont un Ops | F-020 (élevée), F-026 à F-029 |
| Compte de service des sauvegardes utilisé en connexion interactive | F-021 |
| 2FA GitHub désactivée | F-022 |
| 2 auditeurs externes sans sponsor ni expiration | F-023, F-024 |
| 3 comptes inactifs, dont un congé maternité (exception justifiée) | F-030, F-031, F-032 |

**Aucun faux positif** : les 3 départs correctement traités, les comptes d'urgence, le compte de service de la CI/CD et les droits conformes à la matrice ne sont pas signalés.

## Points clés à savoir expliquer

- **La RH est la source de vérité.** On ne revoit pas les accès « au feeling » : on rapproche ce qui existe de ce qui devrait exister.
- **Désactiver l'annuaire ne suffit pas.** 4 accès GitHub et 1 accès AWS ont survécu à la désactivation des comptes. Il faut raccorder chaque outil au SSO et au provisionnement automatique.
- **La mobilité est le cas le plus oublié.** On pense aux départs, rarement aux changements de poste, et les droits s'accumulent.
- **Une revue des accès se termine par des décisions des managers, pas par une liste d'anomalies.** Le RSSI ne connaît pas les besoins de chaque équipe : il outille, anime, contrôle et prouve.
- **Corriger les causes, pas seulement les anomalies.** Chaque anomalie a été rattachée à une cause racine, et la procédure MS-PRO-03 est passée en v1.1.
- **Une anomalie peut révéler un incident.** Une connexion après un départ n'est plus un problème de conformité, c'est un potentiel accès illégitime.

## Suite

- **Module 4 — Sécurité des projets et des fournisseurs** : check-list sécurité pour les chefs de projet, évaluation d'un outil SaaS, cahier des charges d'un test d'intrusion, clauses DORA.

---
*Entreprise, personnes et données entièrement fictives, générées aléatoirement dans un but d'apprentissage.*
