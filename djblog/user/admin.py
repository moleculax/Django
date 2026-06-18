# CREAMOS LA GESTION DE USUARIOS
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# IMPORTAMOS EL MODELO CREADO DEL USUARIO
from user.models import User

@admin.register(User)
# AHORA COMIENZO PERSONALIZACION PARA EL USUARIO EN admin
class UserAdmin(BaseUserAdmin):
    # COLOCA FIELDS POR DEFECTOS
    # pass
    # SI QUEREMOS PERSONALIZAD
    # NOTA: SI IMPECCIONO LA TABLA DEL USUARIO
    # PUEDO VER EL NOMBRE DE LOS fields =
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informacion Personal', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Web Site', {'fields': ('web_site',)}),
        ('Redes Sociales', {'fields': ('linkedin','twitter','instagram')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )





