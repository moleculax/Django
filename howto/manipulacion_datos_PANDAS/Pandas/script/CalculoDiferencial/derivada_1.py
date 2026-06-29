#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 09:35:56 2026

@author: moleculax
"""

import sympy as sp

# 1. Definir la variable simbólica
x = sp.Symbol('x')

# 2. Definir la función
funcion = (3*x**2 + 5)**4

# 3. Calcular la derivada respecto a x
derivada = sp.diff(funcion, x)

print("Función original:", funcion)
print("Su derivada es:", derivada)
# Resultado: 24*x*(3*x**2 + 5)**3
