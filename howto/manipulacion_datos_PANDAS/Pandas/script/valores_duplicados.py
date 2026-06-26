#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:21:39 2026
VALORES DUPLICADOS
@author: moleculax
"""

import pandas as pd

ventas_mes = ["ENERO", "FEBRERO", "ABRIL", "ENERO", "MAYO","ABRIL"]
montos_mes = [50000,10000,50000,50000,630000,120000]

df_ventas = pd.DataFrame({
    "ventas": ventas_mes,
    "montos": montos_mes
})

print("DATOS ORIGINALES:")
print(df_ventas)

print("VALORE DUPLICADOS")

duplicados = df_ventas[df_ventas.duplicated(subset=['ventas'])]

print(duplicados)

print("QUITAMOS VALORES DUPLICADOS")

sin_duplicados = df_ventas.drop_duplicates()

print(sin_duplicados)