# 🐼 Valores faltantes en Pandas

## 📌 Definición
En pandas, los valores faltantes se representan como **NaN** (Not a Number).  
Detectarlos y tratarlos es esencial para un análisis de datos correcto.

---

## 🔍 Identificación de valores faltantes
- **[isnull()](ca://s?q=pandas_isnull_method)** → Devuelve `True` en posiciones con valores faltantes.  
- **[notnull()](ca://s?q=pandas_notnull_method)** → Devuelve `True` en posiciones con valores válidos.  
- **[isna()](ca://s?q=pandas_isna_method)** → Alias de `isnull()`.  
- **[notna()](ca://s?q=pandas_notna_method)** → Alias de `notnull()`.  

### Ejemplo
```python
import pandas as pd

df = pd.DataFrame({
    "Nombre": ["Ana", "Luis", None],
    "Edad": [23, None, 29]
})

print(df.isnull())       # Muestra True/False por celda
print(df.isnull().sum()) # Cuenta NaN por columna
```

## ⚙️ Manejo de valores faltantes
**dropna()** → elimina filas/columnas con NaN.

**fillna()** → reemplaza NaN con un valor específico.

**interpolate()** → rellena valores faltantes usando interpolación.

```
# Eliminar filas con NaN
df_clean = df.dropna()

# Rellenar NaN con un valor fijo
df_fill = df.fillna(0)

# Interpolación lineal
df_interp = df.interpolate()
```

## 📑 Resumen rápido
- Usa df.isnull().sum() para contar valores faltantes por columna.

- Usa dropna() si prefieres eliminar registros incompletos.

- Usa fillna() o interpolate() si necesitas conservar los datos rellenando huecos.

## ✅ Conclusión
La correcta identificación y tratamiento de valores faltantes en pandas asegura que los análisis sean más confiables y evita sesgos en los resultados.