import os
import sqlite3


# ========================================================
# 1. DATOS INICIALES (Puedes modificarlos cuando quieras)
# ========================================================
datos_completos = [
    ("Ana López", 1500.50, "Sueldo", "2024-01-15", 1),
    ("Pedro Gómez", 120.00, "Corriente", "2025-06-20", 1),
    ("María Casal", 7500.00, "Ahorro", "2023-11-02", 1),
    ("Carlos Ruiz", 0.00, "Sueldo", "2025-02-10", 0),
    ("Pedro Lepon", 0.00, "Sueldo", "2025-04-10", 0),
]


# ========================================================
# 2. ARRAY DE OBJETOS
# ========================================================
array_de_objetos = []


# ========================================================
# 3. DEFINICIÓN DE LA CLASE
# ========================================================
class CuentaBancaria:

    def __init__(self, id, titular, saldo, tipo_cuenta, fecha_apertura, activa):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        self.tipo = tipo_cuenta
        self.fecha = fecha_apertura
        self.activa = bool(activa)

    def mostrar_ficha_completa(self):
        estado = "🟢 Activa" if self.activa else "🔴 Suspendida"
        return (
            f"ID: {self.id} | Cliente: {self.titular:<8} | "
            f"Tipo: {self.tipo:<10} | Saldo: ${self.saldo:<6} | "
            f"Creada: {self.fecha} | Estado: {estado}"
        )


# ========================================================
# 4. CONEXIÓN A LA BASE DE DATOS
# ========================================================
NOMBRE_DB = "database/banco.db"

conexion = sqlite3.connect(NOMBRE_DB)
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()


# ========================================================
# 5. CREAR TABLA SI NO EXISTE
# ========================================================
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        titular TEXT,
        saldo REAL,
        tipo_cuenta TEXT,
        fecha_apertura TEXT,
        activa INTEGER
    )
""")


# ========================================================
# 6. INSERTAR DATOS (SIEMPRE)
# ========================================================
cursor.executemany(
    """
    INSERT INTO clientes (titular, saldo, tipo_cuenta, fecha_apertura, activa)
    VALUES (?, ?, ?, ?, ?)
""",
    datos_completos,
)
conexion.commit()


# ========================================================
# 7. SELECT: CARGAR DATOS AL ARRAY DE OBJETOS
# ========================================================
cursor.execute("SELECT * FROM clientes")
filas_db = cursor.fetchall()

for fila in filas_db:
    diccionario_datos = dict(fila)
    if 'id_cliente' in diccionario_datos:
        diccionario_datos['id'] = diccionario_datos.pop('id_cliente')
    nuevo_objeto_cliente = CuentaBancaria(**diccionario_datos)
    array_de_objetos.append(nuevo_objeto_cliente)

conexion.close()


# ========================================================
# 8. MOSTRAR LOS DATOS
# ========================================================
for objeto_cuenta in array_de_objetos:
    print(objeto_cuenta.mostrar_ficha_completa())

print(f"\n✅ Total de objetos en el array: {len(array_de_objetos)}")