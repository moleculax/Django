# 📊 Visualización con Matplotlib en Pandas

## 📌 Introducción
Pandas integra funciones de **visualización** basadas en [Matplotlib](ca://s?q=Que_es_matplotlib), lo que permite crear gráficos directamente desde **Series** y **DataFrames** sin necesidad de escribir mucho código adicional.

---

## 🔑 Características
- Los métodos `.plot()` de pandas usan **matplotlib** como backend.  
- Permite generar gráficos de líneas, barras, histogramas, dispersión, etc.  
- Se pueden personalizar títulos, etiquetas y estilos.  

---

## 📑 Ejemplo básico
```python
import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo
data = {
    "Nombre": ["Ana", "Luis", "María"],
    "Edad": [23, 35, 29],
    "Salario": [2500, 4000, 3200]
}

df = pd.DataFrame(data)

# Gráfico de barras de salarios
df.plot(x="Nombre", y="Salario", kind="bar", title="Salarios por empleado")

plt.show()

```

## Ejemplo

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:45:30 

@author: moleculax
"""

import pandas as pd
import matplotlib.pyplot as plt

diccionario_temperaturas = {
    2010: 73,
    2011: 73.2,
    2012: 75.3,
    2013: 72.4,
    2014: 72.5,
    2015: 74.4,
    2016: 74.9,
    2017: 74.6,
    2018: 73.5,
    2019: 72.7,
    2020: 74.6,
    2021: 73.5,
}

serie_temperaturas= pd.Series(diccionario_temperaturas)

serie_temperaturas.plot(
    title='Temperaturas del 2010 al 2021',
    marker='o',
    color='green',
    xlabel='Años',
    ylabel='Temperaturas'
)

```

## Resultado

