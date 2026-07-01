#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:50:21 2026

@author: moleculax
"""

import pandas as pd
import matplotlib.pyplot as plt

df_ventas = pd.DataFrame({
    'fecha': pd.to_datetime(['2026-02-01', '2026-03-01', '2026-04-01', '2026-05-01', '2026-06-01']),
    'ventas': [1004,1500,1250,1235,13445]
})

df_ventas['Año'] = df_ventas['fecha'].dt.year
df_ventas['Mes'] = df_ventas['fecha'].dt.month
df_ventas['Dia'] = df_ventas['fecha'].dt.day

print("Mostrar información del año, mes y día")
print(df_ventas)

print("Filtro de fechas:")
fecha_inicio = pd.to_datetime('2025-02-01')
fecha_fin = pd.to_datetime('2026-04-01')
df_filtro_fecha = df_ventas[(df_ventas['fecha'] >= fecha_inicio) & (df_ventas['fecha'] <= fecha_fin)]
print(df_filtro_fecha)



# GRAFICAMOS
df_ventas.set_index('fecha', inplace=True)
df_ventas['ventas'].plot(title='Series de tiempo') 

# GUARDAMOPS GRAFICA
ruta_guardado = "graficos/analisis_fechas_ventas.png"
plt.savefig(ruta_guardado, dpi=300, bbox_inches="tight")

# MOSTRAMOS GRAFICA
plt.show()