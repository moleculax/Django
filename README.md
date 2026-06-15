# Proyectos Django

##  Descripción

Proyecto web desarrollado con Django, un framework de alto nivel para Python que permite construir aplicaciones web de manera rápida y segura.

**En Desarrollo...**

# Manual de Django - Comandos Esenciales

## 📋 Índice

1. [Entornos Virtuales](#entornos-virtuales)
2. [Instalación de Django](#instalación-de-django)
3. [Crear un Proyecto](#crear-un-proyecto)
4. [Crear una Aplicación](#crear-una-aplicación)
5. [Ejecutar el Servidor](#ejecutar-el-servidor)
6. [Migraciones y Base de Datos](#migraciones-y-base-de-datos)
7. [Panel de Administración](#panel-de-administración)
8. [Crear Superusuario](#crear-superusuario)
9. [Comandos Útiles](#comandos-útiles)
10. [Estructura del Proyecto](#estructura-del-proyecto)
11. [Configuración Básica](#configuración-básica)
12. [Solución de Problemas](#solución-de-problemas)

---

## 🐍 Entornos Virtuales

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