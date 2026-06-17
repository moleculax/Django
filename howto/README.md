# 🚀 Django - API

Una API REST robusta y escalable para gestionar una tienda en línea, construida con **Django** y **Django REST Framework**. Permite la administración de productos, carrito de compras, procesamiento de órdenes de pago y autenticación segura de usuarios.

---

## 🛠️ Tecnologías - Utilizar

* **Backend:** [Django](https://djangoproject.com) (v5.0+)
* **API REST:** [Django REST Framework](https://django-rest-framework.org)
* **Base de Datos:** PostgreSQL / SQLite (Desarrollo)
* **Autenticación:** JWT (JSON Web Tokens) con Simple JWT
* **Entorno Virtual:** `venv` / `pip`

---

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado en tu sistema:
* Python 3.10 o superior
* Git
* Pip (Administrador de paquetes de Python)

---

## ⚙️ Instalación y Configuración Local

Sigue estos pasos paso a paso para levantar el proyecto en tu entorno local:



### Crear y activar el entorno virtual
En Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```


### Instalar las dependencias si clonaste un proyecto
```bash
pip install -r requirements.txt
```

### Configurar las variables de entorno
Crea un archivo `.env` en la raíz del proyecto basándote en el archivo de ejemplo:
```bash
cp .env.example .env
```
Abre el archivo `.env` y define tu `SECRET_KEY`, `DEBUG=True`, y las credenciales de tu base de datos si usas PostgreSQL.

###  Ejecutar las migraciones
Crea las tablas necesarias en la base de datos:
```bash
python manage.py migrate
```

### Crear un superusuario (Administrador)
Para acceder al panel de administración de Django:
```bash
python manage.py createsuperuser
```

### Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```
El proyecto estará disponible en tu navegador en: `http://127.0.0`

---

## 🧪 Ejecución de Pruebas Unificadas (Tests)

Para correr la suite de pruebas automatizadas ejecuta:
```bash
python manage.py test
```

---

## 📁 Estructura Principal del Proyecto

```text
├── core/                  # Configuración principal de Django (settings, urls, wsgi)
├── apps/                  # Directorio para las aplicaciones del proyecto
│   ├── authentication/    # Gestión de usuarios y perfiles
│   ├── products/          # Gestión del catálogo de productos
│   └── orders/            # Gestión de carritos y pedidos
├── static/                # Archivos estáticos (CSS, JS, Imágenes)
├── templates/             # Plantillas HTML (si aplica)
├── .env.example           # Plantilla de variables de entorno
├── manage.py              # Script de gestión de Django
└── requirements.txt       # Dependencias del proyecto
```

---

## 📌 Puntos de Entrada Clave de la API (Endpoints)

| Método | Endpoint | Descripción | Acceso |
| :--- | :--- | :--- | :--- |
| **POST** | `/api/auth/register/` | Registro de nuevos usuarios | Público |
| **POST** | `/api/auth/login/` | Obtención de tokens JWT | Público |
| **GET** | `/api/products/` | Listar todos los productos | Público |
| **POST** | `/api/products/` | Crear un producto nuevo | Solo Administrador |
| **POST** | `/api/orders/` | Generar una nueva orden de compra | Autenticado |

---

## ✒️ Autor

* **EjGomez** - *github* - [moleculax](https://github.com/moleculax/)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
