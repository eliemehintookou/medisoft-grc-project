# Politique de sécurité du cloud

| Référence | MS-POL-05 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité |
| Date d'approbation | 01/12/2026 | Prochaine revue | 01/12/2027 |

## 1. Objet et périmètre

Encadrer l'usage d'AWS (infrastructure) et des services SaaS (outils internes).

**Mesures couvertes :** A.5.23, A.8.9, A.8.20, A.8.22, A.8.31, A.8.15, A.8.16. **Obligations :** HDS v2.0 (stockage dans l'EEE), DORA (réversibilité). **Constats EBIOS traités :** n° 5 (réseau à plat) et n° 6 (journalisation partielle).

## 2. Responsabilité partagée

| Domaine | AWS | MediSoft |
|---|---|---|
| Datacenters, matériel, réseau physique | ✔ | |
| Hyperviseur | ✔ | |
| Systèmes d'exploitation des instances | | ✔ |
| Configuration des services (IAM, réseau, chiffrement) | | ✔ |
| Données et accès aux données | | ✔ |
| Application MediSoft Care | | ✔ |
| Certification HDS | Activités 1 à 4 | Activités 5 et 6 |

Les attestations d'AWS (ISO 27001, HDS, SOC 2) sont téléchargées chaque année depuis AWS Artifact et conservées comme preuve.

## 3. Règles

**Organisation des comptes**
- Comptes séparés via AWS Organizations : `production`, `preproduction`, `developpement`, `securite` (journaux), `sauvegarde`.
- Aucune donnée de santé réelle hors du compte de production.

**Localisation**
- Régions autorisées : **eu-west-3 (Paris)** pour la production, une seconde région de l'EEE pour la réplication. Toute autre région est bloquée par une règle d'organisation (SCP).

**Réseau**
- Bases et serveurs applicatifs dans des sous-réseaux privés, sans adresse IP publique.
- Seuls le répartiteur de charge et le pare-feu applicatif (WAF) sont exposés à Internet.
- Aucun port d'administration (SSH, RDP) ouvert sur Internet : l'administration passe par AWS Systems Manager Session Manager.

**Configuration**
- Toute l'infrastructure est décrite en code (Terraform), revue et déployée par la CI/CD.
- Règles de conformité AWS Config et AWS Security Hub (référentiel CIS AWS Foundations) activées ; toute dérive génère une alerte.

**Journalisation et surveillance**
- CloudTrail activé sur toutes les régions et tous les comptes, centralisé dans le compte `securite`, protégé contre la modification et conservé 1 an.
- GuardDuty activé sur tous les comptes ; alertes envoyées au SIEM.
- Alertes de facturation et de budget pour détecter un usage anormal.

**Services SaaS internes**
- Tout nouvel outil SaaS est évalué avant usage (check-list du module 4) et validé par le RSSI ; le DPO est consulté s'il traite des données personnelles.
- L'accès se fait par SSO avec MFA.

## 4. Réversibilité

Un plan de sortie est maintenu pour AWS : export des données dans un format standard, documentation de l'infrastructure en Terraform, estimation du délai de migration vers un autre hébergeur certifié HDS. Il est revu chaque année (exigence DORA des clients assureurs).

## 5. Indicateurs

- Score de conformité AWS Security Hub (cible : ≥ 90 %)
- Nombre de ressources exposées publiquement sans justification (cible : 0)
- Alertes GuardDuty critiques traitées en moins de 24 h

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/12/2026 | RSSI | Création |
