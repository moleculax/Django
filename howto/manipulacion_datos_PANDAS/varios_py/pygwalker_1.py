import pandas as pd
import pygwalker as pyg

# 1. Creamos un dataset ficticio de ejemplo (con los datos completados)
data = {
    'Producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado', 'Laptop', 'Monitor', 'Mouse', 'Teclado'],
    'Categoría': ['Hardware', 'Accesorios', 'Hardware', 'Accesorios', 'Hardware', 'Hardware', 'Accesorios', 'Accesorios'],
    'Ventas_USD': [1200, 25, 350, 45, 1100, 400, 30, 50],
    'Cantidad': [3, 10, 5, 8, 2, 4, 12, 7],
    'Fecha': ['2026-01-01', '2026-01-02', '2026-01-02', '2026-01-03', '2026-01-04', '2026-01-05', '2026-01-05', '2026-01-06']
}

df = pd.DataFrame(data)
df['Fecha'] = pd.to_datetime(df['Fecha'])

print(" DataFrame creado:")
print(df)
print("\n" + "="*50)

# 2. Lanzamos la interfaz interactiva de PyGWalker
walker = pyg.walk(df)