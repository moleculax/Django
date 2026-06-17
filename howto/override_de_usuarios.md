# 👤 OVERRIDE DE USUARIOS EN DJANGO - GUÍA COMPLETA

## 🔍 ¿QUÉ ES EL OVERRIDE DE USUARIOS?

El override de usuarios en Django consiste en crear un modelo de usuario personalizado en lugar de utilizar el modelo predeterminado `auth.User` que Django proporciona por defecto. Esta práctica es fundamental porque permite adaptar el sistema de autenticación y gestión de usuarios a las necesidades específicas de cada aplicación, agregando campos adicionales como teléfono, dirección, fecha de nacimiento, biografía, avatar, o cualquier otro dato que sea relevante para el negocio. Django recomienda encarecidamente definir un modelo de usuario personalizado al inicio de cualquier proyecto, incluso si inicialmente no se necesitan campos adicionales. La razón principal es que cambiar el modelo de usuario después de haber realizado migraciones y tener datos en la base de datos es extremadamente complejo y puede requerir procedimientos manuales riesgosos. Existen tres métodos principales para personalizar el modelo de usuario en Django. AbstractUser es el método recomendado porque mantiene toda la funcionalidad del modelo original y solo agrega campos adicionales. AbstractBaseUser ofrece control total sobre el modelo pero requiere implementar manualmente varias funcionalidades como el sistema de autenticación. Profile utiliza una relación uno a uno con el modelo de usuario existente y es útil cuando no se puede modificar el modelo de usuario principal.

## 🛠️ IMPLEMENTACIÓN COMPLETA CON ABSTRACTUSER

Crear la aplicación: python manage.py startapp users

Definir el modelo personalizado en users/models.py:

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    website = models.URLField(blank=True)
    is_verified = models.BooleanField(default=False)
    puntos = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
    
    def get_edad(self):
        if self.fecha_nacimiento:
            from datetime import date
            today = date.today()
            return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return None

Configurar Django en settings.py: AUTH_USER_MODEL = 'users.CustomUser'

Registrar en el admin en users/admin.py:

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información personal adicional', {
            'fields': ('telefono', 'fecha_nacimiento', 'direccion', 'bio', 'avatar', 'website')
        }),
        ('Permisos adicionales', {
            'fields': ('is_verified', 'puntos')
        }),
    )
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_verified')
    list_filter = ('is_active', 'is_verified', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)

Crear y aplicar migraciones: python manage.py makemigrations y python manage.py migrate

Crear superusuario: python manage.py createsuperuser

## 🧪 EJEMPLO PRÁCTICO COMPLETO CON USO

En users/models.py con todos los campos necesarios:

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Campos de perfil
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)
    
    # Campos personales
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    
    # Campos de estado
    is_verified = models.BooleanField(default=False)
    puntos = models.IntegerField(default=0)
    
    # Campos de preferencias
    notificaciones_email = models.BooleanField(default=True)
    notificaciones_push = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
    
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}".strip()
        return self.username
    
    def get_edad(self):
        if self.fecha_nacimiento:
            from datetime import date
            today = date.today()
            return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return None

En settings.py: AUTH_USER_MODEL = 'users.CustomUser'

