#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:37:20 2026

@author: moleculax
"""

import pandas as pd

# CONFIGURACIÓN PARA MOSTRAR TODOS LOS DATOS
pd.set_option("display.max_rows", None)  # Muestra todas las filas sin truncar
pd.set_option("display.max_columns", None)  # Muestra todas las columnas sin truncar
pd.set_option(
    "display.width", None
)  # Ajusta el ancho de la consola para evitar saltos de línea

archivo = "archivos_excel/empleados.csv"
df_empleados = pd.read_csv(archivo, delimiter=";")

print("Dataframe original:")
print(df_empleados)

total_elementos = df_empleados.size
print("Número total de elementos:", total_elementos)

dimensiones = df_empleados.shape
print("Filas:", dimensiones[0])
print("Columnas:", dimensiones[1])

num_dimensiones = df_empleados.ndim
print("Número de dimensiones:", num_dimensiones)

print("Eliminar columnas para reducir la dimensionalidad")
df_empleados = df_empleados.drop(["Estado_Civil", 'Edad', 'Departamento'], axis=1)
print(df_empleados)

print("Eliminar filas para reducir la dimensionalidad")
df_empleados = df_empleados[df_empleados["Salario"] < 2000]
print(df_empleados)

dimensiones = df_empleados.shape
print("Filas:", dimensiones[0])
print("Columnas:", dimensiones[1])
