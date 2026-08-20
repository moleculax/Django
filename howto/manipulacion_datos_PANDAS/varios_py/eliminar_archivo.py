import os
import shutil
from datetime import datetime

from varios_py.crear_archivo import CreaArchivoJSON


class CopiaEliminaArchivo:
    def copia_eliminar_archivo(self, path):  # ¡Falta el 'self'!
        try:
            # COPIO EL ARCHIVO CON FECHA DIA-MES-AÑO
            fecha = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            backup_path = f'copia_{fecha}_{path}'

            shutil.copy2(path, backup_path)
            print(f"Copia creada: '{backup_path}'")

            # ELIMINO EL ARCHIVO ORIGINAL
            os.remove(path)
            print(f"Archivo '{path}' eliminado exitosamente.")

        except FileNotFoundError:
            print(f"Archivo '{path}' no encontrado.")
        except Exception as e:
            print(f"Error: {e}")


# HAGO LLAMADO A CLASS QUE CREA ARCHIVO
creoFile = CreaArchivoJSON()
creoFile.creaJSON()
# EJECUTAR LA CLASS
ejecutoClass = CopiaEliminaArchivo()
ejecutoClass.copia_eliminar_archivo('personas_pandas.csv')