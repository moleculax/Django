#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 19:49:58 2026

@author: moleculax
"""

import pandas as pd

datos = {
    'nombre': ['Juan', 'Pedro', 'Luisa', 'Maria'],
    'edad': [25, 30, 28, 35],
    'ciudad': ['Madrid', 'Buenos Aires', 'Santiago', 'Londres']
}

df = pd.DataFrame(datos)
print(df)

# Filtrar filas donde la edad es mayor a 30
# df_filtro = df.loc[df['edad'] > 30]
# print(df_filtro)

# Filtrar filas donde la edad es mayor a 30

print("Mayores de 30")
df_filtro = df.query("edad >= 30")
print(df_filtro)
