# Étude comparative — Comment tester la sécurité de MediSoft ?

| Référence | MS-ENR-03 | Classification | C1 — Interne |
|---|---|---|---|
| Date | 20/01/2027 | Auteur | RSSI |
| Destinataires | Comité sécurité | Objet | Choisir les prestations de test de sécurité pour 2027-2028 |

## 1. Question posée

Le comité sécurité doit choisir comment vérifier la sécurité de MediSoft Care. Plusieurs types de prestations existent sur le marché : elles ne répondent pas au même besoin et n'ont pas le même coût. Cette étude les compare pour proposer une combinaison adaptée à la maturité de MediSoft.

## 2. Comparatif des approches

Coût relatif : € (faible) à €€€€ (très élevé). Les montants exacts sont à obtenir par consultation : ils varient fortement selon le périmètre et le prestataire.

| Approche | Ce que c'est | Avantages | Limites | Coût relatif | Pour MediSoft |
|---|---|---|---|---|---|
| **Scan de vulnérabilités automatisé** | Outil qui recherche en continu les failles connues (versions obsolètes, mauvaises configurations) | Continu, peu coûteux, couvre tout le parc | Ne trouve pas les failles de logique (ex. accès aux dossiers d'une autre clinique) ; faux positifs | € | **Oui, dès maintenant** (gestion des vulnérabilités, A.8.8) |
| **Revue de configuration cloud (CSPM)** | Contrôle automatique de la configuration AWS par rapport à un référentiel (CIS) | Continu ; détecte les erreurs fréquentes (bucket public, port ouvert) | Limité à la configuration ; ne teste pas l'application | € | **Oui, dès maintenant** (AWS Security Hub, MS-POL-05) |
| **Test d'intrusion classique** | Des auditeurs attaquent l'application dans un périmètre et un délai définis | Trouve les failles de logique ; rapport détaillé | Photo à un instant donné ; qualité variable selon le prestataire | €€ à €€€ | Possible, mais moins crédible auprès des clients sans qualification |
| **Test d'intrusion par un prestataire PASSI** | Même démarche, par un prestataire qualifié par l'ANSSI | Méthodologie et compétences vérifiées par l'ANSSI ; argument fort auprès des clients de santé et des assureurs | Plus cher ; délais de disponibilité des prestataires | €€€ | **Oui, une fois par an** (MS-MOD-02) |
| **Bug bounty privé** | Des chercheurs invités cherchent des failles et sont payés pour chaque faille validée | Couverture continue par de nombreux profils ; on ne paie que les résultats | Exige une organisation capable de trier et corriger vite ; coût imprévisible | €€ à €€€ | **Pas encore** : à envisager en 2028, une fois les bases corrigées |
| **Red team** | Simulation d'une attaque réelle et complète (phishing, intrusion, mouvement latéral), sans prévenir les équipes | Teste la détection et la réaction, pas seulement les failles | Très coûteux ; sans intérêt tant que la détection n'existe pas | €€€€ | **Non** : MediSoft n'a pas encore de supervision (module 5) |
| **Audit de code source** | Analyse du code par des experts | Trouve des failles invisibles de l'extérieur | Long ; complément d'un test d'intrusion | €€ à €€€ | Ciblé sur l'authentification et le contrôle d'accès, en 2028 |

## 3. Bonnes pratiques relevées

- **Commencer par l'automatique** : inutile de payer des auditeurs pour trouver des failles qu'un scanner détecte.
- **Un test d'intrusion n'a de valeur que si les failles sont corrigées.** Prévoir un contre-audit dans l'offre et suivre le taux de correction.
- **Tester ce qui compte vraiment** : pour un éditeur multi-clients, le cloisonnement entre clients est le point le plus important.
- **Changer de prestataire tous les 2 ou 3 ans** pour bénéficier d'un regard neuf.
- **Une red team suppose une équipe de détection** : sans supervision, elle ne fait que confirmer que rien n'est détecté.

## 4. Recommandation au comité sécurité

| Période | Combinaison recommandée |
|---|---|
| **2027** | Scan de vulnérabilités continu + CSPM AWS + **test d'intrusion PASSI annuel** (application web, API, mobile) avec contre-audit |
| **2028** | Idem + audit de code ciblé + bug bounty privé, si le taux de correction des vulnérabilités dépasse 90 % |
| **Au-delà** | Red team, une fois la supervision (SOC) en place et testée |

**Décision du comité du 27/01/2027 :** recommandation 2027 adoptée ; consultation de 3 prestataires PASSI sur la base du cahier des charges MS-MOD-02.
