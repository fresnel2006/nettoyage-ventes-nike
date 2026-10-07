# Nettoyage des ventes de chaussures Nike

Préparation d'un dataset de ventes de chaussures Nike avec pandas.

## Ce que fait le script
- Lecture de `nike_shoes_sales.csv` (110 premières lignes)
- Suppression des colonnes inutiles (`product_id`, `listing_price`, `discount`, `brand`, `description`, `images`)
- Suppression des lignes incomplètes, puis conversion de `sale_price`, `rating` et `reviews` en nombres
- Export dans `output/nike_nettoye.csv` et affichage en tableau

## Lancer le projet
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
Les fichiers nettoyés sont enregistrés dans le dossier `output/` (créé automatiquement).

## Stack
Python, pandas, tabulate

## Auteur
Ange Fresnel Traoré - ESATIC, Abidjan
