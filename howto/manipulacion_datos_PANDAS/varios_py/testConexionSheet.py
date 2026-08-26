import gspread
from google.oauth2.service_account import Credentials

def verificar_google():
    try:
        # Usar el archivo directamente
        creds = Credentials.from_service_account_file(
            '/home/moleculax/ProyectosEnEjecucion/credenciales.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        client = gspread.authorize(creds)
        print("✅ Conexión exitosa")
        return client
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

client = verificar_google()