#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:02:47 2026
@author: moleculax
"""

import sqlite3

# Conectar (crea el archivo si no existe)
conn = sqlite3.connect("database/db.sqlite3")
cursor = conn.cursor()

# Verificar si la tabla existe
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ventas';")
tabla = cursor.fetchone()

# SQL para crear la tabla ventas
sql_crear_ventas = """
CREATE TABLE ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto TEXT NOT NULL,
    cantidad INTEGER NOT NULL CHECK(cantidad > 0),
    precio_unitario REAL NOT NULL CHECK(precio_unitario >= 0),
    total REAL GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cliente_id INTEGER
);
"""

if tabla:
    print("✅ La tabla 'ventas' ya existe.")
else:
    print("⚠️ La tabla 'ventas' no existe. Creándola ahora...")
    cursor.execute(sql_crear_ventas)
    print("✅ Tabla 'ventas' creada correctamente.")

conn.commit()
conn.close()