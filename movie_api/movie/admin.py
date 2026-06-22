from django.contrib import admin
from movie.models import Movie

class MovieAdmin(admin.ModelAdmin):
    # HORIZONTALES
    list_display = ('title', 'duration', )
    # LATERALES
    list_filter = ('release_date','sinopsis',)

    # CAMPOS DE BÚSQUEDA
    search_fields = ('title', 'sinopsis')
    ordering = ('-release_date',)
# ESTO REGISTRA EL MODELO MOVIE EN EL PANEL ADMINISTRATIVO DE Django
admin.site.register(Movie, MovieAdmin)

