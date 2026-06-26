#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:31:55 2026

@author: moleculax
"""

import pandas as pd

archivo_csv = "archivos_excel/archivoexport.csv"
# LEE CSV
df = pd.read_csv(archivo_csv)

# CONVIERTE A JSON

pasojson = "archivos_json/vienedecss.json"

df.to_json(pasojson, orient='records', lines=False)

print("CSV CONVERTIDO EN JSON")

print("LEO Y MUESTRO EL ARCHIVO CONVERTIDO")

print("\nCONTENIDO DEL JSON:")
with open(pasojson, 'r') as f:
    print(f.read())

# MUESTRA EL  DataFrame
print("\n📊 DATOS DEL DATAFRAME:")
print(df)