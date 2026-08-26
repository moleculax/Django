import os
import psycopg2
import pandas as pd
from datetime import datetime

from matplotlib import pyplot as plt


class Conexion():

    def conecta(self):
        # Configuración de conexión
        conexion = psycopg2.connect(
            host="localhost",
            port="5432",
            database="anamucpro",
            user="admin",
            password="admin123"
        )
        return conexion


class TraigoDatos():

    def Datos(self):
        conexion = Conexion()
        conn = conexion.conecta()

        MES = 3
        ANIO = 2026

        sql = f"""
          SELECT DISTINCT ON (v.id_venta)
    ct.nombre_categoria AS nombre_categoria,
    ct.descripcion_categoria AS descripcion_categoria,
    m.nombre AS nombre_menu,
    v.folio,
    TO_CHAR(v.fecha_hora::timestamp, 'DD-MM-YYYY') AS fecha,
    CASE CAST(EXTRACT(DOW FROM v.fecha_hora::timestamp) AS INT)
        WHEN 0 THEN 'Domingo'
        WHEN 1 THEN 'Lunes'
        WHEN 2 THEN 'Martes'
        WHEN 3 THEN 'Miércoles'
        WHEN 4 THEN 'Jueves'
        WHEN 5 THEN 'Viernes'
        WHEN 6 THEN 'Sábado'
        ELSE 'Desconocido'
        END AS nombre_dia,
    EXTRACT(MONTH FROM v.fecha_hora::timestamp)::INT AS mes,
    EXTRACT(YEAR FROM v.fecha_hora::timestamp)::INT AS anio,
    v.subtotal,
    v.impuestos,
    v.total,
    (SELECT nombre FROM users WHERE id_user = v.usuario_id) AS nombre_usuario
FROM ventas v
         INNER JOIN det_pedidos d ON d.pedidos_id = v.pedido_id
         INNER JOIN categorias ct ON ct.restaurante_id = v.restaurant_id AND ct.id_categoria = v.producto_id
         INNER JOIN menu m ON m.restaurante_id = v.restaurant_id AND m.categoria_id = v.producto_id AND m.id_menu = v.id_menu
WHERE v.comercio_id = 1
  AND v.restaurant_id = 1
  AND EXTRACT(MONTH FROM v.fecha_hora::timestamp) = {MES}
  AND EXTRACT(YEAR FROM v.fecha_hora::timestamp) = {ANIO}
  AND v.estado_ventas = 1
ORDER BY v.id_venta ASC;
        """

        # Crear cursor
        cursor = conn.cursor()
        cursor.execute(sql)
        response = cursor.fetchall()

        # Obtener nombres de columnas
        columnas = [desc[0] for desc in cursor.description]

        # Crear DataFrame
        df = pd.DataFrame(response, columns=columnas)

        print(f"Datos obtenidos: {len(df)} registros")

        cursor.close()
        conn.close()

        # Guardar como CSV
        path = "archivo_csv"

        # Crear la carpeta si no existe
        if not os.path.exists(path):
            os.makedirs(path)
            print(f'Carpeta "{path}" creada')

        fecha = datetime.now().strftime('%Y%m%d')
        nombre_archivo = f'{path}/ventas_{fecha}.csv'
        df.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')
        df.to_excel(f'{path}/ventas_{fecha}.xlsx', index=False)
        print(f'CSV creado: {nombre_archivo}')
        print(f'Excel creado: {nombre_archivo}')
        # INICIO GRAFICA DE DATOS
        graficos = GraficoDatos()
        graficos.grafica(nombre_archivo)
        # ====================================
        return df




