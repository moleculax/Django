#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:06:28 2026

lee y muestra datos de archiv excel

@author: moleculax
"""

import pandas as pd

archivo = 'archivos_excel/Workshop_File.xlsx'

# INDICO CUAL PESTAÑA O SHEET LEER DEL ARCHIVO
instrucciones = pd.read_excel(archivo, sheet_name='instrucciones')
contactos = pd.read_excel(archivo, sheet_name='contactos')

print('RESULTADO INSTRUCCIONES')
print(instrucciones)

print('RESULTADO CONTACTOS / EMAIL')

print(contactos)

