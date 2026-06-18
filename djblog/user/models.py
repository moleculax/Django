

# CREADO PARA OVERRRIDE DE USUARIOS
# LO IDEAL ES CREA OVERRRIDE DE USUARIOS APENEAS SE INICIA EL PROYECTO

from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    # pass
    # AGREGAMOS OTROS CAMPOS A USER_USER
    # DESPUES DE AGREGARLOS TENEMOS QUE EJECUTAR makemigrations y migrate
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    web_site = models.URLField(max_length=255, blank=True, null=True)
    # Nuevos campos de redes sociales
    linkedin = models.URLField(max_length=255,blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)

    # CAMBIAMOS PARA LOGUEARNOS CON EL EMAIL Y NO CON EL NOMBRE DE USUARIO
    # HACEMOS EL EMAIL UNICO
    email = models.EmailField(unique=True, max_length=255, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []