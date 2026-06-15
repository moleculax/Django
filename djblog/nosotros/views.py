# from django.shortcuts import render
# Create your views here.
# IMPORTAMOS LAS VISTAS
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class nosotros(View):
    def get(self, request):
        # Array de objetos (lista de diccionarios)
        data = [
            {
                'nombre': 'Pepe Lepon',
                'edad': 30,
                'descripcion': 'Desarrollador backend con experiencia en Python y Django.',
                'tecnologias': ['Python', 'Django', 'NextJS', 'React'],
                'activo': True
            },
            {
                'nombre': 'Lupe Lepon',
                'edad': 25,
                'descripcion': 'Desarrolladora frontend especializada en React y Angular.',
                'tecnologias': ['Java', 'Spring Boot', 'Angular'],
                'activo': True
            },
            {
                'nombre': 'Roki Lepon',
                'edad': 35,
                'descripcion':  'Desarrolladora frontend especializada en Vue y NodeJS.',
                'tecnologias': ['JavaScript', 'Vue', 'NodeJS'],
                'activo': False
            }
        ]

        # context debe ser un diccionario con clave 'data'
        context = {
            'data': data
        }

        #  usar context, no data
        return render(request, 'nosotros.html', context=context)