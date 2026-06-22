from django.db import models
 # MODELO DE USUARIO
from django.contrib.auth.models  import AbstractUser

class User(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.username




