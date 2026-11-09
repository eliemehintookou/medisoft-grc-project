# Programme de sensibilisation et de formation à la sécurité — 2027

| Référence | MS-PRO-05 | Version | 1.0 |
|---|---|---|---|
| Classification | C1 — Interne | Statut | Approuvé |
| Propriétaire | RSSI | Approbateur | Comité sécurité (avec la DRH) |
| Date d'approbation | 01/02/2027 | Prochaine revue | 01/12/2027 |

## 1. Pourquoi ce programme

Avant 2027, MediSoft n'avait **aucune sensibilisation** (constat EBIOS n° 10, mesure A.6.3 au niveau 0). Or la plupart des attaques commencent par un humain : un clic, un mot de passe réutilisé, un virement frauduleux. NIS2 impose aussi aux dirigeants de **suivre une formation** (art. 20) et aux entités de former leur personnel (art. 21).

**Objectif 2027 (PSSI, objectif O3) :** au moins 95 % des collaborateurs formés.

## 2. Publics et contenus

| Public | Contenu | Format | Durée | Fréquence |
|---|---|---|---|---|
| **Tous les collaborateurs** | Bases : phishing, mots de passe et MFA, données de santé, signalement, télétravail | E-learning (CyberQuiz) + quiz | 45 min | Annuelle |
| **Nouveaux arrivants** | Charte, règles essentielles, signalement | Session d'accueil avec le RSSI | 30 min | À l'arrivée, avant tout accès aux données de santé |
| **Direction** | Responsabilités des dirigeants (NIS2), gestion de crise, enjeux réglementaires | Atelier avec le RSSI + exercice de crise | 2 h | Annuelle |
| **Support N2** | Secret médical, accès aux dossiers patients sur ticket, usurpation de clients | Atelier pratique avec cas réels | 1 h | Annuelle |
| **Développeurs et Ops** | OWASP Top 10, secrets dans le code, sécurité AWS, revue de code | Atelier technique + exercices | 3 h | Annuelle |
| **Finance, achats, RH** | Fraude au président, fraude au RIB, faux candidats | Atelier avec cas réels (MS-ENR-04) | 1 h | Annuelle |

## 3. Calendrier 2027

| Mois | Action |
|---|---|
| Janvier | Campagne de phishing simulé n° 1 (mesure de départ) ; lancement de l'e-learning |
| Février | Newsletter cyber n° 1 ; atelier Finance / Achats / RH |
| Mars | Atelier direction + exercice de crise sur table (rançongiciel) |
| Avril | Campagne de phishing simulé n° 2 ; atelier support N2 |
| Mai | Newsletter n° 2 ; atelier développeurs et Ops |
| Juin | Relance des personnes non formées ; bilan semestriel au comité sécurité |
| Juillet | Campagne de phishing simulé n° 3 |
| Septembre | Newsletter n° 3 |
| Octobre | **Mois européen de la cybersécurité** : quiz interne, conférence courte |
| Novembre | Campagne de phishing simulé n° 4 |
| Décembre | Bilan annuel ; préparation du programme 2028 |

Les alertes de sécurité sont diffusées à tout moment, en cas de menace en cours (exemple : `communication/Alerte_securite_2027-01.md`).

## 4. Règles des campagnes de phishing simulé

- Le CSE est informé du principe des campagnes, sans les dates.
- **Aucune sanction** : le but est d'apprendre, pas de piéger.
- Une personne qui clique voit immédiatement une page explicative de 2 minutes.
- Les résultats sont présentés **par service, jamais nominativement**, sauf au RSSI pour proposer un accompagnement individuel.
- Les scénarios reproduisent les menaces réelles observées (signalements, alertes du CERT Santé).

## 5. Résultats de la campagne n° 1 (janvier 2027)

Scénario : faux message « partage de document » imitant Microsoft, envoyé aux 85 collaborateurs.

| Indicateur | Résultat | Cible fin 2027 |
|---|---|---|
| Taux de clic | 24 % (20 personnes) | < 10 % |
| Saisie des identifiants | 9 % (8 personnes) | < 3 % |
| **Taux de signalement** | 18 % (15 personnes) | > 50 % |
| Délai du premier signalement | 11 minutes | < 5 minutes |

**Analyse :** le taux de signalement compte autant que le taux de clic : plus les collaborateurs signalent vite, plus l'équipe sécurité peut supprimer le message chez les autres avant qu'ils cliquent. Les services les plus exposés sont le Commercial et le Support, qui reçoivent beaucoup de messages externes : ils sont prioritaires pour les ateliers.

## 6. Indicateurs suivis

| Indicateur | Source | Cible 2027 |
|---|---|---|
| Collaborateurs ayant suivi l'e-learning | CyberQuiz | ≥ 95 % |
| Nouveaux arrivants sensibilisés avant leur accès aux données de santé | DRH + RSSI | 100 % |
| Dirigeants formés (NIS2) | Feuille de présence | 100 % |
| Taux de clic aux campagnes simulées | CyberQuiz | < 10 % |
| Taux de signalement | CyberQuiz + messagerie | > 50 % |
| Messages réels signalés par mois | MS-ENR-04 | En hausse |

Ces indicateurs alimentent le tableau de bord sécurité (module 6).

## Historique

| Version | Date | Auteur | Modification |
|---|---|---|---|
| 1.0 | 01/02/2027 | RSSI | Création |
