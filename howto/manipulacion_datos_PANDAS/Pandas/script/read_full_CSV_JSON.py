#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:24:30 2026

@author: moleculax
"""
import os
import matplotlib.pyplot as plt
import pandas as pd

# ==========================================
# CONFIGURACIÓN PARA MOSTRAR TODO EN TERMINAL
# ==========================================
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

# 1. Leer el archivo CSV corregido con su separador correcto
df_csv = pd.read_csv("archivos_excel/empleados.csv", sep=";")

# 2. Leer el archivo JSON
df_json = pd.read_json("archivos_json/datos.json")

# ==========================================
print("=== RESULTADO DATOS DEL JSON ===")
print(df_json)
print("\n" + "=" * 40 + "\n")

print("=== RESULTADO DATOS DEL CSV ===")
print(df_csv)
print("\n" + "=" * 40 + "\n")

# ==========================================
# 3. GENERACIÓN DE GRÁFICAS (MÉTRICAS DEL CSV)
# ==========================================
# Limpieza rápida: Eliminar filas donde el Departamento o Salario estén vacíos
df_limpio = df_csv.dropna(subset=["Departamento", "Salario"]).copy()

# Agrupamos para calcular el salario promedio por cada departamento
salario_por_dep = df_limpio.groupby("Departamento")["Salario"].mean().sort_values()

# Creamos una figura con 2 subplots (1 fila, 2 columnas)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Gráfica 1: Barras horizontales para el salario promedio
salario_por_dep.plot(kind="barh", ax=ax1, color="skyblue", edgecolor="black")
ax1.set_title("Salario Promedio por Departamento", fontsize=14, fontweight="bold")
ax1.set_xlabel("Salario Promedio ($)", fontsize=12)
ax1.set_ylabel("Departamento", fontsize=12)
ax1.grid(axis="x", linestyle="--", alpha=0.7)

# Gráfica 2: Histograma para la distribución de los salarios de los empleados
df_limpio["Salario"].plot(
    kind="hist", bins=15, ax=ax2, color="lightgreen", edgecolor="black"
)
ax2.set_title("Distribución General de Salarios", fontsize=14, fontweight="bold")
ax2.set_xlabel("Rango de Salario ($)", fontsize=12)
ax2.set_ylabel("Cantidad de Empleados", fontsize=12)
ax2.grid(axis="y", linestyle="--", alpha=0.7)

# Ajustar diseño para que no se encimen los textos
plt.tight_layout()

# ==========================================
# 4. CREAR CARPETA Y GUARDAR LA IMAGEN
# ==========================================
CapetaGraficos = "graficos"
# Crea la carpeta si no existe. Si ya existe, no hace nada de forma segura.
os.makedirs(CapetaGraficos, exist_ok=True)

# Definir la ruta completa del archivo final
ruta_guardado = os.path.join(CapetaGraficos, "metricas_empleados.png")

# Guardar la imagen con alta resolución (300 DPI) y ajustando márgenes externos
plt.savefig(ruta_guardado, dpi=300, bbox_inches="tight")
print(f"✅ Gráfica generada y guardada con éxito en: '{ruta_guardado}'")

# Cerrar la figura para liberar la memoria RAM
plt.close(fig)
