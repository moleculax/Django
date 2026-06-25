import pandas as pd

ventas = {
    'ventas': [10000, 12000, 15000, 18000, 20000, 22000, 15000, 18000],
    'cantidad': [10, 40, 20, 10, 6, 10, 9, 8],
    'ciudad': ["cumana", "cumana", "caracas", "barcelona",
               "carupano", "cumana", "caracas", "barcelona"]
}

indice = pd.MultiIndex.from_tuples([
     ('Electrónicos', 'Laptop', 'En línea'),
     ('Electrónicos', 'Tableta', 'En tienda'),
     ('Electrónicos', 'Teléfonos', 'En línea'),
     ('Ropa', 'Camiseta', 'En tienda'),
     ('Ropa', 'Medias', 'En línea'),
     ('Ropa', 'Vestido', 'En línea'),
     ('Hogar', 'Alfombras', 'En tienda'),
     ('Hogar', 'Cortinas', 'En tienda'),
], names=['Categoria', 'Producto', 'Canal_Ventas'])

df_tienda = pd.DataFrame(ventas, index=indice)

print("DataFrame completo:")
print(df_tienda)

print("\nAcceder a los datos")
print(df_tienda.loc['Hogar'])  # Filtrar por categoría
print(df_tienda.xs('En tienda', level='Canal_Ventas'))  # Filtrar por canal

print("\nOrdenamiento")
df_ordenamiento = df_tienda.sort_index(
    axis=0,
    level=['Categoria', 'Producto'],
    ascending=[True, True]
)
print(df_ordenamiento)
