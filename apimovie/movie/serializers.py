from rest_framework import serializers
from .models import Movie
# class MovieSerializer(serializers.Serializer): # ES HIJA DEL MODELO GENERICO DE SELIALIZRES
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)
#     duration = serializers.IntegerField()
#     sinopsis = serializers.CharField(
#         style={'base_template': 'textarea.html'}  # se renderiza como textarea en la API navegable
#     )


# CON MODEL ES MUCHO MAS SENCILLO
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'sinopsis','link']

