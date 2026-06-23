# from django.db import models
#
# # CREAMOS EL MODELO
# class Movie(models.Model):
#     title = models.CharField(max_length=200)
#     release_date = models.DateField(null=True, blank=True)
#     duration = models.PositiveIntegerField()
#     sinopsis = models.TextField()
#     link = models.URLField(max_length=500, blank=True, null=True)
#     image = models.ImageField(upload_to='movie/image/%Y/%m', blank=True, null=True)
#     user_id = models.IntegerField(blank=True, null=True)
#
#     def __str__(self): # es un método especial de Python que devuelve la representación en cadena de un objeto.
#         return f"{self.id} - {self.title}" #devuelve una cadena con el formato id - título.


from django.db import models
from django.conf import settings


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField()
    sinopsis = models.TextField()
    link = models.URLField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='movie/image/%Y/%m', blank=True, null=True)

    # RELACIÓN CON EL USUARIO
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='movies',
        null=True,
        blank=True
    )

    # NOTA: Django crea automáticamente el campo 'user_id' en la base de datos

    def __str__(self):
        return f"{self.id} - {self.title}"

