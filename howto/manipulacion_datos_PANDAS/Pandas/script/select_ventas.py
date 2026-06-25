#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:11:29 2026

@author: moleculax
"""

import sqlite3
import pandas as pd

# Conectar a la base de datos SQLite
conexion = sqlite3.connect("database/db.sqlite3")

# Consulta SQL en formato multilínea
query = """
        SELECT
        cantidad,
        precio_unitario, 
        total,
        fecha
        FROM ventas
"""

# Ejecutar consulta SQL y cargar en DataFrame
df = pd.read_sql_query(query, conexion)

# Mostrar resultados
print(df)

# Cerrar conexión
conexion.close()
