# Procédure de gestion des incidents de sécurité

| Référence | MS-PRO-04 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité |
| Date d'approbation | 01/02/2027 | Prochaine revue | 01/02/2028 |

## 1. Objet et périmètre

Détecter, qualifier, traiter et notifier les incidents de sécurité de façon rapide et maîtrisée, puis en tirer des enseignements.

**Mesures couvertes :** A.5.5, A.5.24 à A.5.28, A.6.8. **Obligations :** RGPD art. 33 et 34, NIS2 art. 23 (à la promulgation de la loi française), engagements DORA envers les clients assureurs, CRA art. 14 (application mobile), clauses contractuelles des clients.

**Définitions**
- **Événement** : fait observé qui pourrait concerner la sécurité (alerte, message suspect signalé, comportement anormal).
- **Incident** : événement qui porte atteinte, ou risque de porter atteinte, à la confidentialité, à l'intégrité ou à la disponibilité des informations ou des services.
- **Violation de données personnelles** : incident qui entraîne la destruction, la perte, l'altération, la divulgation ou l'accès non autorisé à des données personnelles (RGPD art. 4.12).

## 2. Signaler

Tout collaborateur qui constate un événement suspect le signale **immédiatement**, sans chercher à enquêter lui-même :

- bouton « Signaler » de la messagerie pour un message suspect ;
- `securite@medisoft.example` ou le canal Slack `#securite-signalement` ;
- **en dehors des heures ouvrées ou en cas d'urgence** : astreinte Ops, au numéro affiché sur l'intranet.

Les alertes techniques (SIEM, GuardDuty, EDR) arrivent directement à l'astreinte Ops et au RSSI.

> Signaler une erreur (clic sur un lien piégé, envoi au mauvais destinataire) n'est jamais sanctionné. La cacher peut l'être (MS-POL-09).

## 3. Grille de gravité

| Gravité | Critères (un seul suffit) | Exemples | Délai de prise en charge |
|---|---|---|---|
| **G4 — Critique** | Données de santé divulguées ou altérées ; MediSoft Care indisponible pour tous les clients ; rançongiciel ; compromission d'un compte administrateur | Base de production exfiltrée ; chiffrement des serveurs | **Immédiat**, cellule de crise |
| **G3 — Majeure** | Données personnelles exposées sans données de santé ; service dégradé pour plusieurs clients ; compromission d'un compte utilisateur avec accès sensible ; accès illégitime avéré | Ancien salarié connecté après son départ ; vulnérabilité critique exploitée | Sous 1 h |
| **G2 — Modérée** | Incident maîtrisé sans fuite de données avérée ; poste infecté isolé | Clic sur un lien de phishing sans saisie d'identifiants ; maliciel bloqué par l'EDR | Sous 4 h ouvrées |
| **G1 — Faible** | Événement sans impact | Spam, phishing signalé et non cliqué | Sous 1 jour ouvré |

Le niveau peut être réévalué à tout moment pendant le traitement.

## 4. Organisation

| Rôle | Qui | Responsabilité |
|---|---|---|
| Gestionnaire de l'incident | RSSI (suppléant : Resp. Ops) | Pilote le traitement, tient la main courante, décide des notifications avec le DPO |
| Équipe technique | Ops, CTO, développeurs concernés | Investigation, confinement, remédiation |
| DPO | DPO | Évalue s'il s'agit d'une violation de données personnelles et le risque pour les personnes |
| Cellule de crise (G4) | DG, RSSI, DPO, CTO, Resp. Ops, communication, juridique | Décisions stratégiques, communication aux clients, aux autorités et à la presse |

**Main courante** : dès l'ouverture, toutes les actions et décisions sont notées avec leur heure. C'est indispensable pour les notifications, l'assurance, une éventuelle plainte et le retour d'expérience.

## 5. Phases de traitement

| Phase | Objectif | Actions principales |
|---|---|---|
| **1. Qualification** | Est-ce un incident ? Quelle gravité ? | Grille de gravité ; arbre de qualification pour les messages signalés (MS-ENR-04) ; ouverture d'un ticket INC-AAAA-NNN |
| **2. Confinement** | Empêcher l'extension | Isoler le poste (EDR), désactiver le compte, révoquer les sessions et jetons, bloquer une adresse IP ou un domaine. **Préserver les preuves avant toute action destructive** |
| **3. Investigation** | Comprendre ce qui s'est passé | Analyse des journaux (Entra ID, CloudTrail, application, accès aux dossiers patients), chronologie, périmètre des données touchées |
| **4. Éradication** | Supprimer la cause | Correctif, suppression du maliciel, changement des secrets exposés |
| **5. Rétablissement** | Revenir à la normale | Restauration depuis une sauvegarde saine (MS-POL-04), surveillance renforcée |
| **6. Clôture et RETEX** | Ne pas revivre l'incident | Rapport d'incident, retour d'expérience pour G3 et G4 sous 15 jours, actions inscrites au plan d'action |

