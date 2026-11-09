# Module 2 — Gouvernance documentaire de la sécurité

> Projet GRC « fil rouge » sur **MediSoft**, éditeur fictif de logiciel de santé en SaaS.
> Ce module traite les chantiers **PA-01 (gouvernance)** et **PA-03 (corpus documentaire)** du plan d'action issu du [module 1](../module1/).

## Objectif

Le module 1 a montré que MediSoft n'avait ni RSSI, ni PSSI, ni procédure : les clauses 5 et 7.5 de l'ISO 27001 étaient presque à zéro. Ce module construit le **socle documentaire** du système de management de la sécurité : ce qu'on décide (politiques), qui le fait (organisation) et comment on gère les exceptions (dérogations).

## Pyramide documentaire

```
                 ┌───────────────────┐
                 │   MS-POL-00 PSSI  │  ← engagement de la direction, principes
                 └─────────┬─────────┘
        ┌──────────────────┴──────────────────┐
        │ MS-POL-01  Organisation et RACI     │  ← qui fait quoi
        │ MS-POL-02 à 08  Politiques          │  ← règles par domaine
        │ MS-POL-09  Charte utilisateurs      │  ← règles pour chaque collaborateur
        └──────────────────┬──────────────────┘
        ┌──────────────────┴──────────────────┐
        │ MS-PRO-01  Dérogations              │  ← gérer les exceptions
        │ MS-PRO-02  Gestion documentaire     │  ← faire vivre les documents
        └─────────────────────────────────────┘
```

## Documents

| Référence | Document | Ce qu'il apporte |
|---|---|---|
| [MS-POL-00](MS-POL-00_PSSI.md) | Politique de sécurité des SI | Engagement du DG, périmètre du SMSI, besoins de sécurité, 7 objectifs mesurables pour 2027, 12 principes |
| [MS-POL-01](MS-POL-01_Organisation_securite.md) | Organisation et matrice RACI | Rôles, comité sécurité, revue de direction, cellule de crise, RACI sur 22 activités |
| [MS-POL-02](MS-POL-02_Controle_acces.md) | Contrôle d'accès | Arrivées et départs, MFA, accès à privilèges à la demande, accès support aux données de santé, revues des accès |
| [MS-POL-03](MS-POL-03_Cryptographie.md) | Cryptographie | Chiffrement par situation, algorithmes autorisés et interdits, gestion des clés KMS |
| [MS-POL-04](MS-POL-04_Sauvegarde.md) | Sauvegarde | RPO / RTO, règle 3-2-1 avec copie immuable, tests de restauration trimestriels |
| [MS-POL-05](MS-POL-05_Cloud.md) | Sécurité du cloud | Responsabilité partagée AWS, séparation des comptes, régions de l'EEE, journalisation, réversibilité |
| [MS-POL-06](MS-POL-06_Developpement_securise.md) | Développement sécurisé | Cycle de développement sécurisé, contrôles en CI, données de test, prestataires, exigences CRA |
| [MS-POL-07](MS-POL-07_Classification_donnees.md) | Classification et conservation | 4 niveaux (C0 à C3), règles de manipulation, durées de conservation, suppression en fin de contrat |
| [MS-POL-08](MS-POL-08_Postes_teletravail.md) | Postes et télétravail | MDM, chiffrement, EDR, télétravail, perte ou vol |
| [MS-POL-09](MS-POL-09_Charte_informatique.md) | Charte informatique | Règles pour tous, en langage simple, à signer |
| [MS-PRO-01](MS-PRO-01_Derogation.md) | Procédure de dérogation | Processus, niveaux d'approbation, formulaire, exemple complet, registre |
| [MS-PRO-02](MS-PRO-02_Gestion_documentaire.md) | Gestion documentaire | Structure, versions, cycle de validation, liste des documents en vigueur |

## Traçabilité avec le module 1

### Constats EBIOS RM traités

