# djblog/constants.py

from pathlib import Path

# ============================================================
# URLs DE LA API
# ============================================================
URL = 'http://localhost:8000'
API_BASE_URL = f'{URL}/api/'

API_POSTS_URL = f'{URL}/api/posts/'
API_POSTS_URL_RESULTADOS = f'{API_BASE_URL}posts/resultados'

# ============================================================
# PAGINACIÓN
# ============================================================
PAGE_SIZE = 10

# ============================================================
# ESTADOS
# ============================================================
STATUS_ACTIVE = True
STATUS_INACTIVE = False

# ============================================================
# RUTA AL ARCHIVO JSON (personas.json)
# ============================================================
# Path(__file__) → Ruta del archivo actual (constants.py)
# .resolve() → Convierte a ruta absoluta
# .parent → Sube un nivel (a la carpeta djblog)
# / 'data' / 'personas.json' → Construye la ruta: djblog/data/personas.json
# ============================================================
JSON_DATA_PATH = Path(__file__).resolve().parent.parent / 'data' / 'personas.json'