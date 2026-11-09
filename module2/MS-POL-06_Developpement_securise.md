# Politique de développement sécurisé

| Référence | MS-POL-06 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | CTO | Approbateur | RSSI |
| Date d'approbation | 01/12/2026 | Prochaine revue | 01/12/2027 |

## 1. Objet et périmètre

Intégrer la sécurité à chaque étape du développement de MediSoft Care et de MediSoft Patient, y compris lorsque le développement est confié à un prestataire.

**Mesures couvertes :** A.5.8, A.8.4, A.8.11, A.8.25 à A.8.33. **Obligations :** RGPD art. 25 (protection des données dès la conception), CRA (application mobile). **Constat EBIOS traité :** n° 11 (secrets en clair, pas de revue de code).

## 2. Cycle de développement sécurisé

| Étape | Exigences de sécurité | Preuve |
|---|---|---|
| **Conception** | Exigences issues de l'OWASP ASVS niveau 2 ; analyse de menaces pour toute fonctionnalité touchant aux données de santé ou à l'authentification ; avis du DPO si nouveau traitement | Fiche d'exigences, analyse de menaces |
| **Développement** | Règles de codage sécurisé (section 3) ; secrets uniquement dans AWS Secrets Manager | Historique Git |
| **Revue** | Revue de code par un second développeur obligatoire avant fusion ; branche principale protégée | Pull request approuvée |
| **Tests automatisés (CI)** | Analyse statique (SAST), analyse des dépendances (SCA) et génération du SBOM, détection de secrets, analyse des images de conteneurs ; une vulnérabilité critique bloque la fusion | Rapports de la CI |
| **Recette** | Analyse dynamique (DAST) sur la préproduction ; tests des droits d'accès | Rapport DAST |
| **Mise en production** | Uniquement via la CI/CD, après approbation d'un responsable différent de l'auteur ; possibilité de retour arrière | Ticket de changement |
| **Exploitation** | Suivi des vulnérabilités des dépendances ; pentest annuel externe | Rapport de pentest |

## 3. Règles de codage

- Valider toutes les entrées côté serveur ; utiliser des requêtes paramétrées (pas de concaténation SQL).
- Encoder les sorties pour prévenir les injections de script (XSS).
- Contrôler les autorisations à chaque requête côté serveur, jamais seulement dans l'interface.
- Ne jamais écrire de donnée de santé ni de secret dans les journaux applicatifs.
- Gérer les sessions de façon sécurisée : expiration après 15 minutes d'inactivité pour les professionnels de santé, cookies `Secure`, `HttpOnly` et `SameSite`.
- Journaliser les événements de sécurité : connexions, échecs, changements de droits, accès aux dossiers patients.

## 4. Gestion des environnements et des données de test

- Environnements séparés dans des comptes AWS distincts (MS-POL-05).
- **Interdiction d'utiliser des données réelles de patients hors production.** Les tests utilisent des jeux de données synthétiques ou anonymisés de façon irréversible, validés par le DPO.

## 5. Code source et chaîne d'approvisionnement

- Accès à GitHub par SSO avec MFA ; droits revus chaque trimestre ; accès des prestataires limités aux dépôts nécessaires et retirés en fin de mission.
- Dépendances : versions figées, mises à jour régulières, licences vérifiées.
- Un SBOM est produit à chaque version de MediSoft Patient (exigence CRA).

## 6. Développement externalisé

Tout prestataire de développement (comme celui de l'application mobile) doit, par contrat :

- respecter la présente politique ;
- livrer le code dans les dépôts de MediSoft, où il passe les mêmes contrôles automatiques et la même revue ;
- signaler sous 24 h toute vulnérabilité découverte ;
- accepter des audits de code.

## 7. Gestion des vulnérabilités du produit

- Délais de correction : critique 7 jours, élevée 30 jours, moyenne 90 jours.
- Une politique de divulgation coordonnée (adresse `security@` et fichier `security.txt`) permet aux chercheurs de signaler des vulnérabilités.
- Une vulnérabilité **activement exploitée** dans MediSoft Patient est signalée dans les délais du CRA (alerte sous 24 h) par le RSSI.

## 8. Indicateurs

- Part des fusions avec revue de code (cible : 100 %)
- Vulnérabilités critiques ouvertes de plus de 7 jours (cible : 0)
- Secrets détectés dans le code (cible : 0)

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/12/2026 | CTO | Création |
