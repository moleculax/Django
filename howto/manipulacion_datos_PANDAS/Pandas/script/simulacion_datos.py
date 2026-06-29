#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:14:57 2026

@author: moleculax
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 0. CREAR CARPETA DESTINO (Si no existe)
output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

# 1. SIMULACIÓN DE DATOS
np.random.seed(42)
fechas = pd.date_range(start="2023-01-01", periods=150, freq="W")
datos_aleatorios = np.random.normal(loc=0.002, scale=0.03, size=(150, 3))
returns_cut = pd.DataFrame(
    datos_aleatorios, index=fechas, columns=["Activo A", "Activo B", "Activo C"]
)

# 2. CONFIGURACIÓN DE LA FIGURA
fig = plt.figure(figsize=(15, 5))
ax1 = plt.subplot2grid((1, 3), (0, 0))
ax2 = plt.subplot2grid((1, 3), (0, 1))
ax3 = plt.subplot2grid((1, 3), (0, 2))

# 3. CUMULATIVE RETURNS
(returns_cut + 1).cumprod().plot(
    colormap="jet", ax=ax1, title="Acumulativo  Returns"
)
leg1 = ax1.legend(loc="upper left", ncol=2, prop={"size": 10}, fancybox=True)
leg1.get_frame().set_alpha(0.8)

# 4. ROLLING 50 SEMANAS RETURN
((returns_cut + 1).rolling(50).apply(np.prod, raw=True) - 1).plot(
    colormap="jet", ax=ax2, title="Rolling 50 Semanas Return"
)
leg2 = ax2.legend(loc="upper left", ncol=2, prop={"size": 10}, fancybox=True)
leg2.get_frame().set_alpha(0.8)

# 5. RETURN DISTRIBUCION
returns_cut.plot.box(vert=False, ax=ax3, title="Return Distribucion")

# 6. FORMATO, GUARDADO Y CIERRE
fig.autofmt_xdate()
plt.tight_layout()  # AJUSTA MARGENES

# Guardar la imagen con alta calidad (dpi=300) en la carpeta indicada
output_path = os.path.join(output_dir, "reporte_retornos.png")
plt.savefig(output_path, dpi=300, bbox_inches="tight")
print(f"Gráfico guardado exitosamente en: {output_path}")

# Cerrar la figura para liberar memoria del sistema
plt.close(fig)