En users/admin.py:

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {
            'fields': ('first_name', 'last_name', 'email', 'telefono', 'fecha_nacimiento', 'direccion', 'ciudad', 'pais')
        }),
        ('Perfil', {
            'fields': ('avatar', 'bio', 'website')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_verified', 'groups', 'user_permissions')
        }),
        ('Configuración', {
            'fields': ('notificaciones_email', 'notificaciones_push', 'puntos')
        }),
        ('Fechas importantes', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_verified')
    list_filter = ('is_active', 'is_verified', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(CustomUser, CustomUserAdmin)

Formularios personalizados en users/forms.py:

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'telefono')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya está registrado')
        return email

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

Vista de perfil en users/views.py:

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def perfil_usuario(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user_profile': user,
        'edad': user.get_edad(),
    }
    return render(request, 'users/perfil.html', context)

Plantilla de perfil en users/templates/users/perfil.html:

{% extends 'base.html' %}

{% block content %}
<div class="container">
    <div class="row">
        <div class="col-md-4">
            <div class="card">
                <div class="card-body text-center">
                    {% if user_profile.avatar %}
                        <img src="{{ user_profile.avatar.url }}" alt="Avatar" class="img-fluid rounded-circle" style="width: 150px; height: 150px; object-fit: cover;">
                    {% else %}
                        <div style="width: 150px; height: 150px; background-color: #ccc; border-radius: 50%; margin: 0 auto;"></div>
                    {% endif %}
                    <h3 class="mt-3">{{ user_profile.get_full_name }}</h3>
                    <p class="text-muted">@{{ user_profile.username }}</p>
                    <p>{{ user_profile.bio }}</p>
                </div>
            </div>
        </div>
        <div class="col-md-8">
            <div class="card">
                <div class="card-body">
                    <h4>Información Personal</h4>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item"><strong>Email:</strong> {{ user_profile.email }}</li>
                        <li class="list-group-item"><strong>Teléfono:</strong> {{ user_profile.telefono|default:"No especificado" }}</li>
                        <li class="list-group-item"><strong>Fecha de nacimiento:</strong> {{ user_profile.fecha_nacimiento|default:"No especificado" }}</li>
                        <li class="list-group-item"><strong>Edad:</strong> {{ edad|default:"No especificado" }}</li>
                        <li class="list-group-item"><strong>Dirección:</strong> {{ user_profile.direccion|default:"No especificado" }}</li>
                        <li class="list-group-item"><strong>Ciudad:</strong> {{ user_profile.ciudad|default:"No especificado" }}</li>
                        <li class="list-group-item"><strong>País:</strong> {{ user_profile.pais|default:"No especificado" }}</li>
                        <li class="list-group-item"><strong>Website:</strong> {% if user_profile.website %}<a href="{{ user_profile.website }}" target="_blank">{{ user_profile.website }}</a>{% else %}No especificado{% endif %}</li>
                    </ul>
                </div>
            </div>
            <div class="card mt-3">
                <div class="card-body">
                    <h4>Estadísticas</h4>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item"><strong>Puntos:</strong> {{ user_profile.puntos }}</li>
                        <li class="list-group-item"><strong>Verificado:</strong> {% if user_profile.is_verified %}✅ Sí{% else %}❌ No{% endif %}</li>
                        <li class="list-group-item"><strong>Fecha de registro:</strong> {{ user_profile.date_joined }}</li>
                        <li class="list-group-item"><strong>Último acceso:</strong> {{ user_profile.last_login|default:"Nunca" }}</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}

## 🔧 SEÑALES PARA CREAR PERFIL AUTOMÁTICAMENTE

En users/signals.py:

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

En users/apps.py:

from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    def ready(self):
        import users.signals

En __init__.py de users: default_app_config = 'users.apps.UsersConfig'

## ⚠️ CONSIDERACIONES IMPORTANTES

Definir el modelo al inicio del proyecto porque cambiar AUTH_USER_MODEL después de las migraciones es extremadamente complicado. Siempre usar get_user_model() para referenciar al modelo de usuario: from django.contrib.auth import get_user_model User = get_user_model(). Si ya tienes datos en producción, usa el método Profile en lugar de modificar el modelo principal. Realizar migraciones inmediatamente después de definir el modelo. Configurar correctamente el admin y los formularios para que el modelo personalizado funcione correctamente en el panel de administración.

## 🔍 COMPARACIÓN DE MÉTODOS

AbstractUser: Complejidad baja, mantiene funcionalidad original, solo agrega campos, recomendado para la mayoría.

AbstractBaseUser: Complejidad alta, control total, implementación manual, para necesidades específicas.

Profile: Complejidad media, no modifica el modelo original, usa relación uno a uno, para proyectos existentes.

## 🧩 MÉTODO PROFILE PARA PROYECTOS EXISTENTES

En models.py:

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.TextField(blank=True)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"

En admin.py:

from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'fecha_nacimiento')
    search_fields = ('user__username', 'user__email')

admin.site.register(Profile, ProfileAdmin)

Señales para crear perfil automáticamente igual que en el método anterior.

## ✅ CONCLUSIÓN

El override de usuarios en Django es una práctica esencial que permite adaptar el sistema de autenticación a las necesidades específicas de cada aplicación. El método más simple y recomendado para la mayoría de los casos es utilizar AbstractUser, que mantiene toda la funcionalidad del modelo original mientras permite agregar campos personalizados. Implementar un modelo de usuario personalizado requiere crear una aplicación dedicada, definir el modelo heredando de AbstractUser, configurar Django para que lo utilice, registrar el modelo en el panel de administración, y finalmente crear y aplicar migraciones. Este proceso es sencillo y proporciona una base sólida para la gestión de usuarios en cualquier proyecto Django. Es importante recordar que esta decisión debe tomarse al inicio del proyecto y que siempre se debe utilizar get_user_model() para referenciar al modelo de usuario.

