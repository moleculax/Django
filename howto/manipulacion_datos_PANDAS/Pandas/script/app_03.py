#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: moleculax
"""

import pandas as pd
import numpy as np

serie_empleados = pd.Series({
    101: "amartinez@empresa.com",
    102: None,
    103: "mrodriguez@empresa.com",
    104: "cgonzalez@empresa.com",
    105: "lfernandez@empresa.com",
    106: None,
    107: "esanchez@empresa.com",
    108: "mlopez@empresa.com",
    109: None,
    110: None,
    111: "pgomez@empresa.com"
})

print("Eliminar registros")
eliminar_registros = serie_empleados.dropna()
print(eliminar_registros)

print("\nReemplazar valores faltantes por 'Desconocido'")
reemplazar_registros = serie_empleados.fillna('desconocido')
print(reemplazar_registros)

diccionario_temperaturas = {
    2010: 73,
    2011: np.nan,
    2012: 75.3,
    2013: 72.4,
    2014: 72.5,
    2015: 74.4,
    2016: np.nan,
    2017: np.nan,
    2018: 73.5,
    2019: 72.7,
    2020: np.nan,
    2021: 73.5,
}

serie_temperaturas = pd.Series(diccionario_temperaturas)

print("\nReemplazar valores faltantes por la media")
reemplazar_temperaturas = serie_temperaturas.fillna(serie_temperaturas.mean())
print(reemplazar_temperaturas)