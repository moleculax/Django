#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:47:13 2026

@author: moleculax
"""

import os
import sqlite3
import matplotlib.pyplot as plt
import numpy as np


# ========================================================
# 1. DATOS INICIALES 
# ========================================================
datos_completos = [
    ("Ana López", 1500.50, "Sueldo", "2024-01-15", 1),
    ("Pedro Gómez", 120.00, "Corriente", "2025-06-20", 1),
    ("María Casal", 7500.00, "Ahorro", "2023-11-02", 1),
    ("Carlos Ruiz", 0.00, "Sueldo", "2025-02-10", 0),
    ("Pedro Lepon", 0.00, "Sueldo", "2025-04-10", 0),
]


# ========================================================
# 2. ARRAY DE OBJETOS
# ========================================================
array_de_objetos = []


# ========================================================
# 3. DEFINICIÓN DE LA CLASE
# ========================================================
class CuentaBancaria:

    def __init__(self, id, titular, saldo, tipo_cuenta, fecha_apertura, activa):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        self.tipo = tipo_cuenta
        self.fecha = fecha_apertura
        self.activa = bool(activa)

    def mostrar_ficha_completa(self):
        estado = "🟢 Activa" if self.activa else "🔴 Suspendida"
        return (
            f"ID: {self.id} | Cliente: {self.titular:<8} | "
            f"Tipo: {self.tipo:<10} | Saldo: ${self.saldo:<6} | "
            f"Creada: {self.fecha} | Estado: {estado}"
        )


# ========================================================
# 4. CONEXIÓN A LA BASE DE DATOS
# ========================================================
NOMBRE_DB = "database/banco.db"

conexion = sqlite3.connect(NOMBRE_DB)
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()


# ========================================================
# 5. CREAR TABLA SI NO EXISTE
# ========================================================
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        titular TEXT,
        saldo REAL,
        tipo_cuenta TEXT,
        fecha_apertura TEXT,
        activa INTEGER
    )
""")


# ========================================================
# 6. INSERTAR DATOS (SIEMPRE)
# ========================================================
cursor.executemany(
    """
    INSERT INTO clientes (titular, saldo, tipo_cuenta, fecha_apertura, activa)
    VALUES (?, ?, ?, ?, ?)
""",
    datos_completos,
)
conexion.commit()


# ========================================================
# 7. SELECT: CARGAR DATOS AL ARRAY DE OBJETOS
# ========================================================
cursor.execute("SELECT * FROM clientes")
filas_db = cursor.fetchall()

for fila in filas_db:
    diccionario_datos = dict(fila)
    if 'id_cliente' in diccionario_datos:
        diccionario_datos['id'] = diccionario_datos.pop('id_cliente')
    nuevo_objeto_cliente = CuentaBancaria(**diccionario_datos)
    array_de_objetos.append(nuevo_objeto_cliente)

conexion.close()


# ========================================================
# 8. MOSTRAR LOS DATOS
# ========================================================
print("=" * 60)
print("📋 LISTA DE CLIENTES")
print("=" * 60)
for objeto_cuenta in array_de_objetos:
    print(objeto_cuenta.mostrar_ficha_completa())

print(f"\n✅ Total de objetos en el array: {len(array_de_objetos)}")


# ========================================================
# 9. GRÁFICO DE SALDOS POR CLIENTE
# ========================================================
print("\n" + "=" * 60)
print("📊 GENERANDO GRÁFICO DE SALDOS...")
print("=" * 60)

# Extraer datos para el gráfico
nombres = [obj.titular for obj in array_de_objetos]
saldos = [obj.saldo for obj in array_de_objetos]
estados = [obj.activa for obj in array_de_objetos]

# Colores: verde para activos, rojo para inactivos
colores = ['#4CAF50' if estado else '#F44336' for estado in estados]

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
bars = plt.bar(nombres, saldos, color=colores, edgecolor='black', linewidth=1.2)

# Agregar valores encima de las barras
for bar, saldo in zip(bars, saldos):
    plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 50,
             f'${saldo:,.2f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.title('💰 Saldos por Cliente', fontsize=16, fontweight='bold')
plt.xlabel('Cliente', fontsize=12)
plt.ylabel('Saldo ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Agregar leyenda personalizada
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#4CAF50', label='🟢 Activa'),
    Patch(facecolor='#F44336', label='🔴 Suspendida')
]
plt.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()

# Guardar gráfico
os.makedirs('graficos', exist_ok=True)
plt.savefig('graficos/saldos_clientes.png', dpi=100)
print("✅ Gráfico guardado en: graficos/saldos_clientes.png")

# Mostrar gráfico
plt.show()