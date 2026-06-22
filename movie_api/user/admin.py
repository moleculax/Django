from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined', 'is_superuser')

    #  Sumar el campo adicional a los fieldsets existentes
    fieldsets = UserAdmin.fieldsets + (
        ('Campos adicionales', {'fields': ('birthdate',)}),
    )


admin.site.register(User, CustomUserAdmin)