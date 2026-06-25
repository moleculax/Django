

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:02:47 2026
@author: moleculax
"""

import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("database/db.sqlite3")
cursor = conn.cursor()

# Datos fijos
datos = [
    ("Laptop Lenovo ThinkPad", 2, 1200.00, 1),
    ("Mouse Logitech MX Master", 5, 80.00, 2),
    ("Teclado Mecánico Redragon", 3, 60.00, 1),
    ("Monitor Samsung 24''", 1, 350.00, 3),
    ("Disco SSD 1TB", 4, 120.00, 2),
    ("Memoria RAM 16GB", 6, 80.00, 4),
    ("Auriculares Sony WH-1000", 2, 250.00, 1),
    ("Cámara Web Logitech C920", 3, 100.00, 5),
    ("Impresora HP LaserJet", 1, 450.00, 3),
    ("Tablet Samsung Galaxy", 2, 300.00, 2),
    ("Celular iPhone 15", 1, 1200.00, 6),
    ("Smart TV LG 55''", 1, 800.00, 4),
    ("Parlante JBL Charge", 3, 150.00, 1),
    ("Proyector Epson", 1, 650.00, 7),
    ("Router TP-Link", 2, 90.00, 2),
    ("Disco Duro Externo 2TB", 3, 180.00, 5),
    ("Micrófono Blue Yeti", 2, 120.00, 3),
    ("Cargador USB-C 65W", 5, 40.00, 1),
    ("Hub USB-C 7 en 1", 4, 60.00, 2),
    ("Funda para Laptop 15.6''", 3, 30.00, 8)
]

# Insertar datos
inserts = """
INSERT INTO ventas (producto, cantidad, precio_unitario, cliente_id)
VALUES (?, ?, ?, ?);
"""

for i, (producto, cantidad, precio, cliente) in enumerate(datos, 1):
    cursor.execute(inserts, (producto, cantidad, precio, cliente))
    print(f"✅ Registro {i}: {producto} - {cantidad} x ${precio}")

conn.commit()
conn.close()

print("\n✅ 20 registros insertados correctamente.")