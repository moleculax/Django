#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para leer CSV con año y temperatura y graficar
@author: moleculax
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# ============================================
# 1. CREAR CSV DE EJEMPLO (si no tienes)
# ============================================

if not os.path.exists('temperaturas.csv'):
    datos = {
        'Año': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
        'Temperatura': [73.0, 73.2, 75.3, 72.4, 72.5, 74.4, 74.9, 74.6, 73.5, 72.7, 74.6, 73.5, 74.0, 75.1, 76.2, 74.8]
    }
    df = pd.DataFrame(datos)
    df.to_csv('temperaturas.csv', index=False)
    print("✅ Archivo temperaturas.csv creado")
else:
    print("📁 Archivo temperaturas.csv ya existe")

# ============================================
# 2. LEER CSV Y DETECTAR COLUMNAS
# ============================================

df = pd.read_csv('temperaturas.csv')

# MOSTRAR NOMBRES DE COLUMNAS (PARA DEPURAR)
print("\n📋 Nombres de columnas ORIGINALES:")
print(df.columns.tolist())

# RENOMBRAR COLUMNAS (ESTANDARIZAR)
# Primero, convertir nombres a minúsculas y eliminar espacios
df.columns = df.columns.str.strip().str.lower()

print("\n📋 Nombres de columnas NORMALIZADOS:")
print(df.columns.tolist())

# Verificar qué columnas existen
columnas_existentes = df.columns.tolist()
print(f"\n📋 Columnas disponibles: {columnas_existentes}")

# Si hay solo una columna (problema de separador), intentar con otro separador
if len(df.columns) == 1:
    print("\n⚠️ Parece que el archivo no usa coma como separador. Intentando con punto y coma...")
    df = pd.read_csv('temperaturas.csv', sep=';')
    df.columns = df.columns.str.strip().str.lower()
    print(f"📋 Columnas detectadas: {df.columns.tolist()}")

# ============================================
# 3. VERIFICAR Y USAR COLUMNAS
# ============================================

# Buscar columnas que contengan 'año' o 'temp'
col_año = None
col_temp = None

for col in df.columns:
    if 'año' in col or 'ano' in col or 'year' in col:
        col_año = col
    if 'temp' in col or 'temperatura' in col:
        col_temp = col

if col_año is None:
    print("❌ No se encontró columna de año. Usando primera columna como año.")
    col_año = df.columns[0]

if col_temp is None:
    print("❌ No se encontró columna de temperatura. Usando segunda columna como temperatura.")
    col_temp = df.columns[1] if len(df.columns) > 1 else df.columns[0]

print(f"\n📋 Usando columna de año: '{col_año}'")
print(f"📋 Usando columna de temperatura: '{col_temp}'")

# Crear columnas estandarizadas
df['año'] = df[col_año]
df['temperatura'] = df[col_temp]

print("\n" + "="*50)
print("📊 DATOS DE TEMPERATURAS")
print("="*50)

print("\n📋 Vista previa:")
print(df[['año', 'temperatura']].head())

print("\n📋 Información:")
print(df[['año', 'temperatura']].info())

print("\n📋 Estadísticas básicas:")
print(df[['año', 'temperatura']].describe())

print(f"\n📋 Total de registros: {len(df)}")

# ============================================
# 4. FILTRAR DATOS
# ============================================

print("\n" + "="*50)
print("🔍 FILTROS")
print("="*50)

# Filtrar años recientes (desde 2020)
df_reciente = df[df['año'] >= 2020]
print(f"\n📋 Años desde 2020:")
print(df_reciente[['año', 'temperatura']])

# Año con temperatura máxima
max_temp = df.loc[df['temperatura'].idxmax()]
print(f"\n📋 Año con temperatura máxima: {max_temp['año']} - {max_temp['temperatura']}°F")

# Año con temperatura mínima
min_temp = df.loc[df['temperatura'].idxmin()]
print(f"\n📋 Año con temperatura mínima: {min_temp['año']} - {min_temp['temperatura']}°F")

# Temperatura promedio
print(f"\n📋 Temperatura promedio: {df['temperatura'].mean():.2f}°F")

# Temperatura máxima y mínima
print(f"📋 Temperatura máxima: {df['temperatura'].max()}°F")
print(f"📋 Temperatura mínima: {df['temperatura'].min()}°F")

# ============================================
# 5. GRAFICAR (3 TIPOS DE GRÁFICOS)
# ============================================

print("\n" + "="*50)
print("📈 GRAFICANDO...")
print("="*50)

# Crear carpeta para gráficos si no existe
if not os.path.exists('graficos'):
    os.makedirs('graficos')

# ---------- GRÁFICO 1: LÍNEA ----------
plt.figure(figsize=(12, 6))
plt.plot(df['año'], df['temperatura'], marker='o', color='red', linestyle='-', linewidth=2, markersize=8)
plt.title('Evolución de Temperaturas (Línea)', fontsize=16)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Temperatura (°F)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(df['año'], rotation=45)
plt.tight_layout()
plt.savefig('graficos/grafico_linea.png', dpi=300, bbox_inches='tight')
print("✅ Gráfico de línea guardado: graficos/grafico_linea.png")

# ---------- GRÁFICO 2: BARRAS ----------
plt.figure(figsize=(12, 6))
colores = ['green' if t < 74 else 'orange' if t < 75 else 'red' for t in df['temperatura']]
plt.bar(df['año'], df['temperatura'], color=colores, edgecolor='black', linewidth=0.5)
plt.title('Temperaturas por Año (Barras)', fontsize=16)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Temperatura (°F)', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.xticks(df['año'], rotation=45)
plt.tight_layout()
plt.savefig('graficos/grafico_barras.png', dpi=300, bbox_inches='tight')
print("✅ Gráfico de barras guardado: graficos/grafico_barras.png")

# ---------- GRÁFICO 3: DISPERSIÓN CON TENDENCIA ----------
plt.figure(figsize=(12, 6))
plt.scatter(df['año'], df['temperatura'], color='blue', s=100, alpha=0.7)

# Línea de tendencia
z = np.polyfit(df['año'], df['temperatura'], 1)
p = np.poly1d(z)
plt.plot(df['año'], p(df['año']), "r--", linewidth=2, label='Tendencia')

plt.title('Temperaturas con Línea de Tendencia', fontsize=16)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Temperatura (°F)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(df['año'], rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('graficos/grafico_dispersion.png', dpi=300, bbox_inches='tight')
print("✅ Gráfico de dispersión guardado: graficos/grafico_dispersion.png")

# ---------- MOSTRAR TODOS LOS GRÁFICOS ----------
plt.show()

# ============================================
# 6. RESUMEN FINAL
# ============================================

print("\n" + "="*50)
print("📋 RESUMEN FINAL")
print("="*50)
print(f"📁 Archivo: temperaturas.csv")
print(f"📊 Total de años: {len(df)}")
print(f"🌡️ Temperatura promedio: {df['temperatura'].mean():.2f}°F")
print(f"🔥 Temperatura máxima: {df['temperatura'].max()}°F")
print(f"❄️ Temperatura mínima: {df['temperatura'].min()}°F")
print(f"📈 Año más caluroso: {max_temp['año']} ({max_temp['temperatura']}°F)")
print(f"📉 Año más frío: {min_temp['año']} ({min_temp['temperatura']}°F)")
print("\n📂 Gráficos guardados en la carpeta 'graficos/'")