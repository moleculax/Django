# El Histograma

Un **histograma** es un gráfico estadístico utilizado para representar la **distribución de una variable numérica continua**. A diferencia de un gráfico de barras común, su objetivo no es comparar categorías individuales, sino mostrar con qué frecuencia los datos caen dentro de ciertos rangos numéricos consecutivos.

---

## 🧱 ¿Cómo funciona un Histograma?

1. **Agrupación en Intervalos (*Bins*):** El eje horizontal (X) representa los valores de la variable analizada. Este rango total se divide en subintervalos de igual tamaño llamados *bins* o contenedores.
2. **Conteo de Frecuencias:** El eje vertical (Y) mide la cantidad de datos (frecuencia) que caen dentro de cada intervalo.
3. **Construcción de Barras:** Se dibuja una barra sobre cada intervalo. La altura de la barra es directamente proporcional al número de registros que pertenecen a ese rango.

---

## ⚖️ Histograma vs. Gráfico de Barras

Es común confundirlos, pero tienen diferencias estructurales críticas:

| Característica | Histograma | Gráfico de Barras |
| :--- | :--- | :--- |
| **Tipo de Variable** | Una sola variable **numérica continua** (ej. Edad, Salario, Altura). | Variables **cualitativas / categorías** (ej. Género, Mes, País). |
| **Espacio entre barras** | Las barras van **pegadas** (indican continuidad numérica). | Las barras van **separadas** (indican categorías independientes). |
| **Orden** | El orden es estrictamente matemático y cronológico de izquierda a derecha. | El orden puede ser arbitrario o alfabético. |

---

## 📐 Formas Comunes de un Histograma y su Significado

La silueta que forman las barras permite entender el comportamiento físico o social de los datos de un solo vistazo:

* **Distribución Normal (Campana de Gauss):** Simétrica. Las barras más altas están en el centro y descienden uniformemente hacia los extremos. Indica un comportamiento estándar (ej. pesos, estaturas).
* **Sesgado a la Derecha (Asimetría Positiva):** Las barras más altas están al principio (izquierda) y dejan una "cola" larga hacia valores altos. Típico en el análisis de salarios o precios de viviendas.
* **Bimodal:** Presenta dos picos altos separados por un valle. Indica que el conjunto de datos probablemente contiene dos poblaciones o grupos internos con comportamientos muy distintos.

---

## 💻 Implementación en Python con Seaborn

En ciencia de datos con Python, la forma más rápida y estética de generar un histograma es utilizando la función `sns.histplot()` de **Seaborn**:

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar el estilo visual de Seaborn
sns.set_theme(style="whitegrid")

# Crear el histograma
# - bins=10: Divide los datos en 10 intervalos iguales
# - kde=True: Añade una línea de densidad suavizada sobre las barras
sns.histplot(data=df_estudiantes, x="Edad", bins=10, kde=True, color="skyblue")

# Personalizar títulos con Matplotlib
plt.title("Distribución de Edades de los Estudiantes", fontsize=14)
plt.xlabel("Edad (Años)")
plt.ylabel("Cantidad de Estudiantes")

# Mostrar el gráfico en pantalla
plt.show()
```
