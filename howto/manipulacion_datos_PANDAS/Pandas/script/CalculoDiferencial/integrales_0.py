#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 09:39:38 2026

@author: moleculax
"""

import sympy as sp

# 1. Definir la variable simbólica
x = sp.Symbol('x')

# 2. Definir la función
funcion = 3*x**2 + sp.exp(x)

# 3. Calcular la integral indefinida respecto a x
integral_indefinida = sp.integrate(funcion, x)

print("Función original:", funcion)
print("Integral (sin la constante C):", integral_indefinida)
# Resultado: x**3 + exp(x)
