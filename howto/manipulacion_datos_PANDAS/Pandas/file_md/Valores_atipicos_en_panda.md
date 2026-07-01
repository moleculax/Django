# Guía de Valores Atípicos (Outliers) en Pandas

Un **valor atípico** (o *outlier*) es un dato que se desvía de forma extrema del resto de los valores en un conjunto de datos. En Pandas, identificar y gestionar estos valores es fundamental, ya que pueden sesgar los análisis estadísticos y arruinar el rendimiento de los modelos de Machine Learning.

---

## 📌 ¿Por qué aparecen los valores atípicos?

1. **Errores de captura:** Equivocaciones humanas al digitar datos (ej. escribir `1550000` en lugar de `155000`).
2. **Eventos especiales genuinos:** Comportamientos reales pero estacionales del negocio (ej. el pico de ventas en Diciembre por Navidad).
3. **Fallas de hardware:** Sensores dañados o mal calibrados que arrojan mediciones absurdas.

---

## 🛠️ Métodos de Detección en Pandas

### 1. Método del Rango Intercuartílico (IQR)
Es el método más utilizado cuando los datos **no siguen una distribución normal** (tienen sesgos o asimetrías). Utiliza las funciones `.quantile()`, `.abs()`, o filtros lógicos booleanos.

* **Q1 (Percentil 25):** El valor por debajo del cual está el 25% de los datos.
* **Q3 (Percentil 75):** El valor por debajo del cual está el 75% de los datos.
* **IQR (Rango Intercuartílico):** La distancia entre Q3 y Q1 (`Q3 - Q1`).

#### Implementación en Código:
```python
# 1. Calcular cuartiles y el IQR
Q1 = df['ventas'].quantile(0.25)
Q3 = df['ventas'].quantile(0.75)
IQR = Q3 - Q1

# 2. Definir límites (usando el umbral estándar de 1.5)
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# 3. Filtrar los valores atípicos
valores_atipicos = df[(df['ventas'] < limite_inferior) | (df['ventas'] > limite_superior)]
```

### 2. Método de Z-Score (Puntuación Z)
Se utiliza cuando los datos **siguen una distribución normal** (curva de campana de Gauss). Mide a cuántas desviaciones estándar se encuentra un dato respecto a la media. 

Todo dato con un Z-Score mayor a **3** o menor a **-3** se considera atípico.

#### Implementación en Código:
```python
media = df['ventas'].mean()
desviacion = df['ventas'].std()

# Calcular el Z-Score para cada fila
df['z_score'] = (df['ventas'] - media) / desviacion

# Filtrar atípicos
valores_atipicos_z = df[df['z_score'].abs() > 3]
```

---

## 📊 ¿Qué hacer con los valores atípicos en Pandas?

Una vez identificados mediante los filtros anteriores, existen tres caminos posibles en Pandas:

### A. Eliminarlos (Trimming)
Útil si confirmas que los datos son errores o ruido que no aporta valor.
```python
# Mantener solo los datos que están DENTRO de los límites permitidos
df_limpio = df[(df['ventas'] >= limite_inferior) & (df['ventas'] <= limite_superior)]
```

### B. Mantenerlos
Obligatorio si tu análisis busca justamente detectar anomalías (ej. detección de fraudes bancarios o caídas críticas de servidores).

### C. Imputarlos (Capping / Winsorización)
Consiste en reemplazar el valor atípico por un tope máximo admisible (como el valor de los límites calculados) o por la mediana, para no perder la fila completa del DataFrame.
```python
import numpy as np

# Reemplazar valores que superan el límite superior por el valor del límite superior
df['ventas_ajustadas'] = np.where(df['ventas'] > limite_superior, limite_superior, df['ventas'])
```
