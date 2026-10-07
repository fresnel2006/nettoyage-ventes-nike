import pandas as pd
import numpy as np
from tabulate import tabulate

nike=pd.read_csv("nike_shoes_sales.csv").head(110)
nike=nike.drop(columns=["product_id","listing_price","discount","brand","description","images"])
for i in ["sale_price","rating","reviews"]:
    nike[i]=nike[i].astype(float)
nike=nike.dropna(subset=["sale_price","product_name","rating","reviews"])
nike.to_csv("C:/Users/fresnel/Desktop/csv traite/nike_shoes_sales.csv",index=False)

print(tabulate(nike,tablefmt="psql",headers="keys"))