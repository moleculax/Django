import pandas as pd
import matplotlib.pyplot as plt

class AnalisisVentas:
    def __init__(self):
        self.datos = [
            {'mes': 'Enero', 'total': 5000.56},
            {'mes': 'Febrero', 'total': 1000.00},
            {'mes': 'Marzo', 'total': 1350.75},
            {'mes': 'Abril', 'total': 900.50},
            {'mes': 'Mayo', 'total': 1500.25},
            {'mes': 'Junio', 'total': 1100.30},
        ]
        self.df = pd.DataFrame(self.datos)

    def mostrar_primeras_filas(self, ):
        print(f"📊   filas:")
        print(self.df.head())

    def mostrar_estadisticas(self):
        total = self.df['total'].sum()
        minimo = self.df['total'].min()
        maximo = self.df['total'].max()
        promedio = self.df['total'].mean()

        print("\n📊 Estadísticas de ventas:")
        print(f"   Total: ${total:,.2f}")
        print(f"   Mínimo: ${minimo:,.2f}")
        print(f"   Máximo: ${maximo:,.2f}")
        print(f"   Promedio: ${promedio:,.2f}")

        # Mes con más y menos ventas
        mes_max = self.df[self.df['total'] == maximo]['mes'].iloc[0]
        mes_min = self.df[self.df['total'] == minimo]['mes'].iloc[0]
        print(f"   Mes con más ventas: {mes_max} (${maximo:,.2f})")
        print(f"   Mes con menos ventas: {mes_min} (${minimo:,.2f})")

    def mostrar_todos_los_meses(self):
        print("\n📊 Todos los meses:")
        print(self.df['mes'].tolist())

    def grafica_datos(self):
        path = 'graficos/'
        nombreGrafico = 'graficoVentas.png'
        plt.figure(figsize=(10, 6))

        # Graficar cada barra por separado

        colores = []
        leyenda = []
        for valor in self.df['total']:
            if valor == self.df['total'].min():
                colores.append('red')
                leyenda.append('Rojo = Venta mínima')
            elif valor == self.df['total'].max():
                colores.append('green')
                leyenda.append('Verde = Venta máxima')
            else:
                colores.append('blue')
                leyenda.append(None)

        plt.bar(self.df['mes'], self.df['total'], color=colores, label=leyenda)
        # Gráfica LINEAL (cambio de bar a plot)
        plt.plot(self.df['mes'], self.df['total'], color='blue', marker='o', linewidth=2, label='Ventas')
        plt.legend()  # muestra la leyenda
        plt.xlabel('Mes')
        plt.ylabel('Total de Ventas')
        plt.title('Análisis de Ventas Mensuales')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'{path}{nombreGrafico}')
        plt.show()

    def analisis_completo(self):
        print("=" * 50)
        print("ANÁLISIS DE VENTAS MENSUALES")
        print("=" * 50)
        self.mostrar_primeras_filas()
        self.mostrar_todos_los_meses()
        self.mostrar_estadisticas()
        self.grafica_datos()
        print("\n" + "=" * 50)


# ===== EJECUTAR =====
analisis = AnalisisVentas()
analisis.analisis_completo()