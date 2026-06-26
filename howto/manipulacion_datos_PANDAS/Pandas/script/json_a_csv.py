#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:20:44 2026
@author: moleculax

LEE UN JSON Y LO EXPORTA A CSV
LUEGO SE MUSTRA DATOS DE ARCHIVO EXPORTADO
"""

import pandas as pd

datafile = pd.read_json('archivos_json/datos.json')

# Exportar a CSV
exportado = "archivos_excel/archivoexport.csv"
datafile.to_csv(exportado, index=False)

# Leer archivo CSV exportado
lectura_exportado = pd.read_csv(exportado)

# Mostrar los datos
print("DATOS DEL ARCHIVO EXPORTADO:")
print(lectura_exportado)