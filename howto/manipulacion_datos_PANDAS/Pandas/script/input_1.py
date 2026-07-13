#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 20:10:04 2026

@author: moleculax
"""


while True:
    num1 = input("Ingrese el primer número: ")
    try:
        num1 = int(num1)
        break
    except ValueError:
        print("Error: El primer número no es un número entero.")

# Pedimos la entrada del segundo número al usuario
while True:
    num2 = input("Ingrese el segundo número: ")
    try:
        num2 = int(num2)
        if num2 == 0 and num1 != 0:
            print("Error: No se puede dividir por cero.")
        else:
            break
    except ValueError:
        print("Error: El segundo número no es^[[A un número entero.")

# Calculamos algo simple
suma = (num1 ** 2) + num2

# Mostramos el resultado
print("resultado", suma)


