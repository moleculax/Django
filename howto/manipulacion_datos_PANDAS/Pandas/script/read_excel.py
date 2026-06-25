#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:10:38 2026

@author: moleculax
"""

import pandas as pd
import matplotlib.pyplot as plt  #  biblioteca para graficar

# Leer el archivo como plantilla de Excel
df = pd.read_excel("temperaturaMes.xltx")

# Explorar el contenido rápido
print(df.head())       
print(df.tail(3))      
print(df.info())       
print(df.describe())   

# Cálculos de máximos y mínimos
temperaturamaxima = df['TEMPERATURA'].max()
temperaturaminima = df['TEMPERATURA'].min()
print("La temperatura máxima es:", temperaturamaxima)
print("La temperatura minima es:", temperaturaminima)

# ==========================================
#              ZONA DE GRÁFICOS
# ==========================================

# Opción A: Gráfico de líneas (Evolución de la temperatura)
plt.figure(figsize=(10, 5)) # Define el tamaño de la ventana del gráfico
plt.plot(df['TEMPERATURA'], marker='o', color='blue', label='Temperatura')

# Personalización del gráfico
plt.title('Evolución de la Temperatura Mensual')
plt.xlabel('Índice / Mes')
plt.ylabel('Temperatura (°C)')
plt.grid(True) # Añade cuadrícula de fondo
plt.legend()


# Guardar gráfico
plt.savefig('graficos/grafico_temp.png', dpi=300, bbox_inches='tight')
print(" Gráfico guardado como 'graficos/grafico_temp.png'")

# Mostrar el gráfico en pantalla
plt.show()
