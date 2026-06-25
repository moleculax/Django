#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificar datos insertados
"""

import sqlite3
import json

conn = sqlite3.connect("database/db.sqlite3")
cursor = conn.cursor()

cursor.execute("SELECT id, producto, cantidad, precio_unitario, total, fecha, cliente_id FROM ventas;")
rows = cursor.fetchall()

# Obtener nombres de columnas
cursor.execute("PRAGMA table_info(ventas);")
columnas = [col[1] for col in cursor.fetchall()]

# Convertir a lista de diccionarios
data = []
for row in rows:
    data.append(dict(zip(columnas, row)))

# Imprimir JSON
print(json.dumps(data, indent=4, ensure_ascii=False, default=str))

conn.close()