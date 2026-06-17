## DOCUMENTACIÓN DE DESPLIEGUE (Referencial) DJANGO CON APACHE

**UBICACIÓN DEL PROYECTO:**
```
/home/usuario/neurocode/djblog
```
**ENTORNO VIRTUAL:**
```
/home/usuario/neurocode/env
```
**ARCHIVO: djblog/settings.py**
```
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'posts',
    'home',
    'nosotros',
]
```
**ARCHIVO: .env (en la raíz del proyecto)**
```
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com,localhost
DB_NAME=nombre_bd
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=5432
```
**ARCHIVO: requirements.txt**
```
Django>=4.2
gunicorn>=21.2.0
psycopg2-binary>=2.9.0
python-dotenv>=1.0.0
djangorestframework>=3.14.0
drf-spectacular>=0.27.0
```
**ARCHIVO: /etc/apache2/sites-available/djblog.conf**
```
<VirtualHost *:80>
    ServerAdmin admin@tudominio.com
    ServerName tudominio.com
    ServerAlias www.tudominio.com
    DocumentRoot /home/usuario/neurocode/djblog
    Alias /static/ /home/usuario/neurocode/djblog/staticfiles/
    <Directory /home/usuario/neurocode/djblog/staticfiles/>
        Require all granted
    </Directory>
    Alias /media/ /home/usuario/neurocode/djblog/media/
    <Directory /home/usuario/neurocode/djblog/media/>
        Require all granted
    </Directory>
    WSGIScriptAlias / /home/usuario/neurocode/djblog/djblog/wsgi.py
    WSGIDaemonProcess djblog python-home=/home/usuario/neurocode/env python-path=/home/usuario/neurocode/djblog
    WSGIProcessGroup djblog
    <Directory /home/usuario/neurocode/djblog/djblog>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/djblog-error.log
    CustomLog ${APACHE_LOG_DIR}/djblog-access.log combined
</VirtualHost>
```
**COMANDOS DE INSTALACIÓN (ejecutar en orden)**

**INSTALAR APACHE**
```
sudo apt update
sudo apt install apache2
sudo apt install libapache2-mod-wsgi-py3
sudo a2enmod wsgi
sudo a2enmod headers
sudo a2enmod rewrite
sudo systemctl restart apache2
```
I**NSTALAR POSTGRESQL**
```
sudo apt install postgresql postgresql-contrib
sudo -u postgres psql
-- Dentro de PostgreSQL ejecutar:
CREATE DATABASE nombre_bd;
CREATE USER usuario WITH PASSWORD 'contraseña';
ALTER ROLE usuario SET client_encoding TO 'utf8';
ALTER ROLE usuario SET default_transaction_isolation TO 'read committed';
ALTER ROLE usuario SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE nombre_bd TO usuario;
\q
```
**CONFIGURAR PROYECTO**
```
cd /home/usuario/neurocode/djblog
source ../env/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
```
**CONFIGURAR PERMISOS**
```
sudo chown -R www-data:www-data /home/usuario/neurocode/djblog
sudo chmod -R 755 /home/usuario/neurocode/djblog
sudo chown -R www-data:www-data /home/usuario/neurocode/djblog/staticfiles
sudo chown -R www-data:www-data /home/usuario/neurocode/djblog/media
sudo chown -R www-data:www-data /home/usuario/neurocode/env
sudo chmod -R 755 /home/usuario/neurocode/env
```
**ACTIVAR SITIO EN APACHE**
```
sudo a2ensite djblog.conf
sudo a2dissite 000-default.conf
sudo apache2ctl configtest
sudo systemctl restart apache2
```
**CONFIGURAR SSL (opcional)**
```
sudo apt install certbot python3-certbot-apache
sudo certbot --apache -d tudominio.com -d www.tudominio.com
```
**COMANDOS DE MANTENIMIENTO**
```
sudo apache2ctl configtest
sudo systemctl restart apache2
sudo tail -f /var/log/apache2/djblog-error.log
sudo tail -f /var/log/apache2/djblog-access.log
sudo systemctl status apache2
```
**ACTUALIZAR PROYECTO**
```
cd /home/usuario/neurocode/djblog
git pull
source ../env/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
sudo systemctl restart apache2
```
**SOLUCIÓN DE PROBLEMAS COMUNES**
```
PROBLEMA: Permission denied
SOLUCIÓN: sudo chown -R www-data:www-data /home/usuario/neurocode/djblog
          sudo chmod -R 755 /home/usuario/neurocode/djblog
PROBLEMA: ModuleNotFoundError
SOLUCIÓN: Verificar que python-path apunte al entorno virtual correcto
PROBLEMA: 502 Bad Gateway
SOLUCIÓN: sudo a2enmod wsgi && sudo systemctl restart apache2
PROBLEMA: Static files no cargan
SOLUCIÓN: python manage.py collectstatic --noinput
PROBLEMA: Error de base de datos
SOLUCIÓN: Verificar credenciales en .env
```
**ESTRUCTURA DEL PROYECTO**
```
/home/usuario/neurocode/djblog/
├── data/
│   └── personas.json
├── djblog/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home/
│   └── views.py
├── nosotros/
│   └── views.py
├── posts/
│   └── views.py
├── static/
├── staticfiles/
├── media/
├── templates/
├── manage.py
├── .env
└── requirements.txt
```
**INFORMACIÓN IMPORTANTE**
```
Ruta del proyecto:      /home/usuario/neurocode/djblog
Entorno virtual:        /home/usuario/neurocode/env
Logs de errores:        /var/log/apache2/djblog-error.log
Logs de acceso:         /var/log/apache2/djblog-access.log
Configuración Apache:   /etc/apache2/sites-available/djblog.conf
```
**NOTAS FINALES**
```
Fecha de creación:      16 de Junio de 2026
Versión:                1.0
Framework:              Django 4.2+
Servidor:               Apache2 + mod_wsgi
Base de datos:          PostgreSQL
Sistema operativo:      Debian/Ubuntu
