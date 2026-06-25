#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:51:02 2026
@author: moleculax
GRAFICAS
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

diccionario_ventas = {
    2018: 200,
    2019: 165,
    2020: 180,
    2021: 400,
    2022: 195,
    2023: 220,
    2024: 280,
    2025: 260,
    2026: 300,
}

serie_ventas = pd.Series(diccionario_ventas)

# Crear carpeta para gráficos si no existe
if not os.path.exists('graficos'):
    os.makedirs('graficos')

# Crear gráfico
fig, ax = plt.subplots(figsize=(12, 6))
serie_ventas.plot(
    title='Ventas anuales 2018-2026',
    marker='o',
    color='blue',
    xlabel='Años',
    ylabel='Ventas (en miles de Pesos)',
    ax=ax
)

ax.grid(True, alpha=0.3)
ax.set_xticks(serie_ventas.index)
ax.set_xticklabels(serie_ventas.index, rotation=45)

# Guardar gráfico
plt.savefig('graficos/grafico_ventas.png', dpi=300, bbox_inches='tight')
print("✅ Gráfico guardado como 'graficos/grafico_ventas.png'")

# Mostrar gráfico
plt.show()
print("Ventas")
ventas = pd.Series(diccionario_ventas)

print(ventas)
