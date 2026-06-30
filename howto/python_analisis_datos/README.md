
# Conocimientos Esenciales de Python para Análisis de Datos

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white) ![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white) ![Scikit_Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white) ![Anaconda](https://img.shields.io/badge/Anaconda-44A833?style=for-the-badge&logo=anaconda&logoColor=white)

Para dominar Python enfocado seriamente en el **Análisis de Datos**, no basta con conocer la sintaxis básica (bucles, condicionales y funciones). Es necesario especializarse en el manejo eficiente de estructuras de datos en memoria, vectorización y manipulación de grandes volúmenes de información.

---

## 1. Estructuras de Datos Avanzadas y Comprensiones
Antes de tocar librerías externas, debes exprimir el potencial nativo de Python para procesar datos de forma limpia y eficiente.

* **List, Dictionary y Set Comprehensions:** Elementales para transformar y filtrar colecciones de datos en una sola línea de código sin recurrir a bucles `for` tradicionales, lo que optimiza el rendimiento.
* **Manejo de Mutabilidad:** Entender a fondo la diferencia entre objetos mutables e inmutables para evitar errores sutiles al copiar o modificar estructuras de datos.
* **Módulo `collections`:** Dominar herramientas específicas como `Counter` (para conteos rápidos), `defaultdict` y `namedtuple`.

---

## 2. NumPy: Cómputo Numérico y Vectorización
NumPy es la base de todo el ecosistema de datos en Python. Aunque rara vez analices datos usando solo NumPy, sus conceptos gobiernan el comportamiento de librerías superiores como Pandas.

* **El objeto `ndarray`:** Comprender cómo almacena los datos en bloques de memoria contiguos (a diferencia de las listas de Python) para operaciones a alta velocidad.
* **Vectorización:** Aprender a eliminar los bucles `for` reemplazándolos por operaciones matemáticas directas entre arrays.
* **Broadcasting:** Entender las reglas que dictan cómo NumPy opera con arrays de diferentes dimensiones.
* **Indexación Avanzada y Máscaras Booleanas:** Filtrar datos de manera masiva utilizando matrices de verdaderos/falsos (e.g., `data[data > 0]`).

---

## 3. Pandas: Manipulación Estructural de Datos
Es la herramienta central del analista de datos. Aquí es donde debes pasar la mayor parte del tiempo especializándote.

* **DataFrames y Series:** Domina la alineación interna de datos basada en índices.
* **Indexación y Selección Eficiente:** Saber cuándo y por qué usar `.loc`, `.iloc` y evitar el *SettingWithCopyWarning* (un error clásico al asignar valores a subconjuntos de datos).
* **Agregaciones y Agrupamientos:** Dominar el patrón **Split-Apply-Combine** mediante el uso exhaustivo de `.groupby()`, `.agg()` y tablas dinámicas (`pivot_table`).
* **Limpieza de Datos Compleja:** Tratamiento avanzado de valores nulos (`fillna`, `dropna`), eliminación de duplicados, transformaciones de texto con `.str` y mapeo de valores.
* **Combinación de datasets:** Dominar las diferencias mecánicas entre `.merge()` (uniones tipo SQL), `.join()` y `.concat()`.
* **Manejo de Series Temporales (Time Series):** Conversión de fechas, remuestreo (`resample`), ventanas móviles (`rolling`) y manejo de zonas horarias.

---

## 4. Visualización de Datos (Lógica y Personalización)
No se trata solo de generar gráficos genéricos, sino de saber estructurarlos para responder preguntas de negocio.

* **Matplotlib (La base):** Entender la arquitectura de capas (la diferencia entre `Figure` y `Axes`). Saber cómo modificar cada pixel, etiqueta, color y eje de un gráfico manualmente.
* **Seaborn (Análisis Estadístico):** Dominar los gráficos relacionales, de distribución y categóricos (`sns.heatmap`, `sns.pairplot`, `sns.boxplot`). Aprender a usar el argumento `hue` para segmentar datos visualmente de inmediato.

---

## 5. Optimización y Rendimiento con Grandes Volúmenes
Cuando los datasets no caben cómodamente en la memoria RAM, el enfoque estándar cambia.

* **Tipos de Datos Eficientes (`dtypes`):** Aprender a reducir drásticamente el uso de memoria convirtiendo columnas `object` a `category`, o reduciendo la precisión de flotantes y enteros (e.g., de `float64` a `float32`).
* **Lectura por bloques (Chunking):** Utilizar el parámetro `chunksize` en `read_csv` para procesar archivos gigantescos por partes.

---

## 6. Integración con Entornos y Formatos de Archivos
* **Ecosistema Jupyter:** Dominar atajos de teclado, comandos mágicos (`%timeit`, `%matplotlib inline`) y la ejecución de entornos interactivos.
* **Formatos de almacenamiento eficientes:** Ir más allá del CSV. Aprender a leer y escribir en formatos optimizados para analítica como **Parquet** o **HDF5**, que conservan los tipos de datos y comprimen el espacio.



[Elaborado por EjGomez](https://moleculaxapp.vercel.app/)