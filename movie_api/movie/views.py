from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from movie.models import Movie
from django.http import JsonResponse

class VistaMovie(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'message': 'La solicitud fue permitida',
        }
        return Response(content)


class MovieList(APIView):
    permission_classes = [IsAuthenticated]  #  AGREGADO PERMISOS
# TRAIGO TODAS LAS PELICULAS
    def get(self, request, format=None):
        movies = Movie.objects.all()
        data = []
        for elemento in movies:
            data.append({
                "id": elemento.id,
                "title": elemento.title,
                "duration": elemento.duration,
                "sinopsis": elemento.sinopsis,
            })  # ← Un solo diccionario con todos los campos
        return JsonResponse(data, safe=False)

# TRAIGO LAS PELICULAS POR ID

class MovieBYID(APIView):
    permission_classes = [IsAuthenticated]  # AGREGO PERMISOS

    def get(self, request, pk, format=None):  # MÉTODO get con pk
        try:
            movie = Movie.objects.get(pk=pk)
            data = {
                "id": movie.id,
                "title": movie.title,
                "duration": movie.duration,
                "sinopsis": movie.sinopsis,
            }
            return JsonResponse(data, safe=False)
        except Movie.DoesNotExist:
            return Response(
                {"error": "Película no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )



