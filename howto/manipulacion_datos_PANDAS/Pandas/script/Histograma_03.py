#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:42:15 2026

@author: moleculax
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# --- 1. CONFIGURACIÓN Y CARGA DE DATOS ---
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

archivo = "archivos_excel/empleados.csv"
df_empleados = pd.read_csv(archivo, delimiter=";")

print("Dataframe original de empleados:")
print(df_empleados)
print("-" * 50)

# Calculamos la matriz de correlación numérica
matriz_correlacion = df_empleados.corr(numeric_only=True)


# --- 2. CREACIÓN DE LA VENTANA UNIFICADA ---
# Dimensiones en formato 16:9 (Alta Definición)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9))


# --- GRÁFICO 1 (Izquierda): MAPA DE CALOR ---
sns.heatmap(
    matriz_correlacion, annot=True, cmap="coolwarm", fmt=".2f", ax=ax1, cbar=True
)
ax1.set_title("Matriz de Correlación del Personal", fontsize=14, fontweight="bold")


# --- GRÁFICO 2 (Derecha): HISTOGRAMAS UNIDOS ---
df_empleados[["Edad", "Experiencia"]].plot(
    kind="hist", bins=5, edgecolor="black", grid=False, alpha=0.7, ax=ax2
)
ax2.set_title("Distribución de Edad y Experiencia", fontsize=14, fontweight="bold")
ax2.set_xlabel("Escala Numérica (Años)", fontsize=11)
ax2.set_ylabel("Frecuencia (Cantidad de Empleados)", fontsize=11)


# --- 3. AJUSTE DE DISEÑO Y GUARDADO EN LA CARPETA GRAFICOS ---
plt.tight_layout()

# UNIFICADO: Creamos la carpeta 'graficos' de forma segura si no existe
os.makedirs("graficos", exist_ok=True)

# UNIFICADMOS: Guardamos la imagen con resolución profesional de 300 DPI
ruta_guardado = "graficos/analisis_empleados_histograma.png"
plt.savefig(ruta_guardado, dpi=300, bbox_inches="tight")
print(f"Grafica guardada exitosamente en: {ruta_guardado}")
print("-" * 50)

# Abre la ventana con los gráficos integrados
plt.show()
