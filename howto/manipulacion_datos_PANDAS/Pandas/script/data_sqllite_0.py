#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:17:35 2026

@author: moleculax
"""

import sqlite3

# 1. Definición de la clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def mostrar_saldo(self):
        return f"Cuenta de {self.titular}: ${self.saldo}"

    def depositar(self, monto):
        self.saldo += monto
        return f"💰 Se depositaron ${monto} a {self.titular}."


# ========================================================
# CONFIGURACIÓN DE SQLITE Y DATOS DE PRUEBA
# ========================================================

# Creamos una base de datos temporal en la memoria RAM (":memory:")
conexion = sqlite3.connect(":memory:")
cursor = conexion.cursor()

# Creamos la tabla de clientes
cursor.execute("""
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titular TEXT,
        saldo REAL
    )
""")

# Insertamos datos simulados en la base de datos
datos_iniciales = [("Ana", 500.0), ("Pedro", 100.0), ("María", 750.0)]
cursor.executemany("INSERT INTO clientes (titular, saldo) VALUES (?, ?)", datos_iniciales)
conexion.commit()


# ========================================================
# RECORRER LA BASE DE DATOS USANDO EL CONSTRUCTOR
# ========================================================

# Ejecutamos la consulta para traer todas las cuentas
cursor.execute("SELECT titular, saldo FROM clientes")
filas_db = cursor.fetchall()  # Retorna una lista de tuplas: [('Ana', 500.0), ...]

# Lista donde guardaremos las instancias de objetos CuentaBancaria
cuentas_vivas = []

# Recorremos cada registro de la base de datos pasándolo por el constructor
for fila in filas_db:
    # fila[0] es el titular, fila[1] es el saldo
    nuevo_objeto = CuentaBancaria(titular=fila[0], saldo_inicial=fila[1])
    cuentas_vivas.append(nuevo_objeto)


# ========================================================
# VERIFICACIÓN: TRABAJANDO CON LOS OBJETOS CREADOS
# ========================================================
print("--- Cuentas cargadas desde SQLite y convertidas a objetos ---")
for cuenta in cuentas_vivas:
    print(cuenta.mostrar_saldo())

print("\n--- Modificando los datos en los objetos creados ---")
# Modificamos el objeto de Ana (índice 0 en la lista)
print(cuentas_vivas[0].depositar(250))
print(cuentas_vivas[0].mostrar_saldo())

# Cerramos la conexión a la base de datos al finalizar
conexion.close()
