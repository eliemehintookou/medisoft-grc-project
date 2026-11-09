# Playbooks de réponse aux incidents

| Référence | MS-MOD-04 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité |
| Date d'approbation | 01/02/2027 | Prochaine revue | 01/02/2028 |

> Fiches réflexes à appliquer avec la procédure MS-PRO-04. Elles indiquent **quoi faire, dans quel ordre et qui le fait**. Elles ne remplacent pas le jugement du gestionnaire de l'incident.

---

## Playbook 1 — Phishing (hameçonnage)

**Déclencheurs :** message signalé par un collaborateur, alerte de la messagerie, clic détecté.

| Étape | Action | Qui |
|---|---|---|
| 1 | Qualifier le message avec l'arbre de qualification (MS-ENR-04) | Analyste (RSSI ou Ops) |
| 2 | Chercher les autres destinataires du même message (même expéditeur, même objet ou même lien) | Ops |
| 3 | Supprimer le message de toutes les boîtes ; bloquer l'expéditeur, le domaine et les liens | Ops |
| 4 | Identifier qui a **cliqué** (journaux du proxy ou du filtrage DNS) et qui a **saisi ses identifiants** (connexions suspectes dans Entra ID) | Ops |
| 5 | **Si identifiants saisis :** appliquer immédiatement le playbook 4 (compromission de compte) | Ops + RSSI |
| 6 | **Si pièce jointe ouverte :** isoler le poste avec l'EDR, analyse, réinstallation si besoin | Support IT |
| 7 | Remercier la personne qui a signalé ; informer l'ensemble des collaborateurs si la campagne est large | RSSI |

**Gravité :** G1 si non cliqué ; G2 si cliqué sans saisie ; G3 si identifiants saisis ; G4 si compte administrateur ou données de santé exposées.

---

## Playbook 2 — Rançongiciel

**Déclencheurs :** fichiers chiffrés, message de rançon, alerte EDR de chiffrement massif, indisponibilité soudaine de serveurs.

| Étape | Action | Qui |
|---|---|---|
| 1 | **Isoler, ne pas éteindre** : déconnecter du réseau les machines touchées (EDR, retrait du réseau), mais les laisser allumées pour préserver la mémoire | Ops |
| 2 | Déclencher la **cellule de crise** (G4) et ouvrir la main courante | RSSI → DG |
| 3 | Protéger les sauvegardes : vérifier que le compte de sauvegarde isolé et le verrouillage des sauvegardes sont intacts ; couper les accès des administrateurs au compte de sauvegarde | Resp. Ops |
| 4 | Désactiver les comptes à privilèges suspects ; changer les secrets et les clés d'accès | Ops |
| 5 | Identifier le point d'entrée et le périmètre (journaux, EDR, CloudTrail) avant toute restauration, pour ne pas restaurer un système encore compromis | Ops + prestataire de réponse à incident |
| 6 | Notifications : clients, ANSSI (NIS2), assureurs clients (DORA), CNIL si données de MediSoft, assureur cyber ; **plainte sous 72 h** | DPO, RSSI, DG |
| 7 | **Ne pas payer la rançon** (recommandation de l'ANSSI) : décision réservée à la cellule de crise | DG |
| 8 | Restaurer depuis des sauvegardes saines, par ordre de priorité métier ; surveillance renforcée | Ops |
| 9 | Retour d'expérience sous 15 jours | RSSI |

**Contacts utiles :** CERT-FR, CERT Santé, Cybermalveillance.gouv.fr (liste de prestataires), prestataire de réponse à incident contractualisé.

---

## Playbook 3 — Fuite de données ou accès illégitime aux données

**Déclencheurs :** données de MediSoft trouvées en ligne, accès anormal aux dossiers patients, connexion d'une personne non autorisée, envoi au mauvais destinataire.

| Étape | Action | Qui |
|---|---|---|
| 1 | Couper l'accès en cause : compte, partage, lien public, clé d'API | Ops |
| 2 | Préserver les preuves : exports des journaux d'accès, captures horodatées | Ops |
| 3 | Établir le périmètre : quelles données, combien de personnes, quels clients, depuis quand | Ops + DPO |
| 4 | **Le DPO qualifie la violation** : nature des données (santé ?), volume, risque pour les personnes, possibilité de les identifier | DPO |
| 5 | Notifier selon MS-PRO-04 §6 : **les clients concernés sans délai**, puis la CNIL sous 72 h si MediSoft est responsable de traitement | DPO + RSSI |
| 6 | Demander le retrait des données publiées ; obtenir une attestation de suppression si le destinataire est identifié | Juridique |
| 7 | Inscrire au registre des violations, **même en l'absence de notification**, avec la justification | DPO |

---

## Playbook 4 — Compromission de compte

**Déclencheurs :** identifiants saisis sur un site de phishing, connexion depuis un pays inhabituel, demandes MFA non sollicitées, règle de transfert de messagerie suspecte, connexion après un départ.

| Étape | Action | Qui |
|---|---|---|
| 1 | Révoquer toutes les sessions, réinitialiser le mot de passe, réinitialiser les méthodes MFA | Ops |
| 2 | Vérifier les modifications faites par l'attaquant : règles de transfert de messagerie, nouvelles méthodes MFA, applications autorisées (OAuth), jetons GitHub, clés d'accès AWS | Ops |
| 3 | Analyser ce qui a été consulté ou téléchargé pendant la période de compromission (Entra ID, messagerie, SharePoint, GitHub, MediSoft Care) | Ops + RSSI |
| 4 | Si le compte avait des accès à privilèges : vérifier les actions d'administration (CloudTrail, journaux d'audit Entra ID) et changer les secrets accessibles | Ops |
| 5 | Si des données personnelles ont été consultées : appliquer le playbook 3 | DPO |
| 6 | Rappel individuel à la personne, sans culpabiliser ; vérifier qu'elle utilise une clé FIDO2 si elle a des accès sensibles | RSSI |

**Cas particulier — connexion après un départ :** traiter comme une compromission, même si l'auteur est l'ancien titulaire du compte : l'accès n'est plus autorisé. Voir l'exemple INC-2026-014 (MS-ENR-05).

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/02/2027 | RSSI | Création |
