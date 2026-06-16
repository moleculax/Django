from django.contrib import admin
from posts.models import Post

# ENVIAMOS AL PANEL DEL ADMINISTRADOR

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # NOS MUESTRA EN EL PANEL ADMIN NOMBRE DE LOS CAMPOS COMO ENCABEZADO
    list_display = ('title', 'create_at','update_at', 'status')
    list_filter = ('status',)