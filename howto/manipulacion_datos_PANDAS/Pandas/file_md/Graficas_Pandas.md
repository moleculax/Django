## Crear gráficas en Pandas 
Es un proceso directo porque la librería integra internamente a Matplotlib. Esto significa que puedes dibujar visualizaciones profesionales llamando al método .plot() directamente desde tus DataFrames o Series, sin necesidad de configurar estructuras complejas desde cero.

![Reporte de Retornos](https://raw.githubusercontent.com/moleculax/Django/main/howto/manipulacion_datos_PANDAS/Pandas/script/graficos/reporte_retornos.png)


## Paso 1:
Importar las librerías necesariasAunque Pandas genera el gráfico, necesitas importar matplotlib.pyplot para controlar el despliegue (mostrar o guardar la imagen)

```
import matplotlib.pyplot as plt
import pandas as pd
```

## Paso 2: 
Preparar y limpiar tus datosAntes de graficar, asegúrate de que tus datos no tengan valores nulos en las columnas clave y que los tipos de datos sean numéricos.

```
# Ejemplo: Crear un DataFrame de ventas semanales
datos = {
    "Semana": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
    "Zapatos":,
    "Camisas":,
}
df = pd.DataFrame(datos)

```


## Paso 3:
Invocar el método .plot() especificando el tipoEl parámetro principal es kind, el cual define la estructura geométrica del gráfico. Las opciones más utilizadas son:
- kind='line': Gráfico de líneas (ideal para tendencias temporales).
- kind='bar': Barras verticales (comparaciones de categorías
- kind='barh': Barras horizontales (ideal para textos largos de categorías).
- kind='hist': Histograma (distribución de frecuencias de variables numéricas).
- kind='box': Diagrama de caja y bigotes (para detectar valores atípicos/outliers).
- kind='scatter': Gráfico de dispersión (relación entre dos variables numéricas).

```
# Ejemplo de gráfico de líneas definiendo los ejes X e Y
df.plot(kind="line", x="Semana", y="Zapatos")
```

## Paso 4:
Personalizar la estética del gráficoPuedes pasar parámetros directamente dentro de .plot() para mejorar la visualización:
- color: Define el color de los elementos (ej. 'skyblue', 'red') o listas de colores.
- grid: Si se establece en True, añade una cuadrícula de fondo.
- figsize: Una tupla (ancho, alto) en pulgadas para ajustar las dimensiones del lienzo.
- title: El título principal de la gráfica.

```
df.plot(
    kind="bar",
    x="Semana",
    y=["Zapatos", "Camisas"],
    figsize=(10, 5),
    grid=True,
    title="Reporte Mensual de Ventas",
)
```

## Paso 5:
Controlar el destino (Mostrar o Guardar)Pandas construye el objeto gráfico en la memoria de Python, pero necesitas indicarle explícitamente qué hacer con él utilizando comandos de Matplotlib al final de tu script:
- Para verlo en pantalla: Usa plt.show().
- Para guardarlo en el disco duro: Usa plt.savefig('ruta/nombre.png').


```
# Ajusta los márgenes automáticamente para que no se corten los textos
plt.tight_layout()

# Guardar el archivo en alta calidad
plt.savefig("graficos/ventas.png", dpi=300)

# Liberar la memoria RAM cerrando la figura
plt.close()

```
