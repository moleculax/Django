import json
import pandas as pd
import os
from sqlalchemy import create_engine
class Person:
    def __init__(self, name="", age=0, mail=""):
        self.name = name
        self.age = age
        self.mail = mail

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "mail": self.mail
        }


# Crear personas
p1 = Person("Tobias", 25, "elmail")
p2 = Person("Tobias2", 20, "elmail2")
p3 = Person("Tobias3", 20, "elmail3")

df = pd.DataFrame(
    [p.to_dict()
     for p in [p1, p2, p3]]
)


#  Guardar a CSV
path = "archivos/"
nombreFile = "personas.csv"
#  Crear la carpeta si no existe
os.makedirs(path, exist_ok=True)
filecsv = df.to_csv(f'{path}{nombreFile}', index=False)
# leo el archivo csv para hacer print
leoFile = pd.read_csv(f'{path}{nombreFile}')
# print(leoFile)
# paso data frame a json
filejson = df.to_json(f'{path}personas.json', orient='records')
leojson = pd.read_json(f'{path}personas.json')
# print(leojson)
formatojson = json.dumps(leojson.to_dict('records'), indent=2)
print(formatojson)
# paso a html
formatohtml = df.to_html(f'{path}personas.html', index=False)
# =====================================================================
# paso a sql
engine = create_engine(f'sqlite:///{path}personas.db')

# Opción 2: PostgreSQL (necesita psycopg2)
# engine = create_engine('postgresql://usuario:contraseña@localhost:5432/nombre_db')

# Opción 3: MySQL (necesita pymysql)
# engine = create_engine('mysql+pymysql://usuario:contraseña@localhost:3306/nombre_db')

# Guardar DataFrame en SQL
formatosql = df.to_sql('personas', con=engine, if_exists='replace', index=False)
print(f"\n Datos guardados en SQLite: {path}personas.db")
print(f"   Filas insertadas: {formatosql}")

# Verificar que se guardó correctamente
print("\n📄 Leyendo desde SQL:")
df_leido_sql = pd.read_sql('SELECT * FROM personas', con=engine)
print(df_leido_sql)

# ================================================================================


# paso a excel
fileexcel = df.to_excel(f'{path}personas.xlsx', index=False)


# Lista de personas a JSON
# personas = [p1, p2, p3]
#
# lista_dict = []
# for p in personas:
#     lista_dict.append(p.to_dict())
# json_data = json.dumps(lista_dict, indent=2)
# print(json_data)