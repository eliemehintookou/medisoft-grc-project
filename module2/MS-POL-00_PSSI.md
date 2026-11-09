# Politique de sécurité des systèmes d'information (PSSI)

| Référence | MS-POL-00 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Directeur général |
| Date d'approbation | 01/12/2026 | Prochaine revue | 01/12/2027 |

> Document de tête de la documentation sécurité de MediSoft. Les politiques thématiques (MS-POL-01 à MS-POL-08) et les procédures (MS-PRO) en précisent l'application.

---

## 1. Engagement de la direction

MediSoft édite et exploite des solutions qui traitent les données de santé de plusieurs centaines de milliers de patients. Nos clients, établissements de santé et assureurs, nous confient des informations couvertes par le secret médical. **Protéger ces données est une condition de notre activité, pas une option.**

La direction générale s'engage à :

- fournir les moyens humains et financiers nécessaires à la sécurité, au travers d'un budget annuel dédié ;
- mettre en place et maintenir un système de management de la sécurité de l'information (SMSI) conforme à l'ISO/IEC 27001:2022 ;
- respecter les obligations légales, réglementaires et contractuelles recensées dans le registre des obligations (module 1) ;
- présider le comité sécurité et conduire chaque année la revue de direction ;
- suivre la formation sécurité prévue pour les dirigeants.

*Signé : le Directeur général, le 01/12/2026*

## 2. Objet

Cette politique fixe les objectifs, l'organisation et les principes de sécurité de MediSoft. Elle s'impose à toute personne qui accède au système d'information.

## 3. Périmètre

| Élément | Inclus |
|---|---|
| Activités | Développement, hébergement, exploitation et support de MediSoft Care (SaaS) et de MediSoft Patient (application mobile) |
| Infrastructure | Comptes AWS (région eu-west-3), annuaire Microsoft Entra ID, GitHub, outils collaboratifs, postes de travail |
| Personnes | Salariés, stagiaires, alternants, prestataires et sous-traitants ayant un accès |
| Lieux | Bureaux de Paris, télétravail, déplacements |

