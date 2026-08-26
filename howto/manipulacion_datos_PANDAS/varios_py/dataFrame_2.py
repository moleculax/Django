
import pandas as pd

class cargarDatosCSV:
    def cargoCsv(self):
        path = 'archivos/'
        fileCSV = 'flights_small.csv'
        # Configurar pandas para mostrar todas las filas
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        # ==============================================================
        self.df = pd.read_csv(f'{path}{fileCSV}', sep=';')
        return self.df

class printCSV:
    def losdatos(self):
        datos = cargarDatosCSV()
        misDatos = datos.cargoCsv()
        print(misDatos)

class NombreColumnas:
    def columnas(self, df):
        # return self.df.columns
        columnas = df.columns
        for c in columnas:
            print(c)


class NombreAeroLineas:
    def aerolineas(self, df):
        # RENOMBRO COLUMNAS
        df = df.rename(columns={'AIRLINE': 'AEROLINEAS', 'ORIGIN_AIRPORT': 'AEROPUERTO_ORIGEN'})

        # LISTO CON NUEVOS NOMBRES DE COLUMNAS
        nombreDatos = df[['AEROLINEAS', 'AEROPUERTO_ORIGEN', 'DEPARTURE_DELAY']]

        # ORDENAR POR AEROLINEAS (descendente)
        ordenadoDatos = nombreDatos.sort_values('AEROLINEAS', ascending=False)

        # GUARDAR ARCHIVOS
        path = 'archivos/'
        file = 'nuevosDatos.csv'
        filehtml = 'nuevosDatos.html'

        # Guardar CSV ORDENADOS POR AEROLINEAS
        guardoCSV = ordenadoDatos.to_csv(f'{path}{file}', index=False)
        print(f"CSV guardado: {path}{file}")

        # Guardar HTML ORDENADOS POR AEROLINEAS
        guardoHTML = ordenadoDatos.to_html(f'{path}{filehtml}')
        print(f"HTML guardado: {path}{filehtml}")

        # Mostrar datos ordenados
        print("\n📊 Datos ordenados por Aerolíneas (descendente):")
        print(ordenadoDatos)

        return nombreDatos

class ConteoAerolineas:
    def countAeroLineas(self, DataFrame, aerolinea):
        # Filtrar el DataFrame por la aerolínea
        filtro = DataFrame[DataFrame['AIRLINE'] == aerolinea]
        total = len(filtro)
        print(f"📊 Aerolínea: {aerolinea} - Total: {total}")
        return total


class Localizacion:
    def localiza(self, DataFrame, tiempo):
        """Filtra vuelos con retraso de llegada mayor o igual a un tiempo específico"""
        # Filtrar por retraso de llegada
        loc = DataFrame.loc[DataFrame['ARRIVAL_DELAY'] >= tiempo, ['AIRLINE', 'ARRIVAL_DELAY']]

        # Mostrar resultados
        print(f'\n ===========================================================================\n')
        print(f"📊 Vuelos con retraso de llegada >= {tiempo} minutos:")
        # print(loc)
        print(f"\n📊 Total de vuelos encontrados: {len(loc)}")

        # Mostrar estadísticas adicionales
        if len(loc) > 0:
            print(f"📊 Retraso promedio: {loc['ARRIVAL_DELAY'].mean():.2f} minutos")
            print(f"📊 Retraso máximo: {loc['ARRIVAL_DELAY'].max()} minutos")
            print(f"📊 Retraso mínimo: {loc['ARRIVAL_DELAY'].min()} minutos")

        return loc


