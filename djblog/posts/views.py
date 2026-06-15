# from django.shortcuts import render
# Create your views here.
# IMPORTAMOS LAS VISTAS
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class HelloWorld(View):
    def get(self, request):
        # Array de objetos (lista de diccionarios)
        data = [
            {
                'nombre': 'Pepe Lepon',
                'edad': 30,
                'tecnologias': ['Python', 'Django', 'NextJS', 'React'],
                'activo': True
            },
            {
                'nombre': 'Maria Gomez',
                'edad': 25,
                'tecnologias': ['Java', 'Spring Boot', 'Angular'],
                'activo': True
            },
            {
                'nombre': 'Carlos Lopez',
                'edad': 35,
                'tecnologias': ['JavaScript', 'Vue', 'NodeJS'],
                'activo': False
            }
        ]

        # context debe ser un diccionario con clave 'data'
        context = {
            'data': data
        }

        # ✅ CORREGIDO: usar context, no data
        return render(request, 'hello_world.html', context=context)