# Politique de sécurité dans les relations avec les fournisseurs

| Référence | MS-POL-10 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité |
| Date d'approbation | 15/01/2027 | Prochaine revue | 15/01/2028 |

## 1. Objet et périmètre

Maîtriser les risques apportés par les fournisseurs, prestataires et outils SaaS, de leur sélection jusqu'à la fin du contrat. S'applique à tout tiers qui traite des informations de MediSoft ou accède à son système d'information.

**Mesures couvertes :** A.5.19 à A.5.23, A.8.30. **Obligations :** NIS2 art. 21.2.d (sécurité de la chaîne d'approvisionnement), RGPD art. 28 (sous-traitants), HDS v2.0 (sous-traitants de l'hébergeur), DORA art. 28 à 30 (exigences des clients assureurs, que MediSoft doit répercuter sur ses propres fournisseurs critiques).

**Pourquoi c'est important :** MediSoft ne peut pas être plus sûre que ses fournisseurs. Si AWS, GitHub ou un prestataire Ops est compromis, MediSoft l'est aussi.

## 2. Classement des fournisseurs par criticité

| Criticité | Critère | Exigences |
|---|---|---|
| **Tier 1 — Critique** | Traite des données de santé (C3) **ou** dispose d'un accès à la production | Questionnaire complet et preuves (certificats, rapports d'audit) ; clauses renforcées ; plan de sortie ; revue annuelle |
| **Tier 2 — Important** | Traite des données confidentielles (C2) | Questionnaire standard ; clauses standard ; revue tous les 2 ans |
| **Tier 3 — Standard** | Données publiques ou internes uniquement (C0, C1) | Vérification simple ; revue tous les 3 ans |

La criticité est calculée automatiquement dans le registre des fournisseurs à partir de ces deux critères.

## 3. Cycle de vie d'un fournisseur

| Étape | Action | Acteur |
|---|---|---|
| **1. Besoin** | Le demandeur décrit le service, les données concernées et les utilisateurs (check-list projet MS-MOD-01, étape « cadrage ») | Demandeur |
| **2. Classement** | Détermination de la criticité | RSSI |
| **3. Évaluation** | Questionnaire de sécurité adapté à la criticité, analyse des preuves, notation pondérée. Le DPO évalue la partie RGPD | RSSI + DPO |
| **4. Avis** | Favorable, favorable sous conditions ou défavorable. Une exigence bloquante non satisfaite entraîne un avis défavorable | RSSI |
| **5. Contrat** | Intégration des clauses de sécurité (MS-MOD-03) adaptées à la criticité | Juridique |
| **6. Mise en service** | Accès par SSO et MFA, comptes avec date d'expiration, inscription au registre | Resp. Ops |
| **7. Suivi** | Revue périodique, suivi des incidents et des changements (sous-traitants, localisation), collecte annuelle des attestations | RSSI |
| **8. Fin de contrat** | Restitution puis suppression des données avec attestation, retrait des accès (procédure de départ MS-PRO-03) | Propriétaire du contrat + Resp. Ops |

**Aucun outil SaaS ne peut être utilisé avec des données de l'entreprise sans être passé par les étapes 1 à 4.** Les outils trouvés en usage sans validation (« shadow IT ») sont évalués a posteriori ou bloqués.

## 4. Exigences bloquantes

Un fournisseur qui ne satisfait pas l'une des exigences suivantes ne peut pas être retenu pour le périmètre concerné :

- **Données de santé** : certification HDS couvrant les activités confiées, stockage dans l'EEE ;
- **Données personnelles** : contrat de sous-traitance conforme à l'art. 28 du RGPD ;
- **Outils d'IA** : engagement contractuel que les données de MediSoft ne servent pas à entraîner les modèles ;
- **Accès à la production** : authentification forte et accès traçable.

## 5. Fournisseurs critiques de MediSoft et répercussion de DORA

Les clients assureurs imposent à MediSoft des exigences issues de DORA : droit d'audit, notification des incidents, plans de continuité testés, stratégie de sortie. MediSoft ne peut tenir ces engagements que si ses propres fournisseurs Tier 1 les acceptent. Pour chaque fournisseur Tier 1, le RSSI vérifie donc :

- la localisation des données et des traitements, et l'information préalable en cas de changement ;
- les délais de notification des incidents, compatibles avec les engagements de MediSoft envers ses clients ;
- l'existence d'un plan de sortie réaliste et testé sur le papier.

## 6. Indicateurs

- Taux de fournisseurs Tier 1 évalués et à jour (cible : 100 %)
- Fournisseurs jamais évalués (cible : 0)
- Fournisseurs Tier 1 sans plan de sortie (cible : 0 fin 2027)
- Complétude contractuelle moyenne (cible : 100 %)

Situation au 20/01/2027 : voir le registre `Registre_fournisseurs_MediSoft.xlsx`.

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 15/01/2027 | RSSI | Création |