| Constat (atelier 1) | Traité dans |
|---|---|
| 1. MFA incomplet | MS-POL-02 §4 |
| 2. Droits trop larges | MS-POL-02 §2 et §5 |
| 3. Chiffrement au repos non généralisé | MS-POL-03 §2 |
| 4. TLS interne non vérifié | MS-POL-03 §2 |
| 5. Réseau à plat | MS-POL-05 §3 |
| 6. Journalisation partielle | MS-POL-05 §3 |
| 7. Sauvegardes jamais testées | MS-POL-04 §4 |
| 8. Pas de gestion des correctifs | MS-POL-06 §7, MS-POL-08 §2 |
| 9. Revue des accès jamais faite | MS-POL-02 §7 |
| 10. Pas de sensibilisation | MS-POL-09 (premier support ; programme complet au module 5) |
| 11. CI/CD non sécurisée | MS-POL-06 §2 et §5 |

### Exigences ISO 27001 couvertes

| Exigence | Document |
|---|---|
| Clauses 4.3, 5.1, 5.2, 6.2 | MS-POL-00 |
| Clause 5.3, A.5.2 à A.5.6 | MS-POL-01 |
| Clause 7.5, A.5.37 | MS-PRO-02 |
| A.5.15 à A.5.18, A.6.5, A.8.2 à A.8.5 | MS-POL-02 |
| A.8.24 | MS-POL-03 |
| A.8.13, A.8.14, A.5.30 | MS-POL-04 |
| A.5.23, A.8.9, A.8.20, A.8.22, A.8.31 | MS-POL-05 |
| A.5.8, A.8.4, A.8.11, A.8.25 à A.8.33 | MS-POL-06 |
| A.5.9, A.5.10, A.5.12 à A.5.14, A.5.33, A.7.14, A.8.10 | MS-POL-07 |
| A.6.7, A.7.7, A.7.9, A.7.10, A.8.1, A.8.7, A.8.18, A.8.23 | MS-POL-08 |
| A.5.10, A.6.2, A.6.4, A.6.8 | MS-POL-09 |

### Obligations réglementaires prises en compte

- **RGPD et secret médical** : MS-POL-02 §6, MS-POL-07, MS-POL-09
- **HDS v2.0** : localisation EEE et responsabilité partagée (MS-POL-05), sauvegarde (MS-POL-04), traçabilité (MS-POL-02)
- **NIS2** : responsabilité de la direction (MS-POL-00 et MS-POL-01), MFA, chiffrement, continuité
- **DORA** (clients assureurs) : tests de restauration ouverts aux clients (MS-POL-04), réversibilité (MS-POL-05)
- **CRA** (appli mobile) : SBOM et signalement des vulnérabilités exploitées (MS-POL-06 §5 et §7)

## Points clés à savoir expliquer

- **Écrire n'est pas appliquer.** Ces documents font passer de nombreuses mesures de la maturité 1 à la maturité 2. Le niveau 3 n'est atteint que lorsqu'on a la **preuve** que la règle est appliquée (exports de revue des accès, PV de restauration…). C'est l'objet du module 6.
- **Une politique dit « quoi », une procédure dit « qui » et « comment ».** Les mélanger produit des documents ingérables.
- **Une dérogation n'est pas un passe-droit.** Elle transforme un contournement silencieux en risque connu, limité dans le temps et compensé. Certaines règles n'en admettent aucune : données de santé hors de l'EEE, par exemple.
- **Chaque règle se rattache à une raison** : un risque EBIOS, une mesure ISO ou une obligation légale. C'est ce qui rend les règles défendables face aux équipes.

## Suite

- **Module 3 — Accès et habilitations** : mise en œuvre concrète de MS-POL-02 (matrice des rôles, revue des accès sur un export avec anomalies, processus arrivées et départs).

---
*Entreprise et documents fictifs, réalisés dans un but d'apprentissage.*
