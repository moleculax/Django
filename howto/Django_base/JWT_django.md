## JWT en Django
**JWT (JSON Web Tokens)**  es un estándar para autenticación y autorización que permite transmitir información segura entre partes como un objeto JSON. En Django, se usa principalmente con Django REST Framework para autenticación stateless (sin estado).

**📦 Instalación**
django-rest-framework-simplejwt (Recomendado)

```
pip install djangorestframework-simplejwt
```

## 🔧 Configuración básica con SimpleJWT

**Configurar settings.py**

```
# settings.py
from datetime import timedelta

INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework_simplejwt',
    # ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}
```

**Configurar URLs**

```
# urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
```

##📝 Uso básico

**Obtener token (Login)**

```
import requests

# POST a /api/token/
response = requests.post('http://localhost:8000/api/token/', json={
    'username': 'admin',
    'password': 'admin123'
})

# Respuesta
{
    'access': 'eyJhbGciOiJIUzI1NiIs...',
    'refresh': 'eyJhbGciOiJIUzI1NiIs...'
}
```

**Usar token en requests**

```
headers = {
    'Authorization': f'Bearer {access_token}'
}
response = requests.get('http://localhost:8000/api/protegida/', headers=headers)
```

## ::. Nota .::
**Consulte para mas informacion:**
[https://django-rest-framework-simplejwt.readthedocs.io/en/latest/](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

**Este archivo se actualiza constantemente**
```
.
.
.
```

