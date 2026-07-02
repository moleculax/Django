#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:48:07 2026

@author: moleculax
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mariadb
import pandas as pd

try:
    conexion = mariadb.connect(
        host="localhost",
        user="admin",
        password="admin123",
        database="bd_neurocode",
        port=3306
    )
    print("Conexión exitosa a MariaDB")
    
    cursor = conexion.cursor()
    
    # Ejecutar SELECT
    cursor.execute("SELECT * FROM paises")
    
    # Obtener nombres de columnas
    columnas = [desc[0] for desc in cursor.description]
    
    # Obtener resultados
    resultados = cursor.fetchall()
    
    # Mostrar resultados
    print("\nDatos de la tabla 'paises':")
    print("-" * 50)
    
    # Mostrar encabezados
    print(" | ".join(columnas))
    print("-" * 50)
    
    # Mostrar filas
    for fila in resultados:
        print(" | ".join(str(valor) for valor in fila))
    
    print("-" * 50)
    print(f"Total de registros: {len(resultados)}")
    
    cursor.close()
    conexion.close()
    print("Conexión cerrada")
    
except mariadb.Error as e:
    print(f"Error: {e}")