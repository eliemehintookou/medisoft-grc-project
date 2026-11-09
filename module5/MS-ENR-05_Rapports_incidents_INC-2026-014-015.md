# Rapports d'incident INC-2026-014 et INC-2026-015

| Classification | C2 — Confidentiel |
|---|---|
| Origine | Revue des accès du T4 2026 (module 3, anomalies F-001 et F-003) |
| Gestionnaire | RSSI |

> Ces deux incidents montrent qu'une anomalie de conformité (un compte resté actif) peut cacher un véritable accès illégitime.

---

## INC-2026-014 — Connexion d'un ancien développeur après son départ

### Synthèse

| Élément | Valeur |
|---|---|
| Détection | 15/12/2026, revue des accès (F-001) |
| Gravité | **G3 — Majeure** (accès illégitime avéré) |
| Période concernée | Connexion unique le 02/10/2026, de 21 h 12 à 21 h 31 |
| Violation de données personnelles | **Oui**, risque jugé faible : inscrite au registre, **non notifiée** |
| Statut | Clos le 08/01/2027 |

### Chronologie

| Date et heure | Événement |
|---|---|
| 30/09/2026 | Départ du développeur. La DRH n'informe pas l'IT : le compte reste actif |
| 02/10/2026, 21 h 12 | Connexion au compte depuis une adresse IP d'un fournisseur d'accès grand public en France, avec MFA réussie (téléphone personnel toujours enregistré) |
| 02/10/2026, 21 h 15 – 21 h 31 | Consultation de la messagerie ; téléchargement de 3 pièces jointes |
| 15/12/2026, 10 h 40 | Détection lors de la revue des accès ; ouverture de l'incident |
| 15/12/2026, 10 h 52 | Compte désactivé, sessions révoquées, méthodes MFA supprimées |
| 15/12/2026 – 18/12/2026 | Investigation : journaux Entra ID, messagerie, GitHub et AWS |
| 19/12/2026 | Entretien téléphonique avec l'ancien salarié, avec la DRH |
| 08/01/2027 | Clôture après réception de l'attestation de suppression |

### Investigation

- **Ce qui a été consulté :** uniquement la messagerie de l'intéressé. Les 3 pièces jointes téléchargées sont ses propres bulletins de paie et un document de mutuelle.
- **Ce qui n'a pas été consulté :** aucun accès à GitHub (compte retiré au départ), à AWS ou à MediSoft Care. Le rôle de développeur ne donne aucun accès aux données de santé.
- **Explication de l'intéressé :** il voulait récupérer ses documents personnels. Il a signé une attestation de suppression de toute autre information de MediSoft en sa possession.

### Analyse au titre du RGPD

La messagerie contenait des échanges internes avec des noms et adresses de collègues, consultables pendant la session : c'est une **violation de données personnelles**, MediSoft étant responsable de traitement pour ces données. Le DPO a évalué le risque pour les personnes comme **improbable** : données professionnelles courantes, aucune donnée de santé ou sensible, aucun téléchargement en dehors des documents personnels de l'intéressé, attestation de suppression obtenue. **Pas de notification à la CNIL** (RGPD art. 33.1), mais **inscription au registre des violations** avec cette justification (art. 33.5).

### Cause racine et actions

| Cause | Action | Statut |
|---|---|---|
| Départ non transmis par la DRH | Synchronisation automatique SIRH → Entra ID (MS-PRO-03 v1.1) | En cours (T1 2027) |
| Téléphone personnel conservé comme méthode MFA | Suppression des méthodes MFA lors de la désactivation ; clés FIDO2 de l'entreprise pour les accès sensibles | Fait |
| Pas de contrôle régulier des départs | Contrôle mensuel automatique (règles R01 à R04) | Fait |

---

## INC-2026-015 — Clonage d'un dépôt de code par une prestataire après sa mission

### Synthèse

| Élément | Valeur |
|---|---|
| Détection | 15/12/2026, revue des accès (F-003 et F-010) |
| Gravité | **G3 — Majeure** (accès illégitime au code source) |
| Période concernée | 18/09/2026 (fin de mission le 30/06/2026) |
| Violation de données personnelles | **Non** : code source sans donnée personnelle |
| Statut | Clos le 12/01/2027 |

### Ce qui s'est passé

Le 18/09/2026, la prestataire s'est connectée à son compte invité, resté actif, puis a **cloné le dépôt `mobile-app`** sur GitHub. L'investigation a montré que l'historique du dépôt contenait **une clé d'API d'un service d'envoi de notifications**, supprimée du code en 2025 mais toujours valide.

### Actions

| Action | Date |
|---|---|
| Compte invité désactivé, accès GitHub retiré | 15/12/2026 |
| **Clé d'API révoquée et remplacée** ; vérification des journaux du service de notifications : aucun usage anormal | 15/12/2026 |
| Contact avec la société de la prestataire : le clonage visait à préparer une offre de maintenance. Attestation de suppression de la copie obtenue | 07/01/2027 |
| Rappel contractuel (clause de confidentialité, MS-MOD-03 C1) | 07/01/2027 |
| Analyse de l'historique de tous les dépôts avec un outil de détection de secrets : 2 autres secrets trouvés et changés | 11/01/2027 |

### Enseignements

1. **Un compte « oublié » n'est pas un risque théorique** : il a été utilisé dans les deux cas.
2. **Supprimer un secret du code ne suffit pas** : il reste dans l'historique Git. Tout secret publié doit être **révoqué**, pas seulement effacé (MS-POL-06).
3. **Les comptes externes doivent expirer automatiquement** à la fin du contrat (MS-PRO-03 v1.1).

---

## Retour d'expérience commun (08/01/2027)

Participants : RSSI, DPO, DRH, Resp. Ops, CTO. Ces deux incidents justifient à eux seuls les chantiers PA-04 (identités et accès) et PA-14 (développement sécurisé) du plan d'action. Ils seront présentés au comité sécurité du T1 2027 comme exemple concret de l'utilité des revues d'accès.
