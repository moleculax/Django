#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.client
import json
import pandas as pd

# 1. Creamos la estructura usando una lista de diccionarios (fila por fila) para evitar el problema de formato
filas_ventas = [
    {"Producto": "Laptop", "Cantidad": 2, "Precio_Unitario": 1200, "Categoría": "Electrónica"},
    {"Producto": "Mouse Inalámbrico", "Cantidad": 15, "Precio_Unitario": 25, "Categoría": "Accesorios"},
    {"Producto": "Monitor 4K", "Cantidad": 4, "Precio_Unitario": 450, "Categoría": "Electrónica"},
    {"Producto": "Teclado Mecánico", "Cantidad": 8, "Precio_Unitario": 90, "Categoría": "Accesorios"},
    {"Producto": "Laptop", "Cantidad": 1, "Precio_Unitario": 1200, "Categoría": "Electrónica"}
]

df = pd.DataFrame(filas_ventas)

# Calculamos el total de cada venta con Pandas
df['Total_Venta'] = df['Cantidad'] * df['Precio_Unitario']

# 2. Convertimos el DataFrame a texto para Ollama
tabla_texto = df.to_string(index=False)

# 3. Prompt de análisis
prompt_inteligente = f"""
Actúa como un analista de datos experto. Analiza la siguiente tabla de ventas y dame un resumen muy breve en viñetas que incluya:
1. Cuál fue el producto que generó más ingresos totales.
2. Una conclusión o recomendación rápida sobre el inventario.

Aquí tienes los datos:
{tabla_texto}
"""

# 4. Petición HTTP directa a Ollama
payload = {
    "model": "llama3.2",
    "prompt": prompt_inteligente,
    "stream": False
}

try:
    print("1. Procesando datos con Pandas...")
    print("2. Enviando DataFrame a Ollama (llama3.2)...")
    
    conn = http.client.HTTPConnection("127.0.0.1", 11434, timeout=45)
    data_json = json.dumps(payload).encode('utf-8')
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    
    conn.request("POST", "/api/generate", body=data_json, headers=headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    
    if response.status == 200:
        resultado = json.loads(data)
        print("\n=== ANÁLISIS DE INTELIGENCIA ARTIFICIAL ===")
        print(resultado['response'])
        print("===========================================")
    else:
        print(f"\nError de Ollama: {response.status}")
        
    conn.close()

except Exception as e:
    print(f"\n❌ Error en el proceso: {e}")
