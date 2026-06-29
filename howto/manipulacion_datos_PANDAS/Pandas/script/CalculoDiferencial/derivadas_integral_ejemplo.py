#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 09:32:37 2026

@author: moleculax
"""

import sympy as sp

x = sp.Symbol('x')

# Calcular la derivada exacta de x^2 + sin(x)
derivada = sp.diff(x**2 + sp.sin(x), x)
print(derivada)  # 2*x + cos(x)

# Resolver una integral indefinida exacta
integral = sp.integrate(sp.cos(x), x)
print(integral)  # sin(x)
