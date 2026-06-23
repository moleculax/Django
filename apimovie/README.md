# 🎬 apiMovie

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)

API RESTful (Ejemplo) para la gestión de películas con autenticación JWT. Permite crear, leer, actualizar y eliminar películas.

---

## 🛠️ Tecnologías utilizadas

- **Django** - Framework web de alto nivel.
- **Django REST Framework** - Para construir la API.
- **JWT (JSON Web Tokens)** - Para autenticación segura.
- **SQLite** - Base de datos por defecto (puedes cambiarla).

---

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/moleculax/Django.git
cd Django/apimovie
```

2. Crea un entorno virtual y actívalo:

```
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```
pip install -r requirements.txt
```
4. Realiza las migraciones:
```
python3 manage.py makemigrations

python3 manage.py migrate
```
5. Crea un superusuario:
```
python3 manage.py createsuperuser
```
6. Ejecuta el servidor:
```
python manage.py runserver
```
Para acceder al panel administrativo de Django:

http://localhost:8000/admin/



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