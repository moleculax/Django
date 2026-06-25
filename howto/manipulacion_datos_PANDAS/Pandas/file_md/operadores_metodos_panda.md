# 📊 Operadores y Métodos en Pandas

## 🔢 Operadores aritméticos
- **[+ (suma)](ca://s?q=Operador_suma_en_pandas)** → `df["col1"] + df["col2"]`
- **[- (resta)](ca://s?q=Operador_resta_en_pandas)** → `df["col1"] - df["col2"]`
- **[* (multiplicación)](ca://s?q=Operador_multiplicacion_en_pandas)** → `df["col1"] * df["col2"]`
- **[/ (división)](ca://s?q=Operador_division_en_pandas)** → `df["col1"] / df["col2"]`
- **[// (división entera)](ca://s?q=Operador_division_entera_en_pandas)** → `df["col1"] // df["col2"]`
- **[% (módulo)](ca://s?q=Operador_modulo_en_pandas)** → `df["col1"] % df["col2"]`
- **[** (potencia)](ca://s?q=Operador_potencia_en_pandas)** → `df["col1"] ** 2`

---

## 🔍 Operadores de comparación
- **[== (igualdad)](ca://s?q=Operador_igualdad_en_pandas)** → `df["col1"] == df["col2"]`
- **[!= (diferente)](ca://s?q=Operador_diferente_en_pandas)** → `df["col1"] != df["col2"]`
- **[> (mayor que)](ca://s?q=Operador_mayor_que_en_pandas)** → `df["col1"] > 50`
- **[< (menor que)](ca://s?q=Operador_menor_que_en_pandas)** → `df["col1"] < 100`
- **[>= (mayor o igual)](ca://s?q=Operador_mayor_o_igual_en_pandas)**
- **[<= (menor o igual)](ca://s?q=Operador_menor_o_igual_en_pandas)**

---

## ⚙️ Operadores lógicos
- **[& (AND)](ca://s?q=Operador_AND_en_pandas)** → `(df["col1"] > 10) & (df["col2"] < 50)`
- **[| (OR)](ca://s?q=Operador_OR_en_pandas)** → `(df["col1"] > 10) | (df["col2"] < 50)`
- **[~ (NOT)](ca://s?q=Operador_NOT_en_pandas)** → `~(df["col1"] > 10)`

---

## 📑 Métodos aritméticos equivalentes
- **[add](ca://s?q=pandas_add_method)** → suma (`s1.add(s2)`)
- **[sub](ca://s?q=pandas_sub_method)** → resta (`s1.sub(s2)`)
- **[mul](ca://s?q=pandas_mul_method)** → multiplicación (`s1.mul(s2)`)
- **[div](ca://s?q=pandas_div_method)** → división (`s1.div(s2)`)
- **[mod](ca://s?q=pandas_mod_method)** → módulo (`s1.mod(s2)`)
- **[pow](ca://s?q=pandas_pow_method)** → potencia (`s1.pow(2)`)

---

## 📊 Métodos estadísticos y de agregación
- **[sum](ca://s?q=pandas_sum_method)** → suma de valores
- **[mean](ca://s?q=pandas_mean_method)** → promedio
- **[median](ca://s?q=pandas_median_method)** → mediana
- **[std](ca://s?q=pandas_std_method)** → desviación estándar
- **[min](ca://s?q=pandas_min_method)** / **[max](ca://s?q=pandas_max_method)** → mínimo y máximo
- **[count](ca://s?q=pandas_count_method)** → cuenta de elementos no nulos
- **[describe](ca://s?q=pandas_describe_method)** → resumen estadístico

---

## 🔍 Métodos de selección y filtrado
- **[loc](ca://s?q=pandas_loc_method)** → selección por etiquetas
- **[iloc](ca://s?q=pandas_iloc_method)** → selección por índices numéricos
- **[query](ca://s?q=pandas_query_method)** → filtrar con expresiones SQL-like
- **[isin](ca://s?q=pandas_isin_method)** → filtrar por pertenencia a una lista

---

## 🛠️ Métodos de transformación
- **[apply](ca://s?q=pandas_apply_method)** → aplicar función a cada elemento
- **[map](ca://s?q=pandas_map_method)** → transformar valores de una `Series`
- **[replace](ca://s?q=pandas_replace_method)** → reemplazar valores
- **[fillna](ca://s?q=pandas_fillna_method)** → rellenar valores nulos
- **[dropna](ca://s?q=pandas_dropna_method)** → eliminar valores nulos
- **[astype](ca://s?q=pandas_astype_method)** → cambiar tipo de datos

---

## 📑 Métodos de estructura
- **[head](ca://s?q=pandas_head_method)** → primeras filas
- **[tail](ca://s?q=pandas_tail_method)** → últimas filas
- **[shape](ca://s?q=pandas_shape_method)** → dimensiones del DataFrame
- **[info](ca://s?q=pandas_info_method)** → información general
- **[columns](ca://s?q=pandas_columns_method)** → nombres de columnas
- **[index](ca://s?q=pandas_index_method)** → índice del DataFrame



# 📊 Tabla de Operadores y Métodos en Pandas

| **Operador** | **Método equivalente** | **Ejemplo** |
|--------------|-------------------------|-------------|
| **[+ (suma)](ca://s?q=Operador_suma_en_pandas)** | **[add](ca://s?q=pandas_add_method)** | `df["A"] + df["B"]` / `df["A"].add(df["B"])` |
| **[- (resta)](ca://s?q=Operador_resta_en_pandas)** | **[sub](ca://s?q=pandas_sub_method)** | `df["A"] - df["B"]` / `df["A"].sub(df["B"])` |
| **[* (multiplicación)](ca://s?q=Operador_multiplicacion_en_pandas)** | **[mul](ca://s?q=pandas_mul_method)** | `df["A"] * df["B"]` / `df["A"].mul(df["B"])` |
| **[/ (división)](ca://s?q=Operador_division_en_pandas)** | **[div](ca://s?q=pandas_div_method)** | `df["A"] / df["B"]` / `df["A"].div(df["B"])` |
| **[// (división entera)](ca://s?q=Operador_division_entera_en_pandas)** | **[floordiv](ca://s?q=pandas_floordiv_method)** | `df["A"] // df["B"]` / `df["A"].floordiv(df["B"])` |
| **[% (módulo)](ca://s?q=Operador_modulo_en_pandas)** | **[mod](ca://s?q=pandas_mod_method)** | `df["A"] % df["B"]` / `df["A"].mod(df["B"])` |
| **[** (potencia)](ca://s?q=Operador_potencia_en_pandas)** | **[pow](ca://s?q=pandas_pow_method)** | `df["A"] ** 2` / `df["A"].pow(2)` |


## Ejemplo

```

import pandas as pd

lista_numerica = [20,30,40,50,60,70,80]
lista_numerica2 = [20,30,40,50,60,70,80]

# Crear DataFrame con ambas listas
df = pd.DataFrame({
    "lista1": lista_numerica,
    "lista2": lista_numerica2
})

# Columna con la suma
df["suma"] = df["lista1"] + df["lista2"]

print(df)
```

## Resultado

```
   lista1  lista2  suma
0      20      20    40
1      30      30    60
2      40      40    80
3      50      50   100
4      60      60   120
5      70      70   140
6      80      80   160
```
