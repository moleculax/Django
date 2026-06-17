# from django.shortcuts import render
# Create your views here.
# IMPORTAMOS LAS VISTAS
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
import json
from urllib.request import urlopen
# IMPORTO LAS CONSTANTE
from djblog.constante.constants import API_POSTS_URL
# AQUI ESTA VINCULADO el archivo json que esta en data/
from djblog.constante.constants import JSON_DATA_PATH

class HelloWorld(View):
    def get(self, request):

        # ============================================================
        # LEER DATOS DESDE ARCHIVO JSON (personas.json)
        # ============================================================
        try:
            # Abrir y leer el archivo JSON
            with open(JSON_DATA_PATH, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            # Si no existe el archivo, mostrar error
            data = []
        except json.JSONDecodeError:
            # Si el JSON está mal formado
            data = []

        # context debe ser un diccionario con clave 'data'
        context = {
            'data': data
        }

        return render(request, 'nosotros.html', context=context)


        # # Array de objetos (lista de diccionarios)
        #
        # data = [
        #     {
        #         'nombre': 'Pepe Lepon',
        #         'edad': 30,
        #         'tecnologias': ['Python', 'Django', 'NextJS', 'React'],
        #         'activo': True
        #     },
        #     {
        #         'nombre': 'Maria Gomez',
        #         'edad': 25,
        #         'tecnologias': ['Java', 'Spring Boot', 'Angular'],
        #         'activo': True
        #     },
        #     {
        #         'nombre': 'Carlos Lopez',
        #         'edad': 35,
        #         'tecnologias': ['JavaScript', 'Vue', 'NodeJS'],
        #         'activo': False
        #     }
        # ]
        #
        # # context debe ser un diccionario con clave 'data'
        # context = {
        #     'data': data
        # }
        #
        # # ✅ CORREGIDO: usar context, no data
        # return render(request, 'nosotros.html', context=context)


# ============================================================
# FUNCIÓN FUERA DE LA CLASE
# MUESTRA RESULTDOS DEL ENDPOINT EN HTML
# ============================================================
def resultados_posts(request):
    """
    Vista que obtiene los posts desde la API y los muestra en una plantilla HTML.

    Args:
        request: Objeto HttpRequest que contiene los datos de la petición HTTP.

    Returns:
        HttpResponse: Renderiza la plantilla 'resultados.html' con los datos de los posts.
    """

    # ============================================================
    # BLOQUE TRY: Intenta ejecutar el código que podría fallar
    # ============================================================
    try:

        # ============================================================
        # 1. LLAMADA A LA API
        # ============================================================
        # urlopen() abre una conexión a la URL especificada
        # API_POSTS_URL es una constante que contiene la URL de la API
        # Ejemplo: 'http://localhost:8000/api/posts/'
        #
        # with ... as response: maneja la conexión automáticamente (la cierra al final)
        # response es el objeto que contiene la respuesta del servidor
        # ============================================================
        with urlopen(API_POSTS_URL) as response:

            # ============================================================
            # 2. LECTURA DE LA RESPUESTA
            # ============================================================
            # response.read() → Lee el contenido de la respuesta en bytes
            # .decode('utf-8') → Convierte los bytes a string (texto)
            # json.loads() → Convierte el string JSON en un objeto Python (lista/diccionario)
            #
            # La API devuelve algo como:
            # [
            #     {"id": 1, "title": "Mi post", "description": "...", "status": true},
            #     {"id": 2, "title": "Otro post", "description": "...", "status": false}
            # ]
            # ============================================================
            data = json.loads(response.read().decode('utf-8'))

        # ============================================================
        # 3. CREACIÓN DEL CONTEXTO
        # ============================================================
        # context es un diccionario que contiene los datos que se pasarán a la plantilla
        # 'resultados' es la clave que usaremos en el template
        # data es la lista de posts que obtuvimos de la API
        # ============================================================
        context = {
            'resultados': data  # En el template se usa {{ resultados }}
        }

        # ============================================================
        # 4. RENDERIZADO DE LA PLANTILLA
        # ============================================================
        # render() combina la plantilla HTML con los datos del context
        # 'resultados.html' es el archivo en posts/templates/resultados.html
        # context son los datos que se inyectan en la plantilla
        # ============================================================
        return render(request, 'resultados.html', context)

    # ============================================================
    # BLOQUE EXCEPT: Captura cualquier error que ocurra en el try
    # ============================================================
    except Exception as e:
        # ============================================================
        # Si algo falla (API no responde, URL incorrecta, etc.)
        # ============================================================

        # ============================================================
        # 1. CREACIÓN DEL CONTEXTO DE ERROR
        # ============================================================
        # 'error' contiene el mensaje de error para mostrarlo en la plantilla
        # 'resultados' es una lista vacía para que el template no falle
        # ============================================================
        context = {
            'error': str(e),  # Convierte la excepción a string: "Connection refused", etc.
            'resultados': []  # Lista vacía para evitar errores en el template
        }

        # ============================================================
        # 2. RENDERIZADO CON ERROR
        # ============================================================
        # Aunque haya error, mostramos la página con el mensaje de error
        # El template debe tener: {% if error %} ... {% endif %}
        # ============================================================
        return render(request, 'resultados.html', context)