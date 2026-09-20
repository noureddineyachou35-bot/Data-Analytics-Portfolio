import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import urllib

# Connexion à SQL Server
server_name = 'PCACHOUNO'
database_name = 'PortfolioProjects'
params = urllib.parse.quote_plus(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes;')
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# 1. Charger les données pour l'analyse RFM
query = """
SELECT 
    customer_id,
    age,
    gender,
    review_score,
    DATEDIFF(day, MAX(order_date), '2025-03-31') AS Recency, -- Jours depuis le dernier achat
    COUNT(order_date) AS Frequency,                         -- Nombre d'achats
    SUM(quantity * price) AS Monetary                      -- Total dépensé
FROM dbo.online_retail
GROUP BY customer_id, age, gender, review_score
"""
df_rfm = pd.read_sql(query, engine)

# 2. Créer des scores (1 à 5) pour la Récence et le Montant
# Plus la récence est basse, mieux c'est (score 5)
df_rfm['R_Score'] = pd.qcut(df_rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
# Plus le montant est haut, mieux c'est (score 5)
df_rfm['M_Score'] = pd.qcut(df_rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])

# 3. Définir des Segments
def segment_customer(df):
    if df['M_Score'] >= 4 and df['R_Score'] >= 4:
        return 'Champions'
    elif df['M_Score'] <= 2 and df['R_Score'] <= 2:
        return 'Lost Customers'
    else:
        return 'Average'

df_rfm['Segment'] = df_rfm.apply(segment_customer, axis=1)

print(df_rfm.head())

# 4. Visualisation : Score de satisfaction par Segment
plt.figure(figsize=(10,6))
sns.boxplot(x='Segment', y='review_score', data=df_rfm)
plt.title('Satisfaction Client (Review Score) par Segment RF')
plt.show()
# 5. Visualisation : Qui sont nos Champions ? (Âge et Genre)
plt.figure(figsize=(12,6))
sns.violinplot(x='Segment', y='age', hue='gender', data=df_rfm, split=True)
plt.title('Répartition de l\'Âge par Segment et par Genre')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# 6. Nettoyage des NaNs pour l'analyse démographique
df_clean = df_rfm.dropna(subset=['gender', 'age'])

# 7. Création de tranches d'âge
bins = [18, 25, 35, 45, 55, 65, 100]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
df_clean['age_group'] = pd.cut(df_clean['age'], bins=bins, labels=labels)

# 8. Visualisation : Montant total dépensé par tranche d'âge et genre
plt.figure(figsize=(12,6))
sns.barplot(x='age_group', y='Monetary', hue='gender', data=df_clean, estimator=sum)
plt.title('Chiffre d''Affaires Total par Tranche d''Âge et Genre')
plt.ylabel('Total Revenue ($)')
plt.show()
# 1. On crée un dataframe propre (sans NaNs pour le genre et l'âge)
df_clean = df_rfm.dropna(subset=['gender', 'age'])

# 2. On crée des catégories d'âge pour une analyse plus claire
df_clean['age_group'] = pd.cut(df_clean['age'], bins=[0, 25, 45, 65, 100], labels=['Jeunes', 'Adultes', 'Seniors', 'Retraités'])

# 3. Visualisation : Montant moyen dépensé par Genre et Groupe d'âge
plt.figure(figsize=(10,6))
sns.barplot(x='age_group', y='Monetary', hue='gender', data=df_clean)
plt.title('Panier Moyen par Groupe d''Âge et Genre')
plt.show()