Les actions détaillées par type d'incident figurent dans les playbooks (MS-MOD-04).

## 6. Notifications

C'est l'étape la plus exposée juridiquement. **Le DPO et le RSSI décident ensemble ; le DG valide pour G3 et G4.**

| Destinataire | Quand | Délai | Base | Qui notifie |
|---|---|---|---|---|
| **Clients établissements de santé** (responsables de traitement) | Violation touchant les données de leurs patients | **Sans délai** (engagement contractuel : 24 h) | RGPD art. 33.2 (sous-traitant) | DPO + RSSI |
| **CNIL** | Violation des données dont MediSoft est responsable de traitement (salariés, prospects, comptes de l'application patient), sauf si le risque pour les personnes est improbable | **72 h** après en avoir eu connaissance | RGPD art. 33 | DPO |
| **Personnes concernées** | Même périmètre, si risque élevé pour leurs droits | Dans les meilleurs délais | RGPD art. 34 | DPO |
| **ANSSI** | Incident important, une fois la loi de transposition de NIS2 en vigueur et MediSoft enregistrée | Alerte **24 h**, notification **72 h**, rapport final **1 mois** | NIS2 art. 23 | RSSI |
| **Clients assureurs** | Incident affectant le module tiers payant | **4 h** pour un incident majeur (avenant DORA) | Contrat (DORA art. 30) | RSSI |
| **CSIRT désigné et ENISA** (plateforme unique de signalement) | Vulnérabilité activement exploitée ou incident grave touchant l'application mobile | Alerte **24 h**, notification **72 h**, rapport final selon le cas | CRA art. 14 | RSSI |
| **Assureur cyber** | Tout incident G3 ou G4 | Selon le contrat | Contrat d'assurance | DG |
| **Police ou gendarmerie** (plainte) | Acte malveillant (intrusion, rançongiciel, fraude) | **Sous 72 h** pour conserver l'indemnisation de l'assurance après une cyberattaque | Code des assurances (loi LOPMI) | DG ou juridique |
| **Collaborateurs** | Pour les consignes à appliquer | Dès que nécessaire | — | RSSI |

**Rappels importants**

- Le délai court à partir du moment où MediSoft **a connaissance** de l'incident, pas de la fin de l'enquête : on notifie ce qu'on sait, puis on complète.
- Les établissements de santé clients ont eux-mêmes l'obligation de déclarer leurs incidents graves de sécurité (Code de la santé publique, art. L.1111-8-2) : MediSoft leur fournit les éléments nécessaires.
- **Toute violation de données personnelles est inscrite au registre des violations**, même si elle n'est pas notifiée (RGPD art. 33.5), avec la justification de la décision de ne pas notifier.

## 7. Registre des incidents

| Champ | Contenu |
|---|---|
| N° | INC-AAAA-NNN |
| Dates | Détection, qualification, confinement, clôture |
| Description | Ce qui s'est passé, source de détection |
| Gravité | G1 à G4 |
| Données touchées | Catégories, volume, personnes concernées |
| Violation de données personnelles | Oui / Non, avec justification |
| Notifications | Destinataires, dates, références |
| Cause racine | — |
| Actions | Correctives et préventives, avec responsable et échéance |

**Registre 2026 (extrait)**

| N° | Date | Description | Gravité | Violation de données | Notifications | Statut |
|---|---|---|---|---|---|---|
| INC-2026-014 | 15/12/2026 | Connexion d'un ancien développeur à sa messagerie après son départ | G3 | Oui, risque faible : inscrite au registre, non notifiée (voir rapport) | Aucune obligatoire | Clos le 08/01/2027 |
| INC-2026-015 | 15/12/2026 | Clonage du dépôt de l'application mobile par une prestataire après la fin de sa mission | G3 | Non (code source sans données personnelles) | Aucune obligatoire | Clos le 12/01/2027 |

## 8. Exercices

- **Exercice sur table annuel** de la cellule de crise : scénario de rançongiciel sur MediSoft Care.
- **Test semestriel** de l'astreinte et de l'annuaire des contacts.

## 9. Indicateurs

- Délai moyen de qualification par gravité
- Part des notifications effectuées dans les délais (cible : 100 %)
- Nombre d'incidents G3 et G4 par trimestre
- Part des RETEX réalisés sous 15 jours (cible : 100 %)

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/02/2027 | RSSI | Création |
