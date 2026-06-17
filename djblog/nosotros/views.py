# from django.shortcuts import render
# Create your views here.
# IMPORTAMOS LAS VISTAS
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
import json  # AGREGAR ESTA IMPORTACIÓN
# AQUI ESTA VINCULADO el archivo json que esta en data/
from djblog.constante.constants import JSON_DATA_PATH

class nosotros(View):
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