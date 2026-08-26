import pandas as pd
import matplotlib.pyplot as plt


class LoadCSV():
    def cargoCsv(self):
        path = 'archivos/'
        file = 'indian_stock_market.csv'
        self.df = pd.read_csv(f'{path}{file}')
        return self.df


class ImprimoPantallaCSV():
    def printer(self):
        # Configurar pandas para mostrar todas las filas
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)

        loadcsv = LoadCSV()
        self.df = loadcsv.cargoCsv()
        self.dataFrameTipe = self.df.dtypes
        self.describe = self.df.describe()
        self.cuantos = self.df.count()
        self.conteoNulosPorFilas = self.df.isnull().sum()
        self.shape = self.df.shape

        print("Todas las filas del CSV:")
        print(self.df)  # Muestra todo el DataFrame
        print("Tipos de datos:")
        print(self.dataFrameTipe)
        print("Estadísticas descriptivas:")
        print(self.describe)
        print("Conteo de valores no nulos:")
        print(self.cuantos)
        print("Conteo de valores nulos por filas:")
        print(self.conteoNulosPorFilas)
        print("Forma del DataFrame (Filas/Columnas):")
        print(self.shape)



class TransformoJSOB:
    def EnJSON(self):
        loadcsv = LoadCSV()
        self.df = loadcsv.cargoCsv()
        path = 'archivos/'
        fileJSON = 'indian_stock_market.json'
        fileExcel = 'indian_stock_market.xlsx'
        fileHTML = 'indian_stock_market.html'
        json_data = self.df.to_json(f'{path}{fileJSON}', orient='records', lines=True)
        excel_data = self.df.to_excel(f'{path}{fileExcel}', index=False)
        html_data = self.df.to_html(f'{path}{fileHTML}', index=False)

class NombreColumnas:
    def ColumnasName(self):
        loadcsv = LoadCSV()
        self.df = loadcsv.cargoCsv()
        self.nombresColumnas = self.df.columns
        print("Nombres de las columnas:")
        for c in self.nombresColumnas:
            print(c)


# =========================================
mostrar = ImprimoPantallaCSV()
mostrar.printer()

transformar = TransformoJSOB()
transformar.EnJSON()

columnas = NombreColumnas()
columnas.ColumnasName()