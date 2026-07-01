#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:09:29 2026

@author: moleculax
"""

import pandas as pd
import matplotlib.pyplot as plt

df_ventas = pd.DataFrame({
    'productos': ['computadora', 'teléfono', 'relojes', 'televisores', 'computadora', 'cámaras', 'computadora', 'teléfono' ],
    'ventas': [10000, 12000, 15000, 18000, 20000, 22000, 15000, 18000]
})

df_agrupamiento = df_ventas.groupby('productos')['ventas'].sum().reset_index()

df_agrupamiento.plot(kind='bar', x='productos', y='ventas')
plt.title('Gráfico de barras de ventas por producto')
plt.xlabel('Productos')
plt.ylabel('Ventas')
plt.show()