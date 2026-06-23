# apiMovie
API RESTful para la gestión de películas con autenticación JWT. Permite crear, leer, actualizar y eliminar películas. 
## 
Encontraras el archivo **requirements.txt** con las dependencias requeridas por este.

![Home Page de la API](https://github.com/moleculax/Django/blob/main/apimovie/capturasP/home.png?raw=true)

![Documentación Swagger de la API](https://github.com/moleculax/Django/blob/main/apimovie/capturasP/docs.png?raw=true)


# Estructura

```
.
├── apimovie
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   ├── settings.cpython-313.pyc
│   │   ├── urls.cpython-313.pyc
│   │   ├── views.cpython-313.pyc
│   │   └── wsgi.cpython-313.pyc
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── movie
│   ├── admin.py
│   ├── apps.py
│   ├── image
│   │   └── 2026
│   │       └── 06
│   │           └── insertion.jpeg
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_movie_link.py
│   │   ├── 0003_alter_movie_release_date.py
│   │   ├── 0004_movie_image.py
│   │   ├── 0005_movie_user_alter_movie_image.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-313.pyc
│   │       ├── 0002_movie_link.cpython-313.pyc
│   │       ├── 0003_alter_movie_release_date.cpython-313.pyc
│   │       ├── 0004_movie_image.cpython-313.pyc
│   │       ├── 0005_movie_user_alter_movie_image.cpython-313.pyc
│   │       └── __init__.cpython-313.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-313.pyc
│   │   ├── apps.cpython-313.pyc
│   │   ├── __init__.cpython-313.pyc
│   │   ├── models.cpython-313.pyc
│   │   ├── serializers.cpython-313.pyc
│   │   ├── urls.cpython-313.pyc
│   │   └── views.cpython-313.pyc
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
├── requirements.txt
├── templates
│   └── home.html
└── user
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-313.pyc
    │       └── __init__.cpython-313.pyc
    ├── models.py
    ├── __pycache__
    │   ├── admin.cpython-313.pyc
    │   ├── apps.cpython-313.pyc
    │   ├── __init__.cpython-313.pyc
    │   ├── models.cpython-313.pyc
    │   ├── serializers.cpython-313.pyc
    │   ├── urls.cpython-313.pyc
    │   └── views.cpython-313.pyc
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py

```