class GraficoDatos():
    def grafica(self, datos):
        # Leer CSV
        path = "graficos"

        if not os.path.exists(path):
            os.makedirs(path)
            print(f'Carpeta "{path}" creada')

        df = pd.read_csv(datos)
        fecha = datetime.now().strftime('%d-%m-%Y')

        # ===== 1. GRÁFICO DE BARRAS (Agrupado) =====
        ventas_por_menu = df.groupby('nombre_menu')['total'].sum().sort_values(ascending=False)

        plt.figure(figsize=(12, 6))
        barras = plt.bar(ventas_por_menu.index, ventas_por_menu.values,
                         color='steelblue', alpha=0.8, edgecolor='black')

        # Agregar valores
        for barra in barras:
            altura = barra.get_height()
            plt.text(barra.get_x() + barra.get_width() / 2., altura,
                     f'${altura:,.0f}',
                     ha='center', va='bottom', fontsize=9)

        plt.xlabel('Nombre del Menú', fontsize=12)
        plt.ylabel('Total de Ventas ($)', fontsize=12)
        plt.title(f'Total de Ventas por Menú - {fecha}', fontsize=14)
        plt.xticks(rotation=45, ha='right')
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig(f'{path}/{fecha}_barras_ventas.png', dpi=300, bbox_inches='tight')
        plt.show()
        plt.close()
        print(f' Gráfico de barras: {path}/{fecha}_barras_ventas.png')

        # ===== 2. GRÁFICO DE PASTEL =====
        plt.figure(figsize=(10, 10))
        plt.pie(ventas_por_menu.values,
                labels=ventas_por_menu.index,
                autopct='%1.1f%%',
                startangle=90,
                colors=plt.cm.Set3(range(len(ventas_por_menu))))
        plt.title(f'Distribución de Ventas por Menú - {fecha}', fontsize=14)
        plt.tight_layout()
        plt.savefig(f'{path}/{fecha}_pastel_ventas.png', dpi=300, bbox_inches='tight')
        plt.show()
        plt.close()
        print(f'Gráfico de pastel: {path}/{fecha}_pastel_ventas.png')

        # ===== 3. GRÁFICO DE BARRAS HORIZONTALES =====
        plt.figure(figsize=(10, 8))
        ventas_por_menu.sort_values(ascending=True).plot(kind='barh',
                                                         color='coral',
                                                         edgecolor='black')
        plt.xlabel('Total de Ventas ($)', fontsize=12)
        plt.ylabel('Nombre del Menú', fontsize=12)
        plt.title(f'Ventas por Menú (Horizontal) - {fecha}', fontsize=14)
        plt.grid(True, alpha=0.3, axis='x')
        plt.tight_layout()
        plt.savefig(f'{path}/{fecha}_barras_horizontal.png', dpi=300, bbox_inches='tight')
        plt.close()
        print(f'Gráfico horizontal: {path}/{fecha}_barras_horizontal.png')

        # ===== 4. GRÁFICO CON LÍNEAS (Tendencia) =====
        plt.figure(figsize=(12, 6))
        plt.plot(ventas_por_menu.index, ventas_por_menu.values,
                 'o-', linewidth=2, markersize=10, color='green')
        plt.fill_between(range(len(ventas_por_menu)),
                         ventas_por_menu.values,
                         alpha=0.2, color='green')
        plt.xlabel('Nombre del Menú', fontsize=12)
        plt.ylabel('Total de Ventas ($)', fontsize=12)
        plt.title(f'Tendencia de Ventas por Menú - {fecha}', fontsize=14)
        plt.xticks(range(len(ventas_por_menu)), ventas_por_menu.index, rotation=45, ha='right')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{path}/{fecha}_linea_tendencia.png', dpi=300, bbox_inches='tight')
        plt.close()
        print(f' Gráfico de líneas: {path}/{fecha}_linea_tendencia.png')

        print(f"\nResumen de ventas por menú:")
        print(ventas_por_menu)
        print(f"\nTotal general: ${ventas_por_menu.sum():,.2f}")


# EJECUTAR
resultados = TraigoDatos()
Datos = resultados.Datos()

print("\nDatos obtenidos:")
print(Datos.to_string(index=False)) # PARA QUE MUESTRE TODOS LOS DATOS

# Mostrar información adicional
print(f"\nTotal de registros: {len(Datos)}")
print(f"Columnas: {len(Datos.columns)}")
# print("\nNombres de columnas:")
# for col in Datos.columns:
#     print(f"  - {col}")