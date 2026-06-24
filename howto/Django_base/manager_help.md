# COMANDOS DE DJANGO MANAGE.PY - GUÍA COMPLETA

## [auth] - AUTENTICACIÓN Y USUARIOS

**changepassword**
Cambia la contraseña de un usuario existente. Te pide el nombre de usuario y la nueva contraseña.

**createsuperuser**
Crea un superusuario (administrador) con acceso total al panel de admin. Te pide username, email y contraseña.

---

## [contenttypes] - TIPOS DE CONTENIDO

**remove_stale_contenttypes**
Elimina registros de contenttypes que ya no tienen una aplicación asociada (limpieza de datos huérfanos).

---

## [django] - COMANDOS PRINCIPALES DEL FRAMEWORK

**check**
Verifica que tu proyecto no tenga errores de configuración o sintaxis. Útil antes de desplegar.

**compilemessages**
Compila archivos de traducción (.po a .mo) para internacionalización (i18n).

**createcachetable**
Crea la tabla en la base de datos para usar caché con DatabaseCache.

**dbshell**
Abre una consola interactiva de la base de datos (SQL) directamente desde Django.

**diffsettings**
Muestra las diferencias entre tu settings.py y la configuración por defecto de Django.

**dumpdata**
Exporta los datos de la base de datos a un archivo (JSON, XML, YAML). Útil para hacer backups.

**flush**
Elimina todos los datos de la base de datos (resetea las tablas) pero mantiene la estructura.

**inspectdb**
Inspecciona la base de datos y genera automáticamente modelos de Django (reverse engineering).

**loaddata**
Carga datos desde un archivo (creado con dumpdata) a la base de datos.

**makemessages**
Crea/actualiza archivos de traducción (.po) para internacionalización.

**makemigrations**
Crea archivos de migración basados en los cambios que hiciste en tus modelos.

**migrate**
Aplica las migraciones pendientes a la base de datos (crea/modifica tablas).

**optimizemigration**
Optimiza migraciones existentes para hacerlas más eficientes.

**sendtestemail**
Envía un correo de prueba para verificar que la configuración de email está bien.

**shell**
Abre una consola interactiva de Python con el entorno de Django cargado.

**showmigrations**
Muestra el estado de las migraciones (cuáles están aplicadas y cuáles pendientes).

**sqlflush**
Muestra el comando SQL que se ejecutaría al hacer flush (sin ejecutarlo).

**sqlmigrate**
Muestra el SQL que generará una migración específica (sin ejecutarlo).

**sqlsequencereset**
Resetea las secuencias de IDs en PostgreSQL después de cargar datos.

**squashmigrations**
Combina varias migraciones en una sola para simplificar el historial.

**startapp**
Crea una nueva aplicación dentro del proyecto (estructura de carpetas).

**startproject**
Crea un nuevo proyecto Django (estructura inicial).

**test**
Ejecuta las pruebas unitarias de tu proyecto.

**testserver**
Ejecuta el servidor de desarrollo con datos de prueba cargados desde una fixture.

---

## [drf_spectacular] - DOCUMENTACIÓN DE API (DRF)

**spectacular**
Genera un esquema OpenAPI (JSON/YAML) de tu API para documentación con Swagger/Redoc.

---

## [rest_framework] - DJANGO REST FRAMEWORK

**generateschema**
Genera un esquema de API (similar a spectacular pero de DRF).

---

## [sessions] - SESIONES

**clearsessions**
Elimina todas las sesiones expiradas de la base de datos.

---

## [staticfiles] - ARCHIVOS ESTÁTICOS

**collectstatic**
Recolecta todos los archivos estáticos de tus apps y los copia en STATIC_ROOT para producción.

**findstatic**
Busca un archivo estático específico y muestra su ruta.

**runserver**
Inicia el servidor de desarrollo local (HTTP).

---

# RESUMEN POR CATEGORÍA

## Auth
- **changepassword**, **createsuperuser**
- Gestión de usuarios y autenticación

## Base de datos
- **makemigrations**, **migrate**, **showmigrations**, **sqlmigrate**, **sqlflush**, **sqlsequencereset**, **squashmigrations**, **optimizemigration**
- Crear y aplicar cambios en la BD

## Datos
- **dumpdata**, **loaddata**, **flush**
- Exportar/importar/limpiar datos

## Depuración
- **check**, **shell**, **dbshell**, **diffsettings**
- Verificar y depurar el proyecto

## Internacionalización
- **makemessages**, **compilemessages**
- Traducciones y multi-idioma

## Estáticos
- **collectstatic**, **findstatic**
- Manejo de archivos estáticos

## Pruebas
- **test**, **testserver**
- Ejecutar tests y servidor de prueba

## Inicio de proyecto
- **startproject**, **startapp**
- Crear nuevos proyectos/apps

## Documentación API
- **spectacular**, **generateschema**
- Generar documentación OpenAPI

---

