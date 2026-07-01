#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:08:32 2026

@author: moleculax
"""

import os
import matplotlib.pyplot as plt
import pandas as pd

# --- 1. DATOS Y TABLA DINÁMICA ---
df_ventas = pd.DataFrame(
    {
        "producto": [
            "Computadora",
            "Camiseta",
            "Alfombras",
            "Tableta",
            "Vestido",
            "Computadora",
        ],
        "categoria": [
            "Electrónicos",
            "Ropa",
            "Hogar",
            "Electrónicos",
            "Ropa",
            "Electrónicos",
        ],
        "ventas": [10000, 12000, 15000, 18000, 2000, 3000],
    }
)

df_tabla_dinamica = df_ventas.pivot_table(
    values="ventas", index="categoria", columns="producto", aggfunc="sum"
)

print("Tabla Dinámica:")
print(df_tabla_dinamica)
print("-" * 50)


# --- 2. CONFIGURACIÓN DEL GRÁFICO (ALTA DEFINICIÓN) ---
fig, ax = plt.subplots(figsize=(12, 6))

# Graficamos la tabla dinámica directamente como barras agrupadas
# - rot=0: Mantiene los nombres de las categorías horizontales
df_tabla_dinamica.plot(kind="bar", ax=ax, rot=0, edgecolor="black")


# --- 3. PERSONALIZACIÓN ---
plt.title("Ventas Totales por Categoría y Producto", fontsize=14, fontweight="bold")
plt.xlabel("Categorías", fontsize=12)
plt.ylabel("Total Ventas ($)", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)  # Añade líneas guía horizontales
plt.legend(title="Productos")


# --- 4. GUARDAR Y MOSTRAR ---
plt.tight_layout()

# Aseguramos que la carpeta exista y guardamos en 300 DPI
os.makedirs("graficos", exist_ok=True)
ruta_guardado = "graficos/ventas_tabla_dinamica_001.png"
plt.savefig(ruta_guardado, dpi=300, bbox_inches="tight")

print(f"Gráfica guardada en: {ruta_guardado}")
print("-" * 50)

# Desplegamos la ventana flotante
plt.show()
