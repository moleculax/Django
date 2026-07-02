#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mariadb
import pandas as pd
import os

# Crear carpeta
os.makedirs("archivos_csv", exist_ok=True)

try:
    conexion = mariadb.connect(
        host="localhost",
        user="admin",
        password="admin123",
        database="bd_neurocode",
        port=3306
    )
    print("Conexion exitosa a MariaDB")
    
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM paises")
    
    columnas = [desc[0] for desc in cursor.description]
    resultados = cursor.fetchall()
    
    df = pd.DataFrame(resultados, columns=columnas)
    
    ruta_archivo = "archivos_csv/paises.csv"
    df.to_csv(ruta_archivo, index=False, encoding='utf-8')
    print("CSV guardado: " + ruta_archivo)
    print("Total registros: " + str(len(df)))
    
    cursor.close()
    conexion.close()
    print("Conexion cerrada")
    
except mariadb.Error as e:
    print("Error DB: " + str(e))