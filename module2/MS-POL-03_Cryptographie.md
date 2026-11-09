# Politique de cryptographie et de gestion des clés

| Référence | MS-POL-03 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité |
| Date d'approbation | 01/12/2026 | Prochaine revue | 01/12/2027 |

## 1. Objet et périmètre

Fixer les règles d'usage du chiffrement pour protéger la confidentialité et l'intégrité des données, en particulier des données de santé.

**Mesures couvertes :** A.8.24, A.5.14. **Obligations :** RGPD art. 32, référentiel HDS v2.0. **Constats EBIOS traités :** n° 3 (chiffrement au repos non généralisé) et n° 4 (TLS interne).

## 2. Règles de chiffrement

| Situation | Exigence |
|---|---|
| Bases de données (RDS) | Chiffrement au repos activé, clé KMS gérée par MediSoft (*customer managed key*) |
| Stockage objet (S3) | Chiffrement SSE-KMS par défaut, blocage de l'accès public sur tous les buckets |
| Volumes (EBS) et snapshots | Chiffrement activé par défaut au niveau du compte |
| Sauvegardes | Chiffrées avec une clé distincte de celle de la production |
| Flux externes (clients, mobile, API) | TLS 1.2 minimum, TLS 1.3 privilégié ; HSTS activé |
| Flux internes (entre services, vers la base) | TLS obligatoire, y compris dans le VPC |
| Échanges de fichiers avec les clients | Plateforme d'échange chiffrée ou SFTP ; **e-mail interdit pour les données de santé** |
| Postes de travail | Disque chiffré (BitLocker ou FileVault) |
| Application mobile | Données locales stockées dans le stockage sécurisé du système (Keychain / Keystore) |

## 3. Algorithmes autorisés

| Usage | Autorisé | Interdit |
|---|---|---|
| Chiffrement symétrique | AES-256 (modes GCM ou XTS) | DES, 3DES, RC4 |
| Chiffrement asymétrique | RSA ≥ 3072 bits, ECC (P-256 ou supérieur, Curve25519) | RSA < 2048 bits |
| Hachage | SHA-256 ou supérieur | MD5, SHA-1 |
| Mots de passe stockés | Argon2id ou bcrypt avec sel | Hachage simple, chiffrement réversible |
| Protocoles | TLS 1.2 et 1.3, SSH v2 | SSL, TLS 1.0 et 1.1 |

Ces choix s'appuient sur les recommandations de l'ANSSI et sont revus chaque année.

## 4. Gestion des clés

- Les clés sont créées et stockées dans **AWS KMS** ; aucune clé privée ne doit apparaître dans le code, un ticket ou un e-mail.
- Rotation automatique annuelle des clés KMS ; rotation immédiate en cas de suspicion de compromission.
- Séparation des clés par environnement (prod, préprod, dev) et par usage (données, sauvegardes, journaux).
- Seuls les rôles de service ont le droit d'utiliser les clés ; l'administration des clés est réservée au Resp. Ops, sous contrôle du RSSI.
- La suppression d'une clé exige une période d'attente de 30 jours et l'accord du RSSI.
- Les certificats TLS sont gérés par AWS Certificate Manager et renouvelés automatiquement ; leur expiration est surveillée.

## 5. Contrôle

- Contrôle automatique et continu (AWS Config) : toute ressource non chiffrée génère une alerte.
- Scan TLS trimestriel des points d'accès externes.
- **Indicateur :** part des ressources de stockage chiffrées (cible : 100 % au 31/03/2027).

## 6. Exceptions

Toute exception passe par la procédure de dérogation MS-PRO-01 (voir l'exemple DER-2026-001).

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/12/2026 | RSSI | Création |
