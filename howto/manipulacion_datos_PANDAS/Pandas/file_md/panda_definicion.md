# 🐼 ¿Qué es Pandas?

## 📌 Definición
**Pandas** es una librería de Python de código abierto diseñada para el **análisis y manipulación de datos**.  
Se construye sobre **NumPy** y proporciona estructuras de datos flexibles y eficientes para trabajar con información tabular y series temporales.

---

## 🔑 Estructuras principales
- **[Series](ca://s?q=Que_es_pandas_Series)** → estructura unidimensional con etiquetas, similar a un array.  
- **[DataFrame](ca://s?q=Que_es_pandas_DataFrame)** → estructura bidimensional similar a una tabla de SQL o Excel, con filas e índices etiquetados.

---

## 📊 Capacidades destacadas
- **[Manejo de datos faltantes](ca://s?q=Manejo_de_datos_faltantes_en_pandas)** (`NaN`) de forma sencilla.  
- **[Mutabilidad de tamaño](ca://s?q=Mutabilidad_de_tamano_en_pandas)** → se pueden agregar/eliminar columnas y filas dinámicamente.  
- **[Alineación automática](ca://s?q=Alineacion_automatica_en_pandas)** de datos por etiquetas.  
- **[GroupBy](ca://s?q=GroupBy_en_pandas)** → agrupamiento para aplicar operaciones de agregación y transformación.  
- **[Entrada/Salida](ca://s?q=Entrada_y_salida_en_pandas)** → lectura y escritura en CSV, Excel, SQL, JSON, HDF5, entre otros.  
- **[Series temporales](ca://s?q=Series_temporales_en_pandas)** → generación de rangos de fechas, estadísticas móviles, desplazamientos y conversiones de frecuencia.

---

## 📑 Ejemplo básico
```python
import pandas as pd

# Crear un DataFrame
df = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "María"],
    "Edad": [23, 35, 29]
})

# Operaciones básicas
print(df.head())       # primeras filas
print(df["Edad"].mean())  # promedio de la columna Edad
```
## Resultado

```
  Nombre  Edad
0    Ana    23
1   Luis    35
2  María    29
29.0
```
