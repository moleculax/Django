## En Python, el método pivot
Se utiliza principalmente dentro de la librería Pandas para reestructurar o remodelar datos, transformando filas en columnas **(crear una tabla dinámica)** sin aplicar agregaciones numéricas. Su objetivo es cambiar el formato de los datos de "largo" (long format) a "ancho" (wide format) para que sean más legibles y fáciles de analizar.


## ¿Cómo funciona pivot?

El método DataFrame.pivot() organiza un conjunto de datos basándose en tres parámetros clave:
- index: La columna cuyos valores se convertirán en los nuevos índices de las filas.
- columns: La columna cuyos valores únicos se transformarán en las nuevas columnas de la tabla.
- values: La columna (o columnas) que contiene los datos numéricos o de texto que rellenarán las celdas resultantes.


### Diferencia crucial: `pivot()` vs `pivot_table()`

Es muy común confundir estas dos funciones en Pandas. Su diferencia principal radica en cómo manejan los datos duplicados:

* **`pivot()`**: Es para reestructuración básica.
* **No acepta datos duplicados** para una misma combinación de índice y columna.
* Si tuvieras dos registros de "Enero" y "Celulares", `pivot()` fallará y arrojará un error (`ValueError`).

* **`pivot_table()`**: Es la versión avanzada.
* **Sí permite agregaciones** como sumar, sacar promedios o contar.
* Si hay elementos duplicados, los combina usando una función matemática (por defecto, el promedio).
* Es el equivalente real a las tablas dinámicas de Excel.

---

### Resumen de usos comunes

* **Formatear reportes**: Presentar datos tabulares limpios de manera horizontal.
* **Preparar datos para gráficos**: Facilitar la creación de gráficos de líneas o barras.
* **Análisis de Series Temporales**: Alinear registros en las mismas fechas para diferentes categorías.

