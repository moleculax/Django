from django.db import models
from apps.categories.models import Category   # Importamos el modelo Category

# CREAMOS EL MODELO
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # RELACIÓN CON CATEGORY
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="posts",
        null=True,      # ✅ permite que los posts existentes queden sin categoría
        blank=True      # ✅ permite que el campo quede vacío en formularios
    )

    def __str__(self):
        return self.title


# PARA EJECUTAR EL MODELO Y SE TRANSFORME EN SQL PARA CREAR LA TABLA POST
# PARA LO CUAL CREAMOS LA MIGRACION
# python3 manage.py makemigrations
# python3 manage.py migrate
# PARA ALTERAR LA TABLA BASTA CON SOLO AGREGAR CAMPOS
