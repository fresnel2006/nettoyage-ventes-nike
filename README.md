# Nettoyage des ventes de chaussures Nike

Préparation d'un dataset de ventes de chaussures Nike avec pandas.

## Ce que fait le script
- Lecture de `nike_shoes_sales.csv` (110 premières lignes)
- Suppression des colonnes inutiles (`product_id`, `listing_price`, `discount`, `brand`, `description`, `images`)
- Conversion de `sale_price`, `rating` et `reviews` en nombres
- Suppression des lignes incomplètes
- Export du CSV nettoyé et affichage en tableau

## Lancer le projet
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Stack
Python, pandas, numpy, tabulate

## Auteur
Ange Fresnel Traoré - ESATIC, Abidjan
