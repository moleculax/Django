## Decoradores
Los decoradores en Django son funciones que modifican el comportamiento de otras funciones (vistas, métodos, etc.) sin cambiar su código fuente. Son una característica poderosa de Python que Django aprovecha extensamente.


## 📚 Referencia rápida de decoradores Django


### Decoradores de autenticación y permisos

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@login_required` | `django.contrib.auth.decorators` | Requiere que el usuario esté autenticado |
| `@permission_required` | `django.contrib.auth.decorators` | Requiere permisos específicos del usuario |
| `@user_passes_test` | `django.contrib.auth.decorators` | Requiere que el usuario pase una prueba personalizada |

### Decoradores de métodos HTTP

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@require_GET` | `django.views.decorators.http` | Solo permite método HTTP GET |
| `@require_POST` | `django.views.decorators.http` | Solo permite método HTTP POST |
| `@require_http_methods` | `django.views.decorators.http` | Limita a métodos HTTP específicos |
| `@require_safe` | `django.views.decorators.http` | Solo permite métodos seguros (GET, HEAD) |
| `@conditional_page` | `django.views.decorators.http` | Respuesta condicional basada en headers |

### Decoradores de CSRF

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@csrf_exempt` | `django.views.decorators.csrf` | Deshabilita la protección CSRF |
| `@csrf_protect` | `django.views.decorators.csrf` | Fuerza la protección CSRF |
| `@csrf_exempt` (CBV) | `django.views.decorators.csrf` | Deshabilita CSRF para vistas basadas en clases |
| `@ensure_csrf_cookie` | `django.views.decorators.csrf` | Asegura que se establezca la cookie CSRF |

### Decoradores de caché

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@cache_page` | `django.views.decorators.cache` | Cachea la respuesta por un tiempo determinado |
| `@never_cache` | `django.views.decorators.cache` | Previene que la respuesta sea cacheada |
| `@cache_control` | `django.views.decorators.cache` | Controla directivas de caché HTTP |
| `@vary_on_cookie` | `django.views.decorators.vary` | Varía el caché según cookies |
| `@vary_on_headers` | `django.views.decorators.vary` | Varía el caché según cabeceras HTTP |

### Decoradores del panel de administración

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@admin.register` | `django.contrib.admin` | Registra un modelo en el panel de administración |
| `@admin.display` | `django.contrib.admin` | Personaliza la visualización de campos en el admin |
| `@admin.action` | `django.contrib.admin` | Define acciones personalizadas en el admin |

### Decoradores de Django REST Framework

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@api_view` | `rest_framework.decorators` | Convierte una función en vista DRF |
| `@action` | `rest_framework.decorators` | Añade acción personalizada a ViewSet |
| `@permission_classes` | `rest_framework.decorators` | Define permisos para vista DRF |
| `@authentication_classes` | `rest_framework.decorators` | Define autenticación para vista DRF |
| `@throttle_classes` | `rest_framework.decorators` | Define clases de limitación de tasa |
| `@renderer_classes` | `rest_framework.decorators` | Define clases de renderizado |
| `@parser_classes` | `rest_framework.decorators` | Define clases de parseo |
| `@schema` | `rest_framework.decorators` | Personaliza la documentación OpenAPI |
| `@extend_schema` | `drf_spectacular.decorators` | Extiende la documentación OpenAPI (drf-spectacular) |
| `@swagger_auto_schema` | `drf_yasg.decorators` | Personaliza documentación Swagger (drf-yasg) |

### Decoradores de respuesta y contenido

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@gzip_page` | `django.views.decorators.gzip` | Comprime la respuesta con GZip |
| `@etag` | `django.views.decorators.http` | Establece ETag para la respuesta |
| `@last_modified` | `django.views.decorators.http` | Establece cabecera Last-Modified |
| `@xframe_options_exempt` | `django.views.decorators.clickjacking` | Permite embebido en frames |
| `@xframe_options_deny` | `django.views.decorators.clickjacking` | Deniega embebido en frames |
| `@xframe_options_sameorigin` | `django.views.decorators.clickjacking` | Permite embebido solo del mismo origen |

### Decoradores para vistas basadas en clases (CBV)

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@method_decorator` | `django.utils.decorators` | Aplica decoradores a métodos de CBV |
| `@classonlymethod` | `django.utils.decorators` | Marca método como solo de clase |

### Decoradores de tiempo de ejecución

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@sensitive_variables` | `django.views.decorators.debug` | Oculta variables sensibles en errores |
| `@sensitive_post_parameters` | `django.views.decorators.debug` | Oculta parámetros POST sensibles |

### Decoradores de middleware (personalizados)

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@decorator_from_middleware` | `django.utils.decorators` | Convierte middleware en decorador |
| `@decorator_from_middleware_with_args` | `django.utils.decorators` | Convierte middleware con argumentos en decorador |

### Decoradores asíncronos

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@sync_only` | `django.utils.asyncio` | Restringe función para solo sincrónico |
| `@async_only` | `django.utils.asyncio` | Restringe función para solo asíncrono |
| `@sync_to_async` | `django.utils.asyncio` | Convierte función sincrónica a asíncrona |
| `@async_to_sync` | `django.utils.asyncio` | Convierte función asíncrona a sincrónica |

### Decoradores de testing

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@override_settings` | `django.test.utils` | Sobrescribe settings para pruebas |
| `@modify_settings` | `django.test.utils` | Modifica settings existentes para pruebas |
| `@tag` | `django.test.utils` | Etiqueta pruebas para ejecución selectiva |
| `@skipIfDBFeature` | `django.test.utils` | Salta prueba si DB tiene característica |
| `@skipUnlessDBFeature` | `django.test.utils` | Salta prueba a menos que DB tenga característica |

### Decoradores de internacionalización

| Decorador | Módulo | Propósito |
|-----------|--------|-----------|
| `@translations` | `django.utils.translation` | Marca función para traducción |
| `@non_atomic_requests` | `django.db.transaction` | Deshabilita atomicidad en requests |

### Decoradores de terceros comunes

| Decorador | Biblioteca | Propósito |
|-----------|-----------|-----------|
| `@login_required` (extendido) | `django.contrib.auth.decorators` | Extensión para redirección AJAX |
| `@staff_member_required` | `django.contrib.admin.decorators` | Requiere usuario staff (interno) |
| `@superuser_required` | `django.contrib.admin.decorators` | Requiere superusuario |
| `@group_required` | `django.contrib.auth.decorators` | Requiere grupos específicos |
| `@ratelimit` | `django-ratelimit` | Limita tasa de requests |
| `@cache_page` (variantes) | `django.views.decorators.cache` | Cache con timeout personalizado |
| `@sensitive_data` | `django.views.decorators.debug` | Marca datos como sensibles |
| `@validate_email` | `django.views.decorators` | Valida email en request |
| `@cors_allow` | `django-cors-headers` | Permite CORS para vista específica |
| `@login_required_ajax` | `django.contrib.auth.decorators` | Login requerido con soporte AJAX |

## 📝 Sintaxis rápida

### Aplicar múltiples decoradores
```python
@login_required
@require_GET
@cache_page(60 * 5)
def mi_vista(request):
    pass