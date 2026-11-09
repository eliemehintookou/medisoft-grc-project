# Politique des postes de travail, des mobiles et du télétravail

| Référence | MS-POL-08 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité |
| Date d'approbation | 01/12/2026 | Prochaine revue | 01/12/2027 |

## 1. Objet et périmètre

Sécuriser les postes de travail et les téléphones qui accèdent au système d'information, au bureau comme en télétravail.

**Mesures couvertes :** A.6.7, A.7.7, A.7.9, A.7.10, A.8.1, A.8.7, A.8.18, A.8.23.

## 2. Postes de travail

| Exigence | Règle |
|---|---|
| Gestion | Tout poste (Windows ou Mac) est enrôlé dans le MDM (Microsoft Intune) ; un poste non conforme ne peut pas se connecter aux outils de l'entreprise |
| Chiffrement | Disque chiffré (BitLocker ou FileVault), clé de secours stockée dans le MDM |
| Protection | EDR installé et actif ; pare-feu activé |
| Mises à jour | Correctifs du système appliqués automatiquement sous 14 jours (7 jours pour une faille critique) |
| Droits | Pas de droits d'administrateur local ; élévation ponctuelle sur demande |
| Verrouillage | Automatique après 5 minutes d'inactivité |
| Supports amovibles | Stockage USB bloqué, sauf dérogation |
| Logiciels | Installation depuis le catalogue de l'entreprise uniquement |
| Navigation | Filtrage DNS des sites malveillants |
| Équipements personnels | Interdits pour accéder aux données C2 et C3 ; messagerie et outils collaboratifs autorisés sur téléphone personnel uniquement via une application gérée |

## 3. Télétravail

- Accès au système d'information uniquement depuis un poste de l'entreprise conforme.
- Accès aux outils internes via SSO avec MFA ; accès aux environnements techniques via le VPN de l'entreprise.
- Réseaux Wi-Fi publics : uniquement avec le VPN activé.
- Travail dans un lieu où l'écran n'est pas visible par des tiers ; filtre de confidentialité fourni sur demande.
- Aucune impression de documents C2 ou C3 au domicile.

## 4. Bureau propre et écran vide

- Aucun document C2 laissé sur un bureau en fin de journée.
- Session verrouillée à chaque absence (Windows + L, Ctrl + Cmd + Q).

## 5. Perte ou vol

Toute perte ou vol d'un poste ou d'un téléphone est signalé **immédiatement** au support et au RSSI. Le poste est alors bloqué et effacé à distance via le MDM.

## 6. Indicateurs

- Part des postes conformes dans le MDM (cible : 100 %)
- Part des postes chiffrés (cible : 100 %)
- Délai moyen d'application des correctifs critiques

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/12/2026 | RSSI | Création |
