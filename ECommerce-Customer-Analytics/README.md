🛒 Analyse de la Valeur Client & Segmentation RFM (E-Commerce)
📌 Présentation du Projet
Ce projet analyse les données de transactions d'une boutique en ligne pour identifier les comportements d'achat, segmenter la clientèle et évaluer la fidélisation. L'objectif est de transformer des données brutes en recommandations stratégiques pour les équipes marketing.

🛠️ Stack Technique
Base de données : SQL Server (T-SQL)
Langage : Python 3.x
Librairies : Pandas (Traitement), Seaborn/Matplotlib (Visualisation), SQLAlchemy (Pipeline Data)
Analyse : Segmentation RFM (Recency, Frequency, Monetary) & Analyse de Cohorte.
🚀 Pipeline de Données (Aspect "Advanced")
Plutôt que d'utiliser de simples fichiers Excel, j'ai mis en place un flux de données professionnel :

Nettoyage Python : Gestion des types de données (dates, IDs) et traitement des valeurs manquantes (NaN).
Ingestion Automatisée : Script Python utilisant SQLAlchemy pour injecter les données dans SQL Server.
Analyses Complexes : Utilisation de CTEs et de PIVOT en SQL pour calculer la rétention mensuelle.
💡 Analyses & Insights Clés
1. Analyse de Cohorte (Rétention)
Observation : Le taux de rétention après le premier mois est de 0%.
Insight Business : Le modèle actuel repose uniquement sur l'acquisition de nouveaux clients. Il y a une absence critique de stratégie de "re-marketing".
2. Segmentation RFM
J'ai classé les clients en 3 segments principaux :

Champions : Clients à haute valeur, récents, avec un score de satisfaction moyen de 4.5/5.
Average : La majorité de la base, avec un panier moyen modéré.
Lost Customers : Clients n'ayant pas acheté depuis plus de 6 mois et ayant un score de satisfaction faible.
3. Profil Démographique (Focus Rentabilité)
Insight : Les femmes de la tranche 36-45 ans représentent le segment le plus rentable avec le panier moyen le plus élevé.
Recommandation : Allouer 60% du budget publicitaire sur ce segment spécifique pour maximiser le ROI.