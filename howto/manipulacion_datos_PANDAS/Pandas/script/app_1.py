#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:44:15 2026

@author: moleculax
"""

import pandas as pd

diccionario_empleados = {
    101 : "Ana Martínez",
    102 : "Luis Pérez",
    103 : "María González",
    104 : "Carlos Rodríguez",
    105 : "Laura Fernández",
    106 : "Javier Sánchez",
    107 : "Carmen López",
    108 : "Manuel Díaz",
    109 : "Isabel Gómez",
    110 : "Pedro Ruiz"
}

serie_empleados = pd.Series(diccionario_empleados)

print("Serie:")
print(serie_empleados)

print("Minúsculas")
print(serie_empleados.str.lower())

print("Mayúsculas")
print(serie_empleados.str.upper())

print("Longitud de los nombres")
print(serie_empleados.str.len())

print("Contienen el apellido Rodríguez")
print(serie_empleados.str.contains("Rodríguez"))

print("Reemplazar el apellido Rodríguez")
print(serie_empleados.str.replace("Rodríguez", "Lepon"))