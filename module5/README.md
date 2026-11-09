# Module 5 — Gestion des incidents et sensibilisation

> Projet GRC « fil rouge » sur **MediSoft**, éditeur fictif de logiciel de santé en SaaS.
> Ce module traite les chantiers **PA-06 (gestion des incidents)**, **PA-09 (sensibilisation)** et **PA-18 (veille)** du plan d'action du [module 1](../module1/), ainsi que les mesures A.5.5 à A.5.7, A.5.24 à A.5.28, A.6.3 et A.6.8.

## Objectif

Le module 1 a montré que MediSoft n'avait **ni procédure d'incident, ni sensibilisation, ni veille**. Pourtant, une entreprise qui traite des données de santé doit savoir **réagir vite** et **notifier dans les délais** : 24 h pour les clients, 72 h pour la CNIL, 24 h pour l'ANSSI lorsque NIS2 s'appliquera. Ce module construit la capacité de réaction et la culture sécurité.

## Contenu

| Document | Ce qu'il apporte |
|---|---|
| [MS-PRO-04](MS-PRO-04_Gestion_incidents.md) — Procédure de gestion des incidents | Grille de gravité G1 à G4, rôles, 6 phases, **tableau des notifications** (clients, CNIL, ANSSI, assureurs, CSIRT, plainte), registre des incidents |
| [MS-MOD-04](MS-MOD-04_Playbooks.md) — Playbooks | Fiches réflexes : phishing, rançongiciel, fuite de données, compromission de compte |
| [MS-ENR-04](MS-ENR-04_Qualification_signalements.md) — Qualification des signalements | 5 catégories, **arbre de décision**, indices à vérifier, et qualification de 8 messages réels d'une semaine |
| [MS-ENR-05](MS-ENR-05_Rapports_incidents_INC-2026-014-015.md) — Rapports d'incident | Traitement complet des 2 incidents découverts par la revue des accès du module 3 |
| [MS-PRO-05](MS-PRO-05_Programme_sensibilisation.md) — Programme de sensibilisation 2027 | 6 publics, calendrier sur 12 mois, règles du phishing simulé, résultats de la 1re campagne, indicateurs |
| [Guide des 10 réflexes](communication/Guide_bonnes_pratiques.md) | Guide d'une page pour tous les collaborateurs |
| [Alerte sécurité](communication/Alerte_securite_2027-01.md) | Alerte interne sur une vague de phishing ciblé |
| [Lettre Cyber n° 1](communication/Newsletter_cyber_01.md) | Newsletter interne trimestrielle |
| [Bulletin de veille](communication/Bulletin_veille_2026-11.md) | Veille réglementaire, menaces et technique, **basée sur l'actualité réelle** de novembre 2026 |

## Résultats clés

- **Incident INC-2026-014** : un ancien développeur s'est connecté à sa messagerie après son départ. C'est une violation de données personnelles (messagerie avec des données de collègues), mais au risque jugé **improbable** : elle n'est **pas notifiée à la CNIL**, mais elle est **inscrite au registre** avec sa justification.
- **Incident INC-2026-015** : une ancienne prestataire a cloné un dépôt dont l'historique contenait une **clé d'API toujours valide**. La clé a été révoquée et 2 autres secrets ont été trouvés et changés.
- **Semaine de signalements** : 8 messages, dont 4 phishing ciblés. Une personne a saisi ses identifiants, mais la **MFA a bloqué l'attaquant**.
- **1re campagne de phishing simulé** : 24 % de clics, 9 % de saisies d'identifiants, 18 % de signalements. Objectif fin 2027 : moins de 10 % de clics et plus de 50 % de signalements.

## Points clés à savoir expliquer

- **MediSoft est sous-traitante pour les données des patients.** En cas de violation, ce n'est pas elle qui notifie la CNIL : elle prévient **sans délai** ses clients, responsables de traitement, qui notifient la CNIL sous 72 h.
- **Toute violation se documente, même non notifiée** (RGPD art. 33.5). Ne pas notifier est une décision qui doit être justifiée.
- **Le délai court à partir de la connaissance de l'incident**, pas de la fin de l'enquête. On notifie ce qu'on sait, puis on complète.
- **Rançongiciel : isoler sans éteindre**, protéger les sauvegardes en premier, ne pas restaurer avant d'avoir trouvé le point d'entrée, porter plainte sous 72 h pour l'assurance.
- **Supprimer un secret du code ne suffit pas** : il reste dans l'historique Git. Il faut le révoquer.
- **En sensibilisation, le taux de signalement compte autant que le taux de clic** : un signalement rapide protège tous les autres.
- **Le phishing simulé ne sanctionne pas** : il mesure et il éduque.

## Suite

- **Module 6 — Pilotage et audit** : tableau de bord des indicateurs de sécurité, suivi du plan d'action, préparation d'un audit (dossier de preuves) et revue de direction.

---
*Entreprise, personnes, incidents et messages fictifs, réalisés dans un but d'apprentissage. Seul le bulletin de veille s'appuie sur l'actualité réelle, avec ses sources.*
