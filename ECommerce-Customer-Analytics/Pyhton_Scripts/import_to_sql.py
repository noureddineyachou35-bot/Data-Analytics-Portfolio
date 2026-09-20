import pandas as pd
from sqlalchemy import create_engine
import urllib

# 1. Charger les données (Excel ou CSV)
# Si c'est le fichier Excel d'origine :
file_path = r'C:\Users\n.yachou\Downloads\archive\syntheticonlineretaildata.csv'
df = pd.read_csv(file_path)

print("Nettoyage des données en cours...")

# 2. NETTOYAGE CRUCIAL (C'est ici que l'assistant SQL échouait)
# On convertit CustomerID en texte d'abord pour gérer les vides, puis en entier (ou on laisse en float)
df['customer_id'] = df['customer_id'].fillna(0).astype(int)

# On s'assure que la date est bien au format Date
df['order_date'] = pd.to_datetime(df['order_date'])

# On enlève les espaces dans les noms de colonnes pour SQL
df.columns = [c.replace(' ', '_') for c in df.columns]

# 3. CONNEXION À SQL SERVER
server_name = 'PCACHOUNO'
database_name = 'PortfolioProjects'

params = urllib.parse.quote_plus(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server_name};'
    f'DATABASE={database_name};'
    f'Trusted_Connection=yes;'
)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# 4. ENVOI VERS SQL (Il va créer la table automatiquement avec les bons types)
try:
    df.to_sql('online_retail', con=engine, if_exists='replace', index=False)
    print("🚀 Succès ! Les données sont dans SQL Server sans erreurs.")
except Exception as e:
    print(f"❌ Erreur : {e}")