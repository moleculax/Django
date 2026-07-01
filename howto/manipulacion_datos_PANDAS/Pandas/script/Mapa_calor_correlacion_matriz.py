#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:08:58 2026

@author: moleculax
"""

# Importamos Pandas para la manipulación de datos y lectura del archivo CSV
import pandas as pd

# Importamos Seaborn para crear gráficos estadísticos atractivos (como el mapa de calor)
import seaborn as sns

# Importamos Matplotlib para controlar los detalles del gráfico (título, mostrar ventana, etc.)
import matplotlib.pyplot as plt

# Lee el archivo CSV de estudiantes y lo carga en memoria como un DataFrame de Pandas
df_estudiantes = pd.read_csv("archivos_excel/estudiantes.csv")

# Muestra en la consola la tabla completa de estudiantes para verificar los datos cargados
print(df_estudiantes)

# .corr() calcula el coeficiente de correlación de Pearson entre todas las columnas numéricas.
# Mide la relación lineal entre variables (va de -1 a 1, donde 1 es correlación perfecta).
matriz_correlacion = df_estudiantes.corr()

# Filtra la matriz para extraer únicamente cómo se relacionan las demás variables con la columna 'promedio'
correlacion_promedio = matriz_correlacion["promedio"]

print("Correlación con el promedio obtenido en el curso")
# Muestra los valores de correlación específicos para el promedio (ej. si estudiar más horas sube el promedio)
print(correlacion_promedio)

# sns.heatmap crea un mapa de calor visual basado en los números de la matriz de correlación.
# - annot=True: Dibuja el valor numérico exacto dentro de cada celda.
# - cmap='coolwarm': Usa una paleta de colores donde el azul es correlación negativa y el rojo es positiva.
# - fmt=".2f": Formatea los números para que muestren solo 2 decimales.
sns.heatmap(matriz_correlacion, annot=True, cmap="coolwarm", fmt=".2f")

# Define el título principal que se mostrará en la parte superior de la ventana del gráfico
plt.title("Matriz de Correlación")

# Renderiza y abre la ventana flotante para visualizar el gráfico en pantalla
plt.show()
