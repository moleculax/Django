# Seaborn (Visualización de Datos Estadísticos)

**Seaborn** es una librería de Python especializada en la **visualización de datos estadísticos**. Está construida sobre **Matplotlib** y diseñada para integrarse perfectamente con las estructuras de datos de **Pandas** (DataFrames).

Su objetivo principal es transformar el análisis exploratorio de datos en un proceso rápido, intuitivo y estéticamente profesional.

---

## 🌟 Características Principales

* **Estilo profesional por defecto:** Genera gráficos con paletas de colores sofisticadas y diseños limpios sin necesidad de configuración adicional.
* **Integración nativa con Pandas:** Permite pasar un DataFrame completo y especificar las columnas por su nombre de texto.
* **Automatización estadística:** Calcula de forma interna líneas de tendencia, distribuciones numéricas e intervalos de confianza.

---

## 🎨 Seaborn vs. Matplotlib

| Característica | Matplotlib | Seaborn |
| :--- | :--- | :--- |
| **Nivel** | Bajo nivel (Motor gráfico). | Alto nivel (Capa estadística). |
| **Código** | Requiere muchas líneas para gráficos complejos. | Gráficos complejos en una sola línea. |
| **Estética** | Básica y plana por defecto. | Moderna y atractiva por defecto. |
| **Uso ideal** | Personalizar detalles (ejes, títulos, ventanas). | Explorar relaciones y patrones estadísticos. |

> **Nota:** No compiten entre sí. En la práctica se usan juntos: Seaborn dibuja el gráfico estadístico y Matplotlib controla la ventana, los títulos o el guardado del archivo.

---

## 📊 Gráficos más Utilizados en Data Science

### 1. Mapa de Calor (`sns.heatmap`)
Ideal para visualizar matrices de correlación. Representa la fuerza de la relación entre variables numéricas mediante intensidades de color.
```python
sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm')
```

### 2. Diagrama de Caja (`sns.boxplot`)
El gráfico estándar para detectar **valores atípicos** (*outliers*) y analizar la dispersión de los datos a través de cuartiles.
```python
sns.boxplot(x='Departamento', y='Salario', data=df)
```

### 3. Gráfico de Dispersión (`sns.scatterplot`)
Dibuja puntos en un plano cartesiano para evaluar visualmente si existe una relación o tendencia entre dos variables cuantitativas.
```python
sns.scatterplot(x='Horas_Estudio', y='Nota_Final', data=df)
```

### 4. Histograma (`sns.histplot`)
Muestra la distribución y frecuencia de una variable numérica continua (permite añadir una curva de densidad con `kde=True`).
```python
sns.histplot(df['Edad'], kde=True)
```

---

## 🚀 Instalación Rápida

Para instalar Seaborn junto con sus dependencias básicas en tu entorno de desarrollo:

```bash
pip install seaborn matplotlib pandas
```
