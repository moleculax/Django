# Técnicas Avanzadas: Optimización de Memoria en Pandas y Máscaras Booleanas en NumPy

Cuando se trabaja con grandes volúmenes de datos, el rendimiento y el uso de la memoria RAM se vuelven críticos. A continuación, se detallan las dos técnicas fundamentales para optimizar tus scripts de análisis.

---

## 1. Optimización de Memoria en Pandas

Por defecto, Pandas suele asignar tipos de datos (`dtypes`) muy pesados a las columnas (como `int64` o `float64`), o interpreta las cadenas de texto como objetos genéricos (`object`). Optimizar estos tipos puede reducir el uso de memoria hasta en un 80%.

### A. Conversión a Tipos Numéricos de Menor Precisión (Downcasting)
Si una columna contiene números pequeños (por ejemplo, valores del 1 al 100), no necesita un entero de 64 bits (`int64`). Puedes reducirlo a 8 bits (`int8`).

```python
import pandas as pd
import numpy as np

# Crear un DataFrame de ejemplo pesado
df = pd.DataFrame({'edad': np.random.randint(0, 100, size=1000000)})
print(df.memory_usage(deep=True)) # Muestra el consumo inicial

# Optimizar la columna numérica
df['edad'] = pd.to_numeric(df['edad'], downcast='integer')
print(df.memory_usage(deep=True)) # Muestra el consumo optimizado
```

## B. Uso del Tipo category para Textos Repetitivos
Las columnas de tipo object (strings) consumen mucha memoria. Si la columna tiene una cardinalidad baja (muchos valores repetidos, como "País", "Género", "Estado"), cambiarla a category almacena los textos únicos una sola vez y asigna enteros internamente.

```
# Columna con alta repetición de strings
df['ciudad'] = np.random.choice(['Madrid', 'Barcelona', 'Valencia'], size=1000000)

# Conversión a categoría
df['ciudad'] = df['ciudad'].astype('category')

```

## C. Carga de Datos por Bloques (Chunking)
Si un archivo CSV es más grande que tu memoria RAM disponible, puedes procesarlo en fragmentos más pequeños en lugar de cargarlo por completo.

```
# Procesar un archivo gigante en bloques de 50,000 filas
chunk_size = 50000
for chunk in pd.read_csv('archivo_gigante.csv', chunksize=chunk_size):
    # Realizar filtrados o agregaciones por cada bloque
    procesar_datos(chunk)
```

## 2. Máscaras Booleanas en NumPy
Las máscaras booleanas permiten filtrar, seleccionar y modificar elementos de un array de manera masiva mediante la aplicación de condiciones lógicas, eliminando por completo la necesidad de usar bucles for (vectorización).

## A. Creación y Aplicación de una Máscara
Cuando aplicas una condición a un array de NumPy, no obtienes los valores directamente, sino un nuevo array de la misma dimensión lleno de valores True y False.
    
    

```
import numpy as np

# Crear un array unidimensional
edades = np.array([12, 25, 47, 18, 60, 15, 31])

# Crear la máscara booleana (¿Quién es mayor de edad?)
mascara = edades >= 18
# Resultado: array([False,  True,  True,  True,  True, False,  True])

# Aplicar la máscara para filtrar los datos originales
mayores = edades[mascara]
# Resultado: array([25, 47, 18, 60, 31])
```
## B. Condiciones Múltiples (Operadores Bitwise)
Para combinar múltiples condiciones en NumPy, se deben usar los operadores lógicos bit a bit (& para AND, | para OR) y envolver cada condición entre paréntesis.

```
valores = np.array([10, 20, 30, 40, 50, 60])

# Filtrar valores mayores a 15 Y menores o iguales a 50
condicion = (valores > 15) & (valores <= 50)
resultado = valores[condicion]
# Resultado: array([20, 30, 40, 50])
```

## C. Modificación de Datos Basada en Condiciones
Las máscaras no solo sirven para extraer datos, sino también para alterarlos de forma selectiva en una sola línea de ejecución.

```
puntuaciones = np.array([4.5, 7.2, 3.1, 8.5, 4.9])

# A todos los que tengan menos de 5.0, asignarles un 5.0 directo
puntuaciones[puntuaciones < 5.0] = 5.0
# Resultado: array([5. , 7.2, 5. , 8.5, 5. ])
```

