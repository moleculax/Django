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
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter


class VistaMovie(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Verificar estado de la API",
        description="Endpoint de prueba para verificar que la API está funcionando correctamente. No requiere autenticación.",
        responses={
            200: OpenApiResponse(description="API funcionando correctamente"),
        }
    )
    def get(self, request, format=None):
        content = {
            'estado': True,
            'message': 'La solicitud fue permitida',
        }
        return Response(content)


class MovieList(APIView):
    permission_classes = [AllowAny]  # CUALQUIERA PUEDE VER ESTE RESULTADO SIN AUTENTICARSE

    @extend_schema(
        summary="Listar todas las películas",
        description="Obtiene la lista completa de todas las películas disponibles en la base de datos. No requiere autenticación.",
        responses={
            200: OpenApiResponse(description="Lista de películas obtenida exitosamente"),
            400: OpenApiResponse(description="Error en la solicitud"),
        }
    )
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
            return Response(
                {
                    "estado": False,
                    "mensaje": "No existen datos",
                    "data": data_serializado.data
                }
            )


# TRAIGO LAS PELICULAS POR ID
# TRAIGO LAS PELICULAS POR ID
class MovieBYID(APIView):
    permission_classes = [AllowAny]  # CUALQUIERA PUEDE VER SIN AUTENTICACIÓN

    @extend_schema(
        summary="Obtener película por ID",
        description="Obtiene los detalles de una película específica usando su ID. No requiere autenticación.",
        # ELIMINAR OpenApiParameter DE pk PORQUE YA ESTÁ EN LA URL
        responses={
            200: OpenApiResponse(description="Película encontrada"),
            404: OpenApiResponse(description="Película no encontrada"),
        }
    )
    def get(self, request, pk, format=None):
        try:
            # FILTRAR POR PK (SIN FILTRO DE USUARIO)
            movie = Movie.objects.get(pk=pk)
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
            return Response(
                {
                    "estado": False,
                    "mensaje": "Película no encontrada",
                    "data": None
                },
                status=status.HTTP_404_NOT_FOUND
            )

class MovieBYIDUSUARIO(APIView):
    permission_classes = [AllowAny]  # CUALQUIERA PUEDE VER SIN AUTENTICACIÓN

    @extend_schema(
        summary="Obtener películas por usuario",
        description="Obtiene todas las películas de un usuario específico usando su ID. No requiere autenticación.",
        parameters=[
            OpenApiParameter(
                name="user_id",
                type=int,
                location=OpenApiParameter.PATH,
                description="ID del usuario para filtrar sus películas",
                required=True
            )
        ],
        responses={
            200: OpenApiResponse(description="Películas del usuario obtenidas exitosamente"),
            400: OpenApiResponse(description="Error en la solicitud"),
        }
    )
    def get(self, request, user_id, format=None):
        try:
            # FILTRAR PELÍCULAS POR ID DE USUARIO
            movies = Movie.objects.filter(user_id=user_id)

            # VERIFICAR SI EL USUARIO TIENE PELÍCULAS
            if not movies.exists():
                return Response(
                    {
                        "estado": False,
                        "mensaje": "El usuario no tiene películas",
                        "data": []
                    },
                    status=status.HTTP_200_OK
                )

            # SERIALIZAR CON many=True PORQUE SON VARIAS
            data_serializado = MovieSerializer(movies, many=True)

            return Response(
                {
                    "estado": True,
                    "mensaje": "Datos encontrados",
                    "data": data_serializado.data
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {
                    "estado": False,
                    "mensaje": "Error al obtener las películas",
                    "data": None
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class MovieCreate(APIView):
    permission_classes = [IsAuthenticated]  # TIENE QUE ESTAR AUTENTICADO

    @extend_schema(
        summary="Crear nueva película",
        description="Crea una nueva película. Requiere autenticación JWT. El usuario autenticado será asignado automáticamente como propietario.",
        request=MovieSerializer,
        responses={
            201: OpenApiResponse(description="Película creada exitosamente"),
            400: OpenApiResponse(description="Datos inválidos"),
            401: OpenApiResponse(description="No autenticado"),
        }
    )
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # ← ASIGNAR USUARIO AUTOMÁTICAMENTE
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieUpdate(APIView):
    permission_classes = [IsAuthenticated]  # TIENE QUE ESTAR AUTENTICADO

    @extend_schema(
        summary="Actualizar película",
        description="Actualiza los datos de una película existente. Requiere autenticación JWT. El usuario solo puede actualizar sus propias películas.",
        request=MovieSerializer,
        parameters=[
            OpenApiParameter(
                name="pk",
                type=int,
                location=OpenApiParameter.PATH,
                description="ID de la película a actualizar",
                required=True
            )
        ],
        responses={
            200: OpenApiResponse(description="Película actualizada correctamente"),
            400: OpenApiResponse(description="Datos inválidos"),
            403: OpenApiResponse(description="No tienes permiso"),
            404: OpenApiResponse(description="Película no encontrada"),
            401: OpenApiResponse(description="No autenticado"),
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

        # QUE LA PELÍCULA PERTENECE AL USUARIO
        if movie.user != request.user:
            return Response(
                {"error": "No tienes permiso para editar esta película"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDelete(APIView):
    permission_classes = [IsAuthenticated]  # TIENE QUE ESTAR AUTENTICADO

    @extend_schema(
        summary="Eliminar película",
        description="Elimina una película existente. Requiere autenticación JWT. El usuario solo puede eliminar sus propias películas.",
        parameters=[
            OpenApiParameter(
                name="pk",
                type=int,
                location=OpenApiParameter.PATH,
                description="ID de la película a eliminar",
                required=True
            )
        ],
        responses={
            204: OpenApiResponse(description="Película eliminada correctamente"),
            403: OpenApiResponse(description="No tienes permiso"),
            404: OpenApiResponse(description="Película no encontrada"),
            401: OpenApiResponse(description="No autenticado"),
        }
    )
    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)

            # QUE LA PELÍCULA PERTENECE AL USUARIO
            if movie.user != request.user:
                return Response(
                    {"error": "No tienes permiso para eliminar esta película"},
                    status=status.HTTP_403_FORBIDDEN
                )

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



