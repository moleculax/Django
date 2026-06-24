# 📊 Funciones de Agregación en Pandas

## 📌 Definición
Las funciones de **agregación** en pandas permiten obtener **resúmenes estadísticos** de los datos, como sumas, promedios, mínimos y máximos.  
Se aplican tanto a **Series** como a **DataFrames**, y son muy útiles en análisis exploratorio.

---

## 🔑 Funciones principales

| **Función** | **Descripción** | **Ejemplo** |
|-------------|-----------------|-------------|
| **[sum](ca://s?q=pandas_sum_method)** | Suma de valores | `df["col"].sum()` |
| **[mean](ca://s?q=pandas_mean_method)** | Promedio | `df["col"].mean()` |
| **[median](ca://s?q=pandas_median_method)** | Mediana | `df["col"].median()` |
| **[min](ca://s?q=pandas_min_method)** | Valor mínimo | `df["col"].min()` |
| **[max](ca://s?q=pandas_max_method)** | Valor máximo | `df["col"].max()` |
| **[std](ca://s?q=pandas_std_method)** | Desviación estándar | `df["col"].std()` |
| **[var](ca://s?q=pandas_var_method)** | Varianza | `df["col"].var()` |
| **[count](ca://s?q=pandas_count_method)** | Número de valores no nulos | `df["col"].count()` |
| **[describe](ca://s?q=pandas_describe_method)** | Resumen estadístico | `df.describe()` |

---

## 📊 Ejemplo práctico
```python
import pandas as pd

df = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "María"],
    "Edad": [23, 35, 29],
    "Salario": [2500, 4000, 3200]
})

print("Suma de edades:", df["Edad"].sum())
print("Promedio de salarios:", df["Salario"].mean())
print("Resumen estadístico:\n", df.describe())
```

## 👉 Resultado:

```
Suma de edades: 87
Promedio de salarios: 3233.33
Resumen estadístico:
             Edad      Salario
count    3.000000     3.000000
mean    29.000000  3233.333333
std      6.000000   750.555349
min     23.000000  2500.000000
25%     26.000000  2850.000000
50%     29.000000  3200.000000
75%     32.000000  3600.000000
max     35.000000  4000.000000

```


## Ejemplo

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:10:18 

@author: moleculax
"""

import pandas as pd

salariosAnuales = [50230.0, 55123.0, 60089.0, 75020.0, 100987.0, 202345.0, 89000.0, 61200.0, 55300.0, 73400.0, 9520.0, 870000.0]
serie_salarios = pd.Series(salariosAnuales)
print(serie_salarios)

print("Total salarios:")
total_salarios = serie_salarios.sum()
print(total_salarios)

print("Promedio de salarios:")
promedio_salarios = serie_salarios.mean()
print(promedio_salarios)

print("Salario Máximo:")
maximo_salarios = serie_salarios.max()
print(maximo_salarios)

print("Salario Mínimo:")
minimo_salarios = serie_salarios.min()
print(minimo_salarios)

print("Mediana Salario:")
mediana_salarios = serie_salarios.median()
print(mediana_salarios)
```

## Resultado

```
0      50230.0
1      55123.0
2      60089.0
3      75020.0
4     100987.0
5     202345.0
6      89000.0
7      61200.0
8      55300.0
9      73400.0
10      9520.0
11    870000.0
dtype: float64
Total salarios:
1702214.0
Promedio de salarios:
141851.16666666666
Salario Máximo:
870000.0
Salario Mínimo:
9520.0
Mediana Salario:
67300.0
```

## Ejemplo

```
import pandas as pd

# Lista de diccionarios
salarios = [
  {"salario": 50230.0},
  {"salario": 55123.0},
  {"salario": 60089.0},
  {"salario": 75020.0},
  {"salario": 100987.0},
  {"salario": 202345.0},
  {"salario": 89000.0},
  {"salario": 61200.0},
  {"salario": 55300.0},
  {"salario": 73400.0},
  {"salario": 9520.0},
  {"salario": 870000.0}
]

# Convertir a DataFrame
df = pd.DataFrame(salarios)

# Calcular salario mayor y menor
salario_max = df["salario"].max()
salario_min = df["salario"].min()

print("Salario mayor:", salario_max)
print("Salario menor:", salario_min)

```

## Resultado

```
Salario mayor: 870000.0
Salario menor: 9520.0
```

## ⚙️ Uso con groupby
Las funciones de agregación se combinan con groupby para obtener estadísticas por grupo:

```
print(df.groupby("Nombre")["Salario"].mean())
```

### ✅ Conclusión
Las funciones de agregación en pandas son esenciales para:

- Resumir datos numéricos.

- Obtener estadísticas descriptivas.

- Analizar información por grupos.

Son la base del análisis exploratorio de datos en Python.