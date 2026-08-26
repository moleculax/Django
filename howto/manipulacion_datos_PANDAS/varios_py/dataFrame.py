import pandas as pd
import matplotlib.pyplot as plt

datos = [
    {
        'mes': 'Enero',
        'total': 1200.56
     } ,
    {
        'mes': 'Febrero',
        'total': 1000.00
    },

    {
        'mes': 'Marzo',
        'total': 1400.00
    },


]

productos = [
    {
        'nombre': 'Producto A',
        'precio': 10.5
     },
    {
        'nombre': 'Producto B',
        'precio': 20.0
     },
]

df = pd.DataFrame(datos)
df.head()
dfmeseTotal = pd.DataFrame(datos)
dfproductos = pd.DataFrame(productos)

print(dfmeseTotal)
print(dfproductos)
# Cálculos estadísticos
total = dfmeseTotal['total'].sum()
promedio = dfmeseTotal['total'].mean()
maximo = dfmeseTotal['total'].max()
minimo = dfmeseTotal['total'].min()

print(f'\nEstadísticas de ventas:')
print(f'   Total: ${total:,.2f}')
print(f'   Promedio: ${promedio:,.2f}')
print(f'   Máximo: ${maximo:,.2f}')
print(f'   Mínimo: ${minimo:,.2f}')

path = 'graficos/'
barra = 'barra.png'
lineal = 'lineal.png'

plt.title('Total de ventas')
plt.xlabel('Meses')
plt.ylabel('Total')

# Crear lista de colores automática
colores = ['red' if x == dfmeseTotal['total'].min() else 'blue' for x in dfmeseTotal['total']]

plt.bar(dfmeseTotal['mes'], dfmeseTotal['total'], color=colores)
plt.savefig(f'{path}{barra}')
plt.show()


plt.title('Total de ventas')
plt.xlabel('Meses')
plt.ylabel('Total')

plt.plot(dfmeseTotal['mes'], dfmeseTotal['total'], marker='o')
plt.savefig(f'{path}{lineal}')
plt.show()