class CreoNuevaColumna:
    def nuevaCol(self, DataFrame, nuevaColumna='NOMBRE_AEROLINEA'):
        """Crea una columna con el nombre completo de la aerolínea basado en el código"""

        # Mapear códigos a nombres
        mapeo = {
            'AA': 'American Airlines',
            'DL': 'Delta Air Lines',
            'UA': 'United Airlines',
            'WN': 'Southwest Airlines',
            'AS': 'Alaska Airlines',
            'B6': 'JetBlue Airways',
            'NK': 'Spirit Airlines',
            'F9': 'Frontier Airlines',
            'HA': 'Hawaiian Airlines',
            'VX': 'Virgin America'
        }

        # Crear nueva columna aplicando el mapeo
        DataFrame[nuevaColumna] = DataFrame['AIRLINE'].map(mapeo)

        # Crear columna de estado según retraso
        # apply() es un método que aplica una función a cada elemento de la columna
        # Creo nueva columna ESTADO_VUELO
        # DataFrame['ESTADO_VUELO'] = DataFrame['ARRIVAL_DELAY'].apply(
        #     lambda x: '🔴 Retrasado' if x > 30 else
        #     ('🟢 A tiempo' if x >= 0 else '🔵 Anticipado')
        # )
        # Mejo con  bucle tradicional
        estados = []
        for valor in DataFrame['ARRIVAL_DELAY']:
            if valor > 30:
                estados.append('🔴 Retrasado')
            elif valor >= 0:
                estados.append('🟢 A tiempo')
            else:
                estados.append('🔵 Anticipado')

        DataFrame['ESTADO_VUELO'] = estados

        # Guardar
        path = 'archivos/'
        file = 'nuevoDataFrame.csv'
        DataFrame.to_csv(f'{path}{file}', index=False)

        print("=" * 50)
        print("NUEVA COLUMNA CREADA")
        print("=" * 50)
        print(f"Columna: '{nuevaColumna}'")
        print(f"Archivo guardado: {path}{file}")

        # Mostrar muestra
        print("\nMuestra de datos:")
        AEROLINEA_ARRIVO = DataFrame[['AIRLINE','FLIGHT_NUMBER', nuevaColumna, 'ARRIVAL_DELAY']]
        DATOS_ESTADO_VUELO = DataFrame[['AIRLINE','FLIGHT_NUMBER', 'NOMBRE_AEROLINEA', 'ARRIVAL_DELAY', 'ESTADO_VUELO']]
        fileArrive = 'arrivos.csv'
        FILE_EDO_VUELO = 'EDO_VUELO.xlsx'
        FILE_EDO_VUELO_HTML = 'EDO_VUELO.html'
        FILE_EDO_VUELO_JSON = 'EDO_VUELO.json'
        FILE_EDO_VUELO_MARKDOWN = 'EDO_VUELO.md'
        AEROLINEA_ARRIVO.to_csv(f'{path}{fileArrive}', index=False)
        DATOS_ESTADO_VUELO.to_excel(f'{path}{FILE_EDO_VUELO}', index_label=False)
        DATOS_ESTADO_VUELO.to_html(f'{path}{FILE_EDO_VUELO_HTML}', index=False)
        DATOS_ESTADO_VUELO.to_json(f'{path}{FILE_EDO_VUELO_JSON}', index=False)
        DATOS_ESTADO_VUELO.to_markdown(f'{path}{FILE_EDO_VUELO_MARKDOWN}', index=False)
        print(AEROLINEA_ARRIVO)
        # Mostrar estadísticas de la nueva columna
        print(f"\n Distribución de estados de vuelo:")
        print(DataFrame['ESTADO_VUELO'].value_counts())
        print("\n Muestra de datos con nuevas columnas:")
        print(DATOS_ESTADO_VUELO)

        return DataFrame

# =======================================

datosCSV = printCSV()
datosCSV.losdatos()
nombreColumnas = NombreColumnas()
cargarDatosCSV = cargarDatosCSV()
datos = cargarDatosCSV.cargoCsv()
nombreColumnas.columnas(datos)

Lineas = NombreAeroLineas()
Lineas.aerolineas(datos)

conteoAerolinea = ConteoAerolineas()
conteoAerolinea.countAeroLineas(datos,'WN')
conteoAerolinea.countAeroLineas(datos,'AA')

loc = Localizacion()
loc.localiza(datos,60)

nuevaColumna = CreoNuevaColumna()
nuevaColumna.nuevaCol(datos)

