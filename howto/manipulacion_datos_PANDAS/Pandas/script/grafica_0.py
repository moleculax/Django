#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:51:02 2026
@author: moleculax
GRAFICAS
"""

import pandas as pd
import matplotlib.pyplot as plt

diccionario_ventas = {
    2018: 150,
    2019: 165,
    2020: 180,
    2021: 210,
    2022: 195,
    2023: 220,
    2024: 245,
    2025: 260,
}

serie_ventas = pd.Series(diccionario_ventas)

serie_ventas.plot(
    title='Ventas anuales 2018-2025',
    marker='o',
    color='blue',
    xlabel='Años',
    ylabel='Ventas (en miles de Pesos'
)

plt.show()
