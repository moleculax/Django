#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:15:14 2026

@author: moleculax
"""

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def mostrar_saldo(self):
        return f"Cuenta de {self.titular}: ${self.saldo}"


# 1. Tu objeto de datos crudos (por ejemplo, una lista de diccionarios)
datos_clientes = [
    {"titular": "Ana", "saldo_inicial": 500},
    {"titular": "Pedro", "saldo_inicial": 100},
    {"titular": "María", "saldo_inicial": 750},
    {"titular": "Carlos", "saldo_inicial": 50}
]

# 2. Lista vacía para almacenar los objetos creados
cuentas_activas = []

# 3. Recorremos el objeto de datos usando un bucle 'for'
for cliente in datos_clientes:
    # Pasamos los datos del diccionario directamente al constructor
    nueva_cuenta = CuentaBancaria(
        titular=cliente["titular"], 
        saldo_inicial=cliente["saldo_inicial"]
    )
    # Guardamos el objeto recién creado en nuestra lista
    cuentas_activas.append(nueva_cuenta)

# ==========================================
# Verificación: Ahora tenemos una lista de OBJETOS
# ==========================================
print("--- Lista de objetos creados y procesados ---")
for cuenta in cuentas_activas:
    # Cada 'cuenta' es un objeto real con acceso a sus métodos
    print(cuenta.mostrar_saldo())
