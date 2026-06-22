from django.db import models

# CREAMOS EL MODELO
class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    sinopsis = models.TextField()

    def __str__(self): # es un método especial de Python que devuelve la representación en cadena de un objeto.
        return f"{self.id} - {self.title}" #devuelve una cadena con el formato id - título.


