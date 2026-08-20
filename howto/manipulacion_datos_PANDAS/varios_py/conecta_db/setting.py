import psycopg2
# CONEXION POSTGRESQL

def conectapostgre():
    conexion = psycopg2.connect(
        host="localhost",
        port="5432",
        database="anamucpro",
        user="admin",
        password="admin123"
    )