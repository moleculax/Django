# movie_api

## 
Este repositorio tiene  movies_api, donde estan los archivos del proyecto de Django REST.
Los archivos de configuración y las aplicaciones. Encontraras el archivo **requirements.txt** con las dependencias requeridas por este.

## Instalación

1. Usa
   ``` 
   Python 3.x
   PyCharm
2. Librerías

		pip install -r requirements.txt

3. Ingresa al directorio

		cd movies_api

4. Crea las migraciones

		python manage.py makemigrations

5. Aplica las migraciones

		python manage.py migrate

6. Crea un super usuario para el administrador

		python manage.py createsuperuser

7. Corre el proyecto

		python manage.py runserver


Estructura

```
.
├── db.sqlite3
├── manage.py
├── movie
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-313.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-313.pyc
│   │   ├── apps.cpython-313.pyc
│   │   ├── __init__.cpython-313.pyc
│   │   ├── models.cpython-313.pyc
│   │   └── urls.cpython-313.pyc
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── movie_api
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   ├── settings.cpython-313.pyc
│   │   ├── urls.cpython-313.pyc
│   │   └── wsgi.cpython-313.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
└── requirements.txt
```

