import pandas as pd
import pygwalker as pyg
from matplotlib import path

# 1. Cargas tus datos en un DataFrame de Pandas
path = "archivos/personas.csv"  # Cambia esto a la ruta de tu archivo CSV
df = pd.read_csv(path)

# 2. Activas la interfaz interactiva de PyGWalker
walker = pyg.walk(df)
