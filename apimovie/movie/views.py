from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from movie.models import Movie
from django.http import JsonResponse

from . import serializers
# COLOCO UN (.) DELANTE PORQUE ESTOY EN LA MISMA CARPETA
from .serializers import MovieSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse


class VistaMovie(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        content = {
            'estado': True,
            'message': 'La solicitud fue permitida',
        }
        return Response(content)


class MovieList(APIView):
    permission_classes = [AllowAny]  #  CUALQUIERA PUEDE VER ESTE RESULTADO SIN AUTENTICARSE
# TRAIGO TODAS LAS PELICULAS
    def get(self, request):
        movie = Movie.objects.all()
        # data = []
        # for elemento in movies:
        #     data.append({
        #         "id": elemento.id,
        #         "title": elemento.title,
        #         "duration": elemento.duration,
        #         "sinopsis": elemento.sinopsis,
        #     })  # ← Un solo diccionario con todos los campos
        # return JsonResponse(data, safe=False)
        # COMENTE LO DE ARRIBA PORQUE USARE SERIALIZER
        data_serializado = MovieSerializer(movie, many=True)
        if movie.exists():

            return Response(
                {
                    "estado": True,
                    "mensaje": "Datos encontrados",
                    "data": data_serializado.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return  Response(
                {
                    "estado": False,
                    "mensaje": "No existen datos",
                    "data": data_serializado.data
                }
            )

# TRAIGO LAS PELICULAS POR ID

class MovieBYID(APIView):
    permission_classes = [AllowAny]  #   CUALQUIERA PUEDE VER ESTE RESULTADO SIN AUTENTICARSE

    def get(self, request, pk, format=None):  # MÉTODO get con pk
        try:
            movie = Movie.objects.get(pk=pk)
            # data = {
            #     "id": movie.id,
            #     "title": movie.title,
            #     "duration": movie.duration,
            #     "sinopsis": movie.sinopsis,
            # }
            # return JsonResponse(data, safe=False)

            data_serializado = MovieSerializer(movie)
            return Response(
                {
                    "estado": True,
                    "mensaje": "Datos encontrados",
                    "data": data_serializado.data
                },
                status=status.HTTP_200_OK
            )

        except Movie.DoesNotExist:
            # return JsonResponse(
            #     {"error": "Película no encontrada"},
            #     status=status.HTTP_404_NOT_FOUND
            # )
            return Response(
                {
                    "estado": False,
                    "mensaje": "Película no encontrada",
                    "data": None
                },
                status=status.HTTP_404_NOT_FOUND
            )

class MovieCreate(APIView):
    permission_classes = [IsAuthenticated] # TIENE QUE ESTAR AUTENTICADO

    @extend_schema(
        request=MovieSerializer,  # MUESTRA LOS CAMPOS EN SWAGGER
        responses={
            200: OpenApiResponse(description='Actualizada correctamente'),
            400: OpenApiResponse(description='Datos inválidos'),
            404: OpenApiResponse(description='No encontrada'),
        }
    )

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieUpdate(APIView):
    permission_classes = [IsAuthenticated]  # TIENE QUE ESTAR AUTENTICADO

    @extend_schema(
        request=MovieSerializer,  #  MUESTRA LOS CAMPOS EN SWAGGER
        responses={
            200: OpenApiResponse(description='Actualizada correctamente'),
            400: OpenApiResponse(description='Datos inválidos'),
            404: OpenApiResponse(description='No encontrada'),
        }
    )
    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                {"error": "Película no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDelete(APIView):
    permission_classes = [IsAuthenticated] # TIENE QUE ESTAR AUTENTICADO
    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response(
                {"message": "Película eliminada correctamente"},
                status=status.HTTP_204_NO_CONTENT
            )
        except Movie.DoesNotExist:
            return Response(
                {"error": "Película no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )




