# Bulletin de veille sécurité — Novembre 2026

| Diffusion | Comité sécurité, DPO, CTO, Resp. Ops | Rédaction | RSSI |
|---|---|---|---|

> Bulletin mensuel (mesure A.5.7, renseignements sur les menaces, et A.5.31, exigences réglementaires). Trois rubriques : **réglementaire**, **menaces**, **technique**. Pour chaque information : son impact pour MediSoft et l'action décidée.
>
> Contrairement au reste du projet, ce bulletin s'appuie sur l'actualité réelle de novembre 2026, avec ses sources.

---

## 1. Veille réglementaire

| Sujet | Ce qu'il faut savoir | Impact pour MediSoft | Action |
|---|---|---|---|
| **NIS2 : la loi française revient à l'Assemblée nationale** | Le projet de loi « Résilience », qui transpose NIS2, est inscrit en séance publique à l'Assemblée nationale à partir du 9 novembre 2026, après plusieurs reports. Le texte avait été adopté par le Sénat en mars 2025. Le 8 juillet 2026, la Commission européenne avait saisi la Cour de justice de l'UE contre la France pour défaut de transposition | Probable qualification d'**entité importante** (registre des obligations, REG-05). Les obligations ne s'appliqueront qu'après la promulgation et les décrets, mais les clients du secteur santé les exigent déjà | Suivre les débats ; préparer l'enregistrement auprès de l'ANSSI ; poursuivre la mise en conformité anticipée (SMSI) |
| **HDS : fin de la période de transition** | Depuis le 16 mai 2026, tous les hébergeurs certifiés doivent l'être selon le référentiel HDS v2.0, qui exige notamment le stockage des données dans l'EEE | **Non-conformité critique** de MediSoft (certificat v1.1 obsolète, REG-03) | Audit de certification v2.0 en priorité absolue (PA-02) |
| **CRA : obligations de signalement en vigueur** | Depuis le 11 septembre 2026, les fabricants doivent signaler les vulnérabilités activement exploitées et les incidents graves touchant leurs produits | Concerne l'application mobile MediSoft Patient (REG-07) | Processus de signalement intégré à la procédure d'incident (MS-PRO-04 §6) |

## 2. Veille sur les menaces

| Menace | Ce qu'il faut savoir | Impact pour MediSoft | Action |
|---|---|---|---|
| **Usurpation de partenaires** | Les campagnes d'hameçonnage se font de plus en plus passer pour des clients, des fournisseurs ou des dirigeants, avec des domaines ressemblants | Constaté chez nous : 4 messages ciblés en une semaine (MS-ENR-04) | Alerte interne ; atelier fraude pour la finance et les achats |
| **Secteur de la santé** | Le secteur de la santé reste une cible fréquente des rançongiciels et des vols de données ; les éditeurs de logiciels sont visés pour atteindre plusieurs établissements à la fois | MediSoft est un point d'entrée possible vers 120 établissements : un scénario majeur de l'EBIOS RM | Priorité au cloisonnement entre clients dans le test d'intrusion (MS-MOD-02) |
| **Comptes et secrets oubliés** | Les comptes d'anciens collaborateurs et les secrets laissés dans l'historique Git sont des points d'entrée classiques | Constaté chez nous : INC-2026-014 et INC-2026-015 | Contrôle mensuel des comptes ; détection des secrets dans la CI |

## 3. Veille technique

| Source | Usage |
|---|---|
| **CERT-FR** (avis et alertes) | Revue hebdomadaire des avis touchant nos technologies : Linux, PostgreSQL, navigateurs, composants de l'application mobile |
| **Catalogue CISA KEV** (vulnérabilités activement exploitées) | Toute vulnérabilité du catalogue touchant notre parc est traitée comme critique (correction sous 7 jours) |
| **Bulletins de sécurité AWS, Microsoft, GitHub** | Suivi des changements de nos fournisseurs Tier 1 |
| **CERT Santé (ANS)** | Alertes propres au secteur de la santé |

**Ce mois-ci :** pas de vulnérabilité critique touchant notre parc identifiée dans les sources suivies. *(À compléter chaque mois à partir des avis publiés.)*

---

## Sources

- Leto, « NIS 2 : le projet de loi Résilience revient à l'Assemblée nationale le 9 novembre », novembre 2026 — leto.legal
- IT-Connect, « NIS 2 encore repoussé : la France traînée devant la justice européenne », 14/07/2026 — it-connect.fr
- Conseil national des barreaux, « État des lieux de la transposition des directives NIS2 et REC », 27/08/2026 — cnb.avocat.fr
- Donneespersonnelles.fr, « Certification HDS : nouveau référentiel v2 » — donneespersonnelles.fr
- Règlement (UE) 2024/2847 (Cyber Resilience Act)
