# 📊 DataFrame en Pandas

## 📌 Definición
Un **[DataFrame](ca://s?q=Que_es_pandas_DataFrame)** es la estructura de datos principal de pandas.  
Se asemeja a una **tabla de Excel o SQL**, con filas e índices etiquetados y columnas con nombres.  
Permite almacenar y manipular datos de manera eficiente.

---

## 🔑 Características principales
- **Estructura bidimensional** (filas y columnas).  
- **Etiquetas de filas y columnas** para acceso rápido.  
- **Soporte para múltiples tipos de datos** en columnas diferentes.  
- **Operaciones vectorizadas** para cálculos eficientes.  
- **Integración con NumPy** y otras librerías científicas.  

---

## 📑 Crear un DataFrame

### Desde un diccionario
```python
import pandas as pd

data = {
    "Nombre": ["Ana", "Luis", "María"],
    "Edad": [23, 35, 29],
    "Salario": [2500, 4000, 3200]
}

df = pd.DataFrame(data)
print(df)

```

## Ejemplo Agregando datos

```
"""
Created on Wed Jun 24 12:36:15 2026

@author: moleculax
"""

import pandas as pd

df_clientes = pd.DataFrame({
  "nombre" : ["Luis", "Ana", "Sebastián", "Sofía", "Mateo", "Camila", "Valentín", "Isabella"],
  "edad" : [35, 30, 32, 41, 47, 23, 20, 28], 
  "cuidad" : ["Buenos Aires", "Lima", "Ciudad de México", "Santiago", "Alajuela", "Nueva York", "Toronto", "Río de Janeiro"]
})

lista_profesion = ["Médico", "Ingeniera civil", "Abogado", "Profesora", "Contador", "Enfermera", "Estudiante", "Periodista"]



df_clientes['profesion'] = lista_profesion


print(df_clientes)
```

## Resultado
```
      nombre  edad            cuidad        profesion
0       Luis    35      Buenos Aires           Médico
1        Ana    30              Lima  Ingeniera civil
2  Sebastián    32  Ciudad de México          Abogado
3      Sofía    41          Santiago        Profesora
4      Mateo    47          Alajuela         Contador
5     Camila    23        Nueva York        Enfermera
6   Valentín    20           Toronto       Estudiante
7   Isabella    28    Río de Janeiro       Periodista
```