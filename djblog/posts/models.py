from django.db import models

# CREAMOS EL MODELO
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField( default=1)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


# PARA EJECUTAR EL MODELO Y SE TRANFORME EN SQL PRA CREAR LA TABLA POST
# PARA LO CUAL CREAMOS LA MIGRACION
# python3 manage.py makemigrations
# python3 manage.py migrate
# PARA ALTERAR LA TABLA BASTA CON SOLO AGREGAR CAMPOS
