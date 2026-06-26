#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 00:00:00 2026
@author: moleculax
"""

import pandas as pd

# Configurar pandas para mostrar todos los datos
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

# Ubicar el archivo
archivo = "archivos_excel/empleados.csv"

# Lectura del archivo
df = pd.read_csv(archivo, delimiter=";")

# Obtener dimensiones
nro_filas, nro_columnas = df.shape

print(f"NRO FILAS {nro_filas} NRO COLUMNAS {nro_columnas}")

print("\n ===================================== \n")
print(df.to_string())  #  to_string() para mostrar todas las columnas

print("\n ===================================== \n")

# Mostrar nombres de columnas
print("NOMBRES DE COLUMNAS:")
print(df.columns.tolist())

# Verificar si la columna 'Departamento' existe
if 'Departamento' in df.columns:
    print("\n✅ La columna 'Departamento' existe")
else:
    print("\n❌ La columna 'Departamento' NO existe")

print("\n ===================================== \n")

# Valores faltantes
valoresFaltantesColumnas = df.isna().sum()
print("Nro de valores faltantes en cada columna:")
print(valoresFaltantesColumnas)

# Reemplazar valores faltantes en todas las columnas
df = df.fillna("Sin asignacion")

print("\n ===================================== \n")
print(df.to_string())  # to_string() para mostrar todas las columnas