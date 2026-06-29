# NumPy en Python

**NumPy** (Numerical Python) es la librería fundamental para el cómputo científico en Python. Proporciona estructuras de datos avanzadas y herramientas matemáticas de alto rendimiento para manejar grandes volúmenes de datos numéricos.

---

### ¿Por qué se utiliza NumPy?

* **Rendimiento extremo**: Está escrito en C, lo que hace que los cálculos sean hasta 100 veces más rápidos que las listas nativas de Python.
* **Menos memoria**: Consume mucha menos memoria RAM al almacenar los datos en bloques contiguos.
* **Operaciones vectorizadas**: Permite aplicar operaciones matemáticas a bloques enteros de datos sin usar bucles `for`.

---

### El Objeto Central: `ndarray`

La estructura principal es el arreglo multidimensional o **`ndarray`**. A diferencia de las listas de Python, todos sus elementos deben ser del **mismo tipo de datos** (generalmente números).

```python
import numpy as np

# Crear un arreglo de 1 dimensión (Vector)
vector = np.array([1, 2, 3, 4])

# Crear un arreglo de 2 dimensiones (Matriz)
matriz = np.array([[1, 2], [3, 4]])
```

---

### Características Clave

* ** Broadcasting**: Capacidad de realizar operaciones aritméticas entre arreglos de diferentes formas (shapes).
* **Funciones Matemáticas**: Incluye álgebra lineal, transformadas de Fourier, generación de números aleatorios y trigonometría.
* **Base de Data Science**: Es el motor interno sobre el cual están construidas librerías como **Pandas, SciPy, Scikit-learn y TensorFlow**.
