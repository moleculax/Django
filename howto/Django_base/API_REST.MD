# API REST

## ¿Qué es una API?

**API** (Application Programming Interface) es un conjunto de reglas y definiciones que permite que dos aplicaciones se comuniquen entre sí.

### Tipos de API

| Tipo | Descripción |
|------|-------------|
| **SOAP** | Protocolo antiguo, usa XML |
| **REST** | Estilo arquitectónico, usa HTTP |
| **GraphQL** | Permite pedir datos específicos |
| **WebSocket** | Comunicación en tiempo real |

---

## ¿Qué es REST?

**REST** (Representational State Transfer) es un estilo de arquitectura para diseñar APIs que usan HTTP.

### Principios REST

| Principio | Descripción |
|-----------|-------------|
| **Cliente-Servidor** | Separación entre frontend y backend |
| **Sin estado (Stateless)** | Cada petición contiene toda la información necesaria |
| **Cacheable** | Las respuestas pueden almacenarse en caché |
| **Interfaz uniforme** | URLs consistentes y métodos HTTP estándar |
| **Sistema en capas** | Puede haber intermediarios (proxies, balanceadores) |

---

## Métodos HTTP en REST

| Método | Acción | Ejemplo |
|--------|--------|---------|
| **GET** | Obtener datos | `GET /api/users` → Lista usuarios |
| **POST** | Crear recurso | `POST /api/users` → Crear usuario |
| **PUT** | Actualizar todo | `PUT /api/users/1` → Actualizar usuario |
| **PATCH** | Actualizar parcial | `PATCH /api/users/1` → Actualizar email |
| **DELETE** | Eliminar | `DELETE /api/users/1` → Eliminar usuario |

---

## Códigos de estado HTTP

| Código | Significado |
|--------|-------------|
| **200** | OK (éxito) |
| **201** | Creado |
| **400** | Solicitud incorrecta |
| **401** | No autorizado |
| **403** | Prohibido |
| **404** | No encontrado |
| **500** | Error interno del servidor |

---

## Ejemplo de API REST

### GET /api/users

**Petición:**
```http
GET /api/users HTTP/1.1
Host: midominio.com
Accept: application/json
```
Respuesta:
```
[
    { "id": 1, "nombre": "Juan", "email": "juan@email.com" },
    { "id": 2, "nombre": "Maria", "email": "maria@email.com" }
]
```
POST /api/users
Petición:
```
POST /api/users HTTP/1.1
Host: midominio.com
Content-Type: application/json

{
    "nombre": "Pedro",
    "email": "pedro@email.com"
}
```

Respuesta:

```
{
    "message": "Usuario creado",
    "id": 3
}
```

## Resumen

| Término | Definición |
|---------|------------|
| **API** | Conjunto de reglas para comunicación entre sistemas |
| **REST** | Estilo arquitectónico para APIs web |
| **Endpoint** | URL donde se accede a un recurso (`/api/users`) |
| **Recurso** | Entidad que se manipula (usuarios, productos) |
| **JSON** | Formato de datos más usado en REST APIs |