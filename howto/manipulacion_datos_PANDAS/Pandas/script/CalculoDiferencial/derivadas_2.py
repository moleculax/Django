#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 09:38:09 2026

@author: moleculax
"""

import sympy as sp

t = sp.Symbol('t')

# Ecuación de posición
posicion = t**3 - 6*t**2 + 9*t

# Primera derivada = Velocidad
velocidad = sp.diff(posicion, t)

# Segunda derivada = Aceleración (derivamos la velocidad)
aceleracion = sp.diff(velocidad, t)

print("Posición (s):", posicion)
print("Velocidad (v):", velocidad)       # Resultado: 3*t**2 - 12*t + 9
print("Aceleración (a):", aceleracion)   # Resultado: 6*t - 12
