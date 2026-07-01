#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:08:58 2026

@author: moleculax
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_estudiantes = pd.read_csv('archivos_excel/estudiantes.csv')
print(df_estudiantes)

matriz_correlacion = df_estudiantes.corr()

correlacion_promedio = matriz_correlacion['promedio']
print("Correlación con el promedio obtenido en el curso")
print(correlacion_promedio)

sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlación')
plt.show()