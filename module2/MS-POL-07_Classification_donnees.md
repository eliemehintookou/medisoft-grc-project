# Politique de classification, de manipulation et de conservation de l'information

| Référence | MS-POL-07 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité (avis du DPO) |
| Date d'approbation | 01/12/2026 | Prochaine revue | 01/12/2027 |

## 1. Objet et périmètre

Protéger chaque information selon sa sensibilité, de sa création à sa destruction. S'applique à toutes les informations, quel que soit leur support.

**Mesures couvertes :** A.5.9, A.5.10, A.5.12 à A.5.14, A.5.33, A.7.14, A.8.10. **Obligations :** RGPD (art. 5, 9, 28.3.g et 32), secret médical, HDS.

## 2. Niveaux de classification

| Niveau | Définition | Exemples |
|---|---|---|
| **C0 — Public** | Diffusion libre, aucun impact | Site web, plaquettes commerciales, offres d'emploi |
| **C1 — Interne** | Réservé aux collaborateurs ; impact limité en cas de fuite | Politiques internes, procédures, organigramme |
| **C2 — Confidentiel** | Réservé aux personnes autorisées ; impact important | Contrats, données RH, code source, architecture, rapports d'audit, données personnelles hors santé |
| **C3 — Données de santé** | Données couvertes par le secret médical ; impact critique | Dossiers patients, documents médicaux, données de remboursement, sauvegardes de production |

En cas de doute, on retient le niveau le plus élevé. Le propriétaire de l'information (créateur ou responsable métier) fixe le niveau.

## 3. Règles de manipulation

| Règle | C0 | C1 | C2 | C3 |
|---|---|---|---|---|
| Marquage | Non | En pied de page | « Confidentiel » en en-tête | Pas de document bureautique : les données restent dans la plateforme |
| Stockage | Libre | Outils de l'entreprise | Espaces à accès restreint | Uniquement dans la plateforme de production, chiffrée, chez un hébergeur certifié HDS |
| Envoi par e-mail | Oui | Interne uniquement | Pièce jointe chiffrée | **Interdit** |
| Transfert vers un client ou partenaire | Libre | Avec accord du manager | Plateforme d'échange chiffrée | SFTP ou API chiffrée, sur demande documentée du client |
| Impression | Libre | Autorisée | Limitée, récupération immédiate | Interdite, sauf demande du client |
| Usage dans un outil d'IA externe | Oui | Non | Non | **Interdit** |

## 4. Durées de conservation

| Information | Durée | Base |
|---|---|---|
| Données de santé des clients | Fixée par le client (responsable de traitement) dans le contrat | RGPD art. 28 |
| Données après la fin d'un contrat client | Restitution au client puis suppression sous 90 jours | RGPD art. 28.3.g, contrat |
| Journaux d'accès aux dossiers patients | Durée fixée avec les clients (référence de travail : 1 an minimum) | Traçabilité HDS, recommandations CNIL |
| Journaux techniques et d'administration | 1 an | Investigation des incidents |
| Sauvegardes | 35 jours (quotidiennes), 12 mois (mensuelles) | MS-POL-04 |
| Dossiers RH | Selon les obligations légales du droit du travail | Code du travail |
| Contrats | Durée du contrat + 5 ans | Prescription civile |

## 5. Suppression et destruction

- En fin de contrat : restitution des données au client dans un format standard, puis suppression de la production et, à leur expiration, des sauvegardes. Un **procès-verbal de suppression** est remis au client.
- Supports physiques (disques, postes) : effacement sécurisé certifié ou destruction par un prestataire qui délivre un certificat.
- Documents papier C2 : broyeur ou bac de destruction sécurisé.

## 6. Inventaire

Le RSSI tient l'inventaire des actifs informationnels (A.5.9), avec pour chacun : propriétaire, niveau de classification, localisation, durée de conservation. La cartographie des flux de données de santé est maintenue avec le DPO.

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/12/2026 | RSSI | Création |
