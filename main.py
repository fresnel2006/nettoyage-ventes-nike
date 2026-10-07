from pathlib import Path

import pandas as pd
from tabulate import tabulate

DOSSIER = Path(__file__).parent
SORTIE = DOSSIER / "output"
SORTIE.mkdir(exist_ok=True)

nike = pd.read_csv(DOSSIER / "nike_shoes_sales.csv").head(110)

nike = nike.drop(columns=["product_id", "listing_price", "discount", "brand", "description", "images"])

# On retire d'abord les lignes incompletes, puis on convertit en nombres
nike = nike.dropna(subset=["product_name", "sale_price", "rating", "reviews"])
for colonne in ["sale_price", "rating", "reviews"]:
    nike[colonne] = pd.to_numeric(nike[colonne], errors="coerce")
nike = nike.dropna(subset=["sale_price", "rating", "reviews"])

nike["product_name"] = nike["product_name"].str.strip()

nike.to_csv(SORTIE / "nike_nettoye.csv", index=False)
print(tabulate(nike, tablefmt="psql", headers="keys", showindex=False))
