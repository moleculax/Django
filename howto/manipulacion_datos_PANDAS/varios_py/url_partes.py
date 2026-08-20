from urllib.parse import urlparse, urlunparse, urljoin, urlencode, parse_qs
import pandas as pd

from varios_py.decorador_contarTiempo import contarTiempo



class PartesDeURL():
    @contarTiempo
    def partes(url):
        url_data = urlparse(url)


        # Crear DataFrame
        df = pd.DataFrame([{
            "protocolo": url_data.scheme,
            "dominio": url_data.netloc,
            "ruta": url_data.path,
            "parametros": url_data.params,
            "query": url_data.query,
            "etiqueta": url_data.fragment


        }])
        path = "archivos"
        df.to_csv(f'{path}/datosURL.csv', index=False)  # <-- CORREGIDO: agregar index=False
        print(f"Datos guardados en 'datosURL.csv'")

        return df  # <-- CORREGIDO: retornar el DataFrame


# EJECUTAR
url = "https://www.dynadot.com/es/mercado/subasta"
partes = PartesDeURL.partes(url)
print("\nDatos de la URL:")
print(partes)