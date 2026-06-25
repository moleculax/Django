#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:11:29 2026
@author: moleculax
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# Conectar a la base de datos SQLite
conexion = sqlite3.connect("database/db.sqlite3")

# Consulta SQL
query = """
        SELECT
        id,
        producto,
        cantidad,
        precio_unitario, 
        total,
        fecha,
        cliente_id
        FROM ventas
        ORDER BY fecha
"""

# Ejecutar consulta SQL y cargar en DataFrame
df = pd.read_sql_query(query, conexion)

# Cerrar conexión
conexion.close()

# Mostrar datos
print("Datos de ventas:")
print(df)

# Crear carpeta para graficos si no existe
if not os.path.exists('graficos'):
    os.makedirs('graficos')

# Grafico 1: Ventas por producto (Barras)
plt.figure(figsize=(12, 6))
ventas_producto = df.groupby('producto')['total'].sum().sort_values(ascending=True)
ventas_producto.plot(kind='barh', color='steelblue')
plt.title('Ventas Totales por Producto', fontsize=16)
plt.xlabel('Total Ventas ($)', fontsize=12)
plt.ylabel('Producto', fontsize=12)
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('graficos/ventas_por_producto.png', dpi=300, bbox_inches='tight')
print("Grafico guardado: graficos/ventas_por_producto.png")

# Grafico 2: Evolucion de ventas (Linea)
plt.figure(figsize=(12, 6))
df['fecha'] = pd.to_datetime(df['fecha'])
ventas_por_fecha = df.groupby(df['fecha'].dt.date)['total'].sum()
plt.plot(ventas_por_fecha.index, ventas_por_fecha.values, marker='o', color='green', linewidth=2)
plt.title('Evolucion de Ventas por Fecha', fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Total Ventas ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('graficos/evolucion_ventas.png', dpi=300, bbox_inches='tight')
print("Grafico guardado: graficos/evolucion_ventas.png")

# Grafico 3: Distribucion por cliente (Torta)
plt.figure(figsize=(10, 10))
ventas_cliente = df.groupby('cliente_id')['total'].sum()
plt.pie(ventas_cliente.values, labels=ventas_cliente.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribucion de Ventas por Cliente', fontsize=16)
plt.tight_layout()
plt.savefig('graficos/ventas_por_cliente.png', dpi=300, bbox_inches='tight')
print("Grafico guardado: graficos/ventas_por_cliente.png")

# Grafico 4: Cantidad vs Total (Dispersion)
plt.figure(figsize=(10, 6))
plt.scatter(df['cantidad'], df['total'], color='red', alpha=0.6, s=100)
plt.title('Relacion Cantidad vs Total', fontsize=16)
plt.xlabel('Cantidad', fontsize=12)
plt.ylabel('Total ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('graficos/cantidad_vs_total.png', dpi=300, bbox_inches='tight')
print("Grafico guardado: graficos/cantidad_vs_total.png")

print("\nTodos los graficos guardados en la carpeta 'graficos/'")

# Mostrar estadisticas
print("\nEstadisticas:")
print(f"Total de registros: {len(df)}")
print(f"Total de ventas: ${df['total'].sum():,.2f}")
print(f"Promedio por venta: ${df['total'].mean():,.2f}")
print(f"Venta maxima: ${df['total'].max():,.2f}")
print(f"Venta minima: ${df['total'].min():,.2f}")


plt.show()