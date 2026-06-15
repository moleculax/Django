# from django.shortcuts import render
# Create your views here.
# IMPORTAMOS LAS VISTAS
from importlib.resources import contents
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base  import View

class HelloWorld(View):
    def get(self, request):

        data = {
            'name': 'Pepe lepon',
            'years': 30,
            'codes': ['Python','Django','NextJS', 'React']
        }


        # return HttpResponse(contents("Hello World primer django"))
        return render(request, 'hello_world.html', context=data)
