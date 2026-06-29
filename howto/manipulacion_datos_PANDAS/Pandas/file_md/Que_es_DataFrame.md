# Estructura de Datos Central:
# El DataFrame de Pandas

El **DataFrame** es la estructura de datos bidimensional más utilizada en la biblioteca **Pandas**. Diseñado para el manejo de datos tabulares estructurados, combina la flexibilidad de los diccionarios de Python con la velocidad de cálculo de los arreglos de NumPy.

---

### 1. Características Fundamentales

*   **Estructura Bidimensional:** Los datos se organizan formalmente en un eje de filas (Eje 0) y un eje de columnas (Eje 1). Es el equivalente directo a una tabla de base de datos SQL o a una hoja de cálculo de Excel.
*   **Heterogeneidad de Columnas:** A diferencia de las matrices de NumPy, un DataFrame es **heterogéneo**. Cada columna puede almacenar un tipo de dato diferente (enteros, flotantes, strings, booleanos o fechas), manteniendo la homogeneidad dentro de una misma columna.
*   **Mutabilidad de Tamaño y Datos:** Es posible modificar los valores de las celdas, añadir nuevas filas/columnas o eliminar canales de información existentes sin necesidad de reconstruir la estructura en memoria.
*   **Indexación Doble:** 
    *   **Índice de filas (`index`):** Identifica de forma única cada registro. Puede ser secuencial numérico (`0, 1, ... N`) o un índice etiquetado (como fechas o nombres de usuario).
    *   **Índice de columnas (`columns`):** Etiquetas de texto o numéricas que identifican cada variable o atributo del dataset.

---

### 2. Contexto Histórico y Evolución de Estructuras

Originalmente, Pandas se diseñó en torno a tres estructuras principales correlacionadas por su dimensionalidad:
1.  **Series (1D):** Estructura unidimensional etiquetada, similar a una columna individual. Un DataFrame es, internamente, un conjunto de Series alineadas bajo el mismo índice.
2.  **DataFrame (2D):** Estructura bidimensional estándar para la gran mayoría de operaciones de Data Science.
3.  **Panel (3D):** Estructura tridimensional utilizada para manejar datos en contenedores cúbicos. *Nota histórica:* El objeto **Panel fue depreciado** a partir de la versión 0.20.0 y eliminado por completo de la librería. Hoy en día, los datos con más de dos dimensiones se manejan de forma más eficiente mediante **MultiIndex** (índices jerárquicos) en DataFrames bidimensionales.

---

### 3. Métodos Esenciales de Construcción

Un DataFrame se puede instanciar invocando al constructor `pd.DataFrame(data, index, columns)` alimentándolo de diversas fuentes de datos nativas y externas:

#### A. A partir de Diccionarios (Orientado a Columnas)
Es la forma más intuitiva. Las llaves del diccionario se transforman automáticamente en los nombres de las columnas y las listas asociadas representan las filas verticales.
```python
import pandas as pd

datos_dict = {
    "Producto": ["Laptop", "Celular", "Tablet"],
    "Precio":,
    "Stock":,
}
df_dict = pd.DataFrame(datos_dict)
```

#### B. A partir de Matrices de NumPy (Orientado a Matrices Matemáticas)
Ideal cuando se trabaja con computación científica. Al no tener metadatos nativos, las etiquetas de las filas y columnas se deben proveer de forma explícita o Pandas las generará numéricamente por defecto.
```python
import numpy as np

matriz = np.array([[10, 20], [30, 40], [50, 60]])
df_matriz = pd.DataFrame(matriz, columns=["Variable_A", "Variable_B"])
```

#### C. A partir de una Lista de Tuplas o Listas (Orientado a Filas)
Cada elemento de la lista principal representa un registro horizontal independiente (fila). Las columnas se mapean según la posición indexada de los elementos de la tupla.
```python
datos_tuplas = [
    ("Pepo Lepon", 25, "Cumana"),
    ("Lupe Lepon", 32, "Barcelona"),
    ("Koki Lepon", 28, "Caracas"),
]
df_tuplas = pd.DataFrame(datos_tuplas, columns=["Nombre", "Edad", "Ciudad"])
```
