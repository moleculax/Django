import os
import psycopg2
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import numpy as np
"""
        # Conexión a PostgreSQL
        pip install psycopg2-binary
        
        # Manipulación de datos
        pip install pandas
        
        # Gráficos
        pip install matplotlib
        
        # Interfaz gráfica (tkinter viene con Python por defecto)
        # tkinter ya viene instalado con Python, no necesitas instalarlo
"""

class Conexion():
    def conecta(self):
        conexion = psycopg2.connect(
            host="localhost",
            port="5432",
            database="anamucpro",
            user="admin",
            password="admin123"
        )
        return conexion


class AppVentas:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 Análisis de Ventas")
        self.root.geometry("1200x700")
        self.root.configure(bg='#f0f0f0')

        self.df = None
        self.ventas_por_menu = None

        # ===== CONFIGURAR TEMA =====
        style = ttk.Style()

        # Listar temas disponibles (opcional)
        temas_disponibles = style.theme_names()
        print(f"📋 Temas disponibles: {temas_disponibles}")

        # Usar un tema que existe en todos los sistemas
        if 'clam' in temas_disponibles:
            style.theme_use('clam')
        elif 'alt' in temas_disponibles:
            style.theme_use('alt')
        elif 'default' in temas_disponibles:
            style.theme_use('default')
        else:
            style.theme_use(temas_disponibles[0])  # Usar el primero disponible

        self.crear_widgets()
        self.cargar_datos()

    def crear_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 10))

        titulo = ttk.Label(top_frame, text="📊 ANÁLISIS DE VENTAS",
                           font=('Arial', 16, 'bold'))
        titulo.pack(side=tk.LEFT, padx=10)

        btn_frame = ttk.Frame(top_frame)
        btn_frame.pack(side=tk.RIGHT)

        ttk.Button(btn_frame, text="🔄 Actualizar",
                   command=self.cargar_datos).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="📁 Exportar CSV",
                   command=self.exportar_csv).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="📊 Ver Gráficos",
                   command=self.mostrar_graficos).pack(side=tk.LEFT, padx=5)

        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)

        self.crear_tabla(content_frame)
        self.crear_estadisticas(content_frame)

    def crear_tabla(self, parent):
        table_frame = ttk.LabelFrame(parent, text="📋 Datos de Ventas", padding="5")
        table_frame.pack(fill=tk.BOTH, expand=True)

        scroll_y = ttk.Scrollbar(table_frame)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree = ttk.Treeview(table_frame,
                                 yscrollcommand=scroll_y.set,
                                 xscrollcommand=scroll_x.set)
        self.tree.pack(fill=tk.BOTH, expand=True)

        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview)

    def crear_estadisticas(self, parent):
        stats_frame = ttk.LabelFrame(parent, text="📊 Estadísticas", padding="10")
        stats_frame.pack(fill=tk.X, pady=(10, 0))

        self.stats_text = tk.Text(stats_frame, height=4, bg='#f8f9fa',
                                  font=('Arial', 10), wrap=tk.WORD)
        self.stats_text.pack(fill=tk.X)

    def cargar_datos(self):
        try:
            self.stats_text.insert(tk.END, "🔄 Cargando datos...\n")
            self.root.update()
            threading.Thread(target=self._cargar_datos_thread, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar datos: {e}")

    def _cargar_datos_thread(self):
        try:
            traigo = TraigoDatos()
            self.df = traigo.Datos()
            self.ventas_por_menu = self.df.groupby('nombre_menu')['total'].sum().sort_values(ascending=False)
            self.root.after(0, self._actualizar_ui)
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Error: {e}"))

    def _actualizar_ui(self):
        if self.df is None or self.df.empty:
            self.stats_text.insert(tk.END, "❌ No se encontraron datos\n")
            return

        for item in self.tree.get_children():
            self.tree.delete(item)

        columnas = list(self.df.columns)
        self.tree['columns'] = columnas
        self.tree['show'] = 'headings'

        for col in columnas:
            self.tree.heading(col, text=col.replace('_', ' ').title())
            self.tree.column(col, width=120, anchor='center')

        for _, row in self.df.iterrows():
            self.tree.insert('', 'end', values=list(row))

        self.stats_text.delete(1.0, tk.END)
        stats = f"""
📊 Resumen de Ventas:
• Total registros: {len(self.df)}
• Total ventas: ${self.df['total'].sum():,.2f}
• Promedio por venta: ${self.df['total'].mean():,.2f}
• Menú más vendido: {self.ventas_por_menu.index[0]} (${self.ventas_por_menu.iloc[0]:,.2f})
• Total de menús: {len(self.ventas_por_menu)}
        """
        self.stats_text.insert(tk.END, stats)

    def exportar_csv(self):
        if self.df is None:
            messagebox.showwarning("Advertencia", "No hay datos para exportar")
            return

        archivo = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )

        if archivo:
            try:
                self.df.to_csv(archivo, index=False, encoding='utf-8-sig')
                messagebox.showinfo("Éxito", f"Datos exportados a:\n{archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al exportar: {e}")

    def mostrar_graficos(self):
        if self.ventas_por_menu is None:
            messagebox.showwarning("Advertencia", "Primero carga los datos")
            return

        ventana_graficos = tk.Toplevel(self.root)
        ventana_graficos.title("📊 Gráficos de Ventas")
        ventana_graficos.geometry("1100x800")

        notebook = ttk.Notebook(ventana_graficos)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self._crear_grafico_barras(notebook)
        self._crear_grafico_pastel(notebook)
        self._crear_grafico_horizontal(notebook)
        self._crear_grafico_lineas(notebook)

    def _crear_grafico_barras(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="📊 Barras")

        fig, ax = plt.subplots(figsize=(10, 6))

        indices = self.ventas_por_menu.index.tolist()
        valores = self.ventas_por_menu.values

        barras = ax.bar(indices, valores,
                        color='steelblue', alpha=0.8, edgecolor='black')

        for barra in barras:
            altura = barra.get_height()
            ax.text(barra.get_x() + barra.get_width() / 2., altura,
                    f'${altura:,.0f}', ha='center', va='bottom', fontsize=9)

        ax.set_xlabel('Nombre del Menú', fontsize=12)
        ax.set_ylabel('Total de Ventas ($)', fontsize=12)
        ax.set_title('Total de Ventas por Menú', fontsize=14)
        ax.set_xticks(range(len(indices)))
        ax.set_xticklabels(indices, rotation=45, ha='right')
        ax.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def _crear_grafico_pastel(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="🥧 Pastel")

        try:
            ventas_series = self.ventas_por_menu
            valores = pd.to_numeric(ventas_series.values, errors='coerce')
            etiquetas = ventas_series.index.tolist()

            mascara = (valores > 0) & (~pd.isna(valores))
            valores_validos = valores[mascara]
            etiquetas_validas = [etiquetas[i] for i in range(len(etiquetas)) if mascara[i]]

            if len(valores_validos) == 0 or valores_validos.sum() == 0:
                label = ttk.Label(frame, text="❌ No hay datos válidos para el gráfico de pastel",
                                  font=('Arial', 14))
                label.pack(expand=True)
                return

            fig, ax = plt.subplots(figsize=(10, 10))

            wedges, texts, autotexts = ax.pie(
                valores_validos,
                labels=etiquetas_validas,
                autopct='%1.1f%%',
                startangle=90,
                colors=plt.cm.Set3(range(len(valores_validos))),
                textprops={'fontsize': 10}
            )

            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontweight('bold')
                autotext.set_fontsize(11)

            for text in texts:
                text.set_fontsize(10)
                text.set_fontweight('normal')

            ax.set_title('Distribución de Ventas por Menú', fontsize=14, fontweight='bold')
            ax.legend(wedges, etiquetas_validas,
                      title="Menús",
                      loc="center left",
                      bbox_to_anchor=(1, 0, 0.5, 1),
                      fontsize=10)

            plt.tight_layout()

            canvas = FigureCanvasTkAgg(fig, frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        except Exception as e:
            label = ttk.Label(frame, text=f"❌ Error al crear gráfico: {str(e)}",
                              font=('Arial', 12), foreground='red')
            label.pack(expand=True)
            print(f"Error en gráfico de pastel: {e}")

    def _crear_grafico_horizontal(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="📊 Horizontal")

        fig, ax = plt.subplots(figsize=(10, 8))

        datos_ordenados = self.ventas_por_menu.sort_values(ascending=True)
        indices = datos_ordenados.index.tolist()
        valores = datos_ordenados.values

        barras = ax.barh(indices, valores,
                         color='coral', edgecolor='black')

        for barra in barras:
            ancho = barra.get_width()
            ax.text(ancho, barra.get_y() + barra.get_height() / 2.,
                    f'${ancho:,.0f}', ha='left', va='center', fontsize=9)

        ax.set_xlabel('Total de Ventas ($)', fontsize=12)
        ax.set_ylabel('Nombre del Menú', fontsize=12)
        ax.set_title('Ventas por Menú (Horizontal)', fontsize=14)
        ax.grid(True, alpha=0.3, axis='x')
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def _crear_grafico_lineas(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="📈 Líneas")

        fig, ax = plt.subplots(figsize=(10, 6))

        indices = self.ventas_por_menu.index.tolist()
        valores = self.ventas_por_menu.values

        ax.plot(indices, valores,
                'o-', linewidth=2, markersize=10, color='green')
        ax.fill_between(range(len(indices)),
                        valores,
                        alpha=0.2, color='green')

        ax.set_xlabel('Nombre del Menú', fontsize=12)
        ax.set_ylabel('Total de Ventas ($)', fontsize=12)
        ax.set_title('Tendencia de Ventas por Menú', fontsize=14)
        ax.set_xticks(range(len(indices)))
        ax.set_xticklabels(indices, rotation=45, ha='right')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


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

        cursor = conn.cursor()
        cursor.execute(sql)
        response = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(response, columns=columnas)

        cursor.close()
        conn.close()

        return df


# ===== EJECUTAR =====
if __name__ == "__main__":
    root = tk.Tk()
    app = AppVentas(root)
    root.mainloop()