Ce périmètre est celui du SMSI (clause 4.3 de l'ISO 27001).

## 4. Références

- ISO/IEC 27001:2022 et 27002:2022
- RGPD et loi Informatique et Libertés
- Code de la santé publique (art. L.1110-4 sur le secret, art. L.1111-8 sur l'hébergement des données de santé) et référentiel de certification HDS v2.0
- Directive NIS2 (en cours de transposition), règlement DORA (exigences contractuelles des clients financiers), règlement CRA (application mobile)
- Guide d'hygiène informatique de l'ANSSI, PGSSI-S de l'Agence du Numérique en Santé

## 5. Objectifs de sécurité

| Critère | Besoin | Ce que cela signifie pour MediSoft |
|---|---|---|
| **Confidentialité** | Très élevé | Aucune donnée de santé ne doit être accessible à une personne non autorisée |
| **Intégrité** | Très élevé | Une donnée médicale altérée peut entraîner une erreur de soin |
| **Disponibilité** | Élevé | MediSoft Care est utilisé en continu par les établissements (RTO 4 h, RPO 1 h) |
| **Traçabilité** | Élevé | Tout accès à un dossier patient doit pouvoir être retrouvé et attribué |

**Objectifs mesurables pour 2027** (clause 6.2) :

| N° | Objectif | Cible | Échéance |
|---|---|---|---|
| O1 | Comptes à privilèges protégés par MFA | 100 % | 31/03/2027 |
| O2 | Bases, buckets et sauvegardes chiffrés | 100 % | 31/03/2027 |
| O3 | Collaborateurs formés à la sécurité | ≥ 95 % | 30/06/2027 |
| O4 | Vulnérabilités critiques corrigées en moins de 7 jours | ≥ 90 % | 30/06/2027 |
| O5 | Tests de restauration réussis | 4 par an | 31/12/2027 |
| O6 | Certification HDS v2.0 obtenue | Oui | 30/06/2027 |
| O7 | Certification ISO 27001 obtenue | Oui | 31/12/2027 |

Ces objectifs sont suivis dans le tableau de bord sécurité (module 6).

## 6. Organisation

L'organisation détaillée (rôles, comité, matrice RACI) fait l'objet du document **MS-POL-01**. En résumé :

- le **Directeur général** est responsable en dernier ressort de la sécurité ;
- le **RSSI** pilote le SMSI et rend compte au Directeur général ;
- le **DPO** veille au respect du RGPD ;
- chaque **manager** applique la PSSI dans son équipe ;
- chaque **collaborateur** respecte la charte informatique (MS-POL-09) et signale tout incident.

## 7. Principes de sécurité

Chaque principe renvoie à la politique qui le détaille.

| N° | Principe | Document | Mesures ISO 27001 |
|---|---|---|---|
| P1 | **Moindre privilège** : chacun n'a accès qu'à ce dont il a besoin, pour la durée nécessaire | MS-POL-02 | A.5.15 à A.5.18, A.8.2 |
| P2 | **Authentification forte** pour tout accès à privilèges ou à distance | MS-POL-02 | A.5.17, A.8.5 |
| P3 | **Chiffrement systématique** des données de santé, au repos et en transit | MS-POL-03 | A.8.24 |
| P4 | **Sauvegarde testée** : une sauvegarde non restaurée n'est pas une sauvegarde | MS-POL-04 | A.8.13 |
| P5 | **Données de santé dans l'EEE**, chez un hébergeur certifié HDS | MS-POL-05 | A.5.23 |
| P6 | **Sécurité dès la conception** dans les projets et le développement | MS-POL-06 | A.5.8, A.8.25 à A.8.29 |
| P7 | **Classification** : chaque information est protégée selon sa sensibilité | MS-POL-07 | A.5.12 à A.5.14, A.5.33 |
| P8 | **Postes maîtrisés** : seuls des postes gérés et chiffrés accèdent au SI | MS-POL-08 | A.6.7, A.8.1 |
| P9 | **Cloisonnement** des environnements de production, de préproduction et de développement | MS-POL-05 | A.8.22, A.8.31 |
| P10 | **Traçabilité** des accès et des actions sensibles | MS-POL-02 | A.8.15, A.8.16 |
| P11 | **Fournisseurs évalués** et engagés contractuellement | Module 4 | A.5.19 à A.5.22 |
| P12 | **Incidents signalés sans délai** et traités selon une procédure | Module 5 | A.5.24 à A.5.28, A.6.8 |

## 8. Gestion des risques

Les risques sont appréciés avec la méthode **EBIOS Risk Manager** (analyse de novembre 2026). L'analyse est révisée chaque année et à chaque changement majeur : nouveau produit, nouvel hébergeur, incident grave. Les risques résiduels sont acceptés formellement par leurs propriétaires.

## 9. Dérogations

Une règle de sécurité qui ne peut pas être appliquée fait l'objet d'une **demande de dérogation** (procédure MS-PRO-01). Une dérogation est limitée dans le temps, s'accompagne de mesures compensatoires et est enregistrée dans le registre des dérogations. **Aucune règle ne peut être contournée sans dérogation approuvée.**

## 10. Sanctions

Le non-respect de la PSSI peut entraîner des sanctions disciplinaires prévues au règlement intérieur, sans préjudice d'éventuelles poursuites (notamment pour violation du secret professionnel, art. 226-13 du Code pénal).

## 11. Contrôle et révision

- Conformité vérifiée par l'audit interne annuel et les contrôles du RSSI.
- PSSI revue au moins une fois par an, et après tout incident majeur ou évolution réglementaire importante.
- Toute modification est validée par le comité sécurité et approuvée par le Directeur général (procédure MS-PRO-02).

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/12/2026 | RSSI | Création |
