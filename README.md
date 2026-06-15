# Proyectos Django

##  Descripción

Proyecto web desarrollado con Django, un framework de alto nivel para Python que permite construir aplicaciones web de manera rápida y segura.

**En Desarrollo...**

# Django - Comandos Esenciales



### Crear entorno virtual

```bash
# Linux / macOS
python3 -m venv env

# Windows
python -m venv env



```
Activar entorno virtual

```
source env/bin/activate

# Debería mostrar (env) al inicio de la línea de comandos
pip list

Eliminar entorno virtual

# Linux 
rm -rf env
```
**Instalar Django**
```
pip install django

Instalacion especifica:

pip install django==5.1

Actualizarlo:

pip install --upgrade django

Exportar dependencias:

pip freeze > requirements.txt

```
**Crear proyecto en directorio actual**

```
django-admin startproject nombre_proyecto .
```

**Estructura del proyecto creado**

```
nombre_proyecto/
├── manage.py
└── nombre_proyecto/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
    
```
    

Web: [Moleculax App](https://moleculaxapp.vercel.app/)