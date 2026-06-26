#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: moleculax
"""

import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('resultados_golf.csv')

print("RESULTADO TORNEO")
print(df)

# Obtener los ganadores (posición 1)
ganadores = df[df['posicion'] == 1]

# Obtener el último lugar (posición máxima) comparando cada valor
ultimo_lugar = df[df['posicion'] == df['posicion'].max()]

# Usar if para verificar si hay ganadores
if len(ganadores) > 0:
    print("\nGANADORES POR TORNEO:")
    print(ganadores[['torneo', 'jugador', 'total', 'premio']])
else:
    print("\nNo se encontraron ganadores.")

print("\nULTIMA POSICION:")
print(ultimo_lugar[['torneo', 'jugador', 'total', 'posicion']])