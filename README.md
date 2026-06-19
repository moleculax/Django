#  Django (project - Crudos en desarrollo)


| Tecnología | Descripción |
|------------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Lenguaje de programación principal de alto nivel. |
| ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) | Entorno de desarrollo web enfocado en la velocidad y la seguridad. |
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) | Sistema de base de datos relacional avanzado y de código abierto. |
| ![Debian](https://img.shields.io/badge/Debian-A81D33?style=for-the-badge&logo=debian&logoColor=white) | Sistema operativo servidor para un entorno de despliegue estable. |
| ![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white) | Entorno de desarrollo integrado (IDE) para Python. |

---

##  Descripción

**Proyecto (ejemplo) desarrollado con Django.**

**En Desarrollo...**

# Django -  Esencial



### Crear entorno virtual

```bash
# Linux / macOS
python3 -m venv env

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

**PARA EJECUTAR EL MODELO Y  CREAR LA TABLAS**
```
 python3 manage.py makemigrations
 python3 manage.py migrate  
 ```  
 
 
**PARA REST FRAMEWORK**
```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

Django Rest [www.django-rest-framework.org](https://www.django-rest-framework.org/) 

Web: [Moleculax App](https://moleculaxapp.vercel.app/)