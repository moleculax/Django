#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:27:47 2026

@author: moleculax
"""

import pandas as pd

archivo = 'archivos_excel/empleados.csv'
df_empleados = pd.read_csv(archivo, delimiter=";")

print("Dataframe ORIGINAL:")
print(df_empleados)

df_empleados = df_empleados.drop(columns=['Estado_Civil','Edad'])
print("Dataframe SIN EL ESTADO CIVIL Y SIN EDAD:")
print(df_empleados)

# ELIMINAMOS EL PRIMER REGISTRO
df_empleados = df_empleados.drop(df_empleados.index[0])
print("Dataframe SIN EL PRIMER REGISTRO:")
print(df_empleados)