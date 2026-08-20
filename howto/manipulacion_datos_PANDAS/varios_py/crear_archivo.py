import datetime
import pandas as pd
import matplotlib.pyplot as plt
import os  # <-- AGREGADO: para crear carpetas


class CreaArchivoJSON:

    def creaJSON(self):
        # Crear DataFrame
        df = pd.DataFrame({
            'Nombre': ['Ana', 'Luis', 'Carlos'],
            'Edad': [25, 30, 28],
            'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
        })

        print(df)

        # Crear carpeta si no existe
        path = "archivos"
        if not os.path.exists(path):
            os.makedirs(path)
            print(f'📁 Carpeta "{path}" creada')

        # Guardar como CSV
        df.to_csv(f'{path}/personas_pandas.csv', index=False, encoding='utf-8')
        print('✅ Archivo CSV creado')


class copParaExcell():

    def excelCopia(self):
        # Leer CSV y guardar como Excel
        path = "archivos"
        df = pd.read_csv(f'{path}/personas_pandas.csv')

        # Crear carpeta si no existe
        if not os.path.exists(path):
            os.makedirs(path)
            print(f'📁 Carpeta "{path}" creada')

        # Guardar en Excel
        fecha = datetime.datetime.now().strftime('%d-%m-%Y')
        pathExcel = f'{path}/copia_{fecha}.xlsx'

        df.to_excel(pathExcel, index=False)
        print(f'✅ Archivo Excel creado: {pathExcel}')


class creoGrafica():
    def graficodatos(self):
        # Leer CSV
        path = "graficos"

        # Crear carpeta si no existe
        if not os.path.exists(path):
            os.makedirs(path)
            print(f'📁 Carpeta "{path}" creada')

        df = pd.read_csv('archivos/personas_pandas.csv')
        fecha = datetime.datetime.now().strftime('%d-%m-%Y')

        # Crear gráfica de barras y línea de puntos en una sola
        plt.figure(figsize=(10, 6))  # <-- AGREGADO: tamaño de la gráfica
        plt.bar(df['Nombre'], df['Edad'], color='green', alpha=0.7, label='Edad')  # Barras
        plt.plot(df['Nombre'], df['Edad'], marker='o', linestyle='-', color='black', linewidth=2)  # Línea con puntos

        plt.xlabel('Nombre')
        plt.ylabel('Edad')
        plt.title('Edad de las personas')
        plt.grid(True, alpha=0.3)  # <-- AGREGADO: cuadrícula
        plt.tight_layout()  # <-- AGREGADO: ajustar diseño

        # Guardar gráfica
        plt.savefig(f'{path}/{fecha}_grafica_edad.png', dpi=300, bbox_inches='tight')
        plt.show()
        print(f' Gráfica creada: {path}/{fecha}_grafica_edad.png')


# ===== EJECUTAR =====
crear = CreaArchivoJSON()
crear.creaJSON()

creaExcel = copParaExcell()
creaExcel.excelCopia()

grafico = creoGrafica()
grafico.graficodatos()