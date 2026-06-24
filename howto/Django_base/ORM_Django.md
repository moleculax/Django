## ORM y Filtros en Django

## ¿Qué es el ORM?
El **ORM (Object Relational Mapper)** de Django es la capa que traduce instrucciones en Python a consultas SQL.  
- Permite **crear, leer, actualizar y borrar registros** en la base de datos usando objetos Python.  
- Evita que tengas que escribir SQL manualmente.  
- Garantiza portabilidad: puedes cambiar de motor de base de datos (PostgreSQL, MySQL, SQLite) sin modificar tu código de consultas.  

### Ejemplo conceptual
```python
# Crear registro
Objeto.objects.create(campo="valor")

# Leer registros
Objeto.objects.all()

# Actualizar
obj = Objeto.objects.get(id=1)
obj.campo = "nuevo valor"
obj.save()

# Borrar
obj.delete()
```

## Filtros en Django ORM
Los filtros (filter, exclude, get) permiten construir consultas con condiciones, de forma muy expresiva:

- filter → devuelve un conjunto de objetos que cumplen la condición.

- exclude → devuelve objetos que no cumplen la condición.

- get → devuelve un único objeto que cumple la condición (lanza error si hay más de uno o ninguno).

**Ejemplos generales**

```
# Filtrar por igualdad
Objeto.objects.filter(campo="valor")

# Filtrar por mayor/menor que
Objeto.objects.filter(numero__gt=10)   # mayor que 10
Objeto.objects.filter(numero__lte=5)   # menor o igual a 5

# Filtrar por texto
Objeto.objects.filter(nombre__icontains="abc")  # contiene "abc" sin importar mayúsculas

# Filtrar por rango
Objeto.objects.filter(fecha__range=["2026-01-01", "2026-12-31"])

```

##  Resumen en tabla

| **Acción**   | **Método ORM** | **Ejemplo** |
|--------------|----------------|-------------|
| Crear        | `create()`     | `Objeto.objects.create(campo="valor")` |
| Leer         | `all()`        | `Objeto.objects.all()` |
| Filtrar      | `filter()`     | `Objeto.objects.filter(campo="valor")` |
| Excluir      | `exclude()`    | `Objeto.objects.exclude(campo="valor")` |
| Obtener uno  | `get()`        | `Objeto.objects.get(id=1)` |
| Ordenar      | `order_by()`   | `Objeto.objects.order_by("campo")` |



## Filtros avanzados en Django ORM

| **Operador**   | **Uso**                        | **Ejemplo**                                      | **Resultado** |
|----------------|--------------------------------|--------------------------------------------------|---------------|
| `__gt`         | Mayor que                     | `Objeto.objects.filter(numero__gt=10)`           | Valores mayores a 10 |
| `__gte`        | Mayor o igual que             | `Objeto.objects.filter(numero__gte=10)`          | Valores ≥ 10 |
| `__lt`         | Menor que                     | `Objeto.objects.filter(numero__lt=5)`            | Valores menores a 5 |
| `__lte`        | Menor o igual que             | `Objeto.objects.filter(numero__lte=5)`           | Valores ≤ 5 |
| `__exact`      | Igualdad exacta               | `Objeto.objects.filter(nombre__exact="Juan")`    | Solo “Juan” |
| `__iexact`     | Igualdad sin mayúsculas       | `Objeto.objects.filter(nombre__iexact="juan")`   | “Juan”, “JUAN”, etc. |
| `__contains`   | Contiene (sensible a mayúsc.) | `Objeto.objects.filter(nombre__contains="an")`   | “Andrés”, “Manuel” |
| `__icontains`  | Contiene (insensible)         | `Objeto.objects.filter(nombre__icontains="an")`  | “Andrés”, “MANUEL” |
| `__startswith` | Comienza con                  | `Objeto.objects.filter(nombre__startswith="A")`  | Nombres que empiezan con “A” |
| `__istartswith`| Comienza con (insensible)     | `Objeto.objects.filter(nombre__istartswith="a")` | “Ana”, “andrés” |
| `__endswith`   | Termina con                   | `Objeto.objects.filter(nombre__endswith="z")`    | Nombres que terminan en “z” |
| `__iendswith`  | Termina con (insensible)      | `Objeto.objects.filter(nombre__iendswith="z")`   | “Luz”, “LUZ” |
| `__range`      | Dentro de un rango            | `Objeto.objects.filter(fecha__range=["2026-01-01","2026-12-31"])` | Fechas dentro de 2026 |
| `__year`       | Año específico                | `Objeto.objects.filter(fecha__year=2026)`        | Registros del año 2026 |
| `__month`      | Mes específico                | `Objeto.objects.filter(fecha__month=6)`          | Registros de junio |
| `__day`        | Día específico                | `Objeto.objects.filter(fecha__day=21)`           | Registros del día 21 |
| `__isnull`     | Valor nulo                    | `Objeto.objects.filter(campo__isnull=True)`      | Campos vacíos/nulos |


## Consultas encadenadas en Django ORM

En Django puedes **encadenar métodos** del ORM para construir consultas más complejas y expresivas.  
Cada método devuelve un `QuerySet`, lo que permite seguir aplicando filtros, ordenamientos o exclusiones.

---

##  Ejemplo general

```python
# Filtrar registros que cumplan varias condiciones
objetos = Objeto.objects.filter(
    campo1__icontains="abc"   # contiene "abc"
).filter(
    numero__gte=10            # número mayor o igual a 10
).exclude(
    estado="inactivo"         # excluir los inactivos
).order_by(
    "-fecha"                  # ordenar por fecha descendente
)

```

## Conclusión
El ORM de Django es la interfaz que te permite manipular la base de datos con objetos Python, y los filtros son la forma de construir consultas precisas sin escribir SQL manual.

El encadenamiento en Django ORM permite construir consultas complejas de manera legible y modular, sin necesidad de escribir SQL manual.