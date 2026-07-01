#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:37:21 2026

@author: moleculax
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:31:05 2026

@author: moleculax
"""

import pandas as pd
import matplotlib.pyplot as plt

archivo = "archivos_excel/empleados.csv"
df_empleados = pd.read_csv(archivo, delimiter=";")

# SELECCIONAMOS AMBAS COLUMNAS
# Agregamos alpha=0.7 para darle transparencia a las barras por si se enciman
df_empleados[["Edad", "Experiencia"]].hist(
    bins=5, edgecolor="black", grid=False, alpha=0.7
)

# Añadimos una leyenda para saber qué color corresponde a cada variable
plt.legend(["Edad", "Experiencia"])

plt.title("Distribución de Edad y Experiencia")
plt.xlabel("Rangos Numéricos")
plt.ylabel("Frecuencia")
plt.show()
