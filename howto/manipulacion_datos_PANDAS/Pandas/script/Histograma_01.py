#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:31:05 2026

@author: moleculax
"""

import pandas as pd
import matplotlib.pyplot as plt

archivo = 'archivos_excel/empleados.csv'
df_empleados = pd.read_csv(archivo, delimiter=";")

print("Dataframe original:")
print(df_empleados)

df_empleados['Edad'].hist(bins=5, edgecolor='black', grid=False)
plt.title('Distribución de edades')
plt.xlabel('Grupos de edad')
plt.ylabel('Frecuencia')
plt.show()