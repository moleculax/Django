# Integración de Análisis de Datos con Ollama, Pandas y LangChain

Este proyecto demuestra cómo conectar un entorno local de Python (Spyder/IPython) con una instancia local de **Ollama** para realizar análisis inteligente de datos estructurados utilizando **Pandas** y la abstracción de **LangChain**.

---

## 🚀 Requisitos del Sistema

* **Ollama** instalado y ejecutándose localmente (`http://localhost:11434`).
* **Modelos locales requeridos:**
  * `llama3.2` (Para tareas de chat y análisis).
  * `nomic-embed-text` (Para generación de embeddings y búsquedas semánticas).
* **Python 3.13+** con las siguientes librerías:
  * `pandas`
  * `langchain`
  * `langchain-community`

---

## 🛠️ Solución de Problemas Críticos (Entorno)

### 1. Error de Proxy / Intercepción de Apache (`Error 400`)
Si tu entorno del sistema redirige el tráfico local al puerto `80` (gestionado por Apache), debes forzar conexiones HTTP directas de bajo nivel o asegurarte de omitir las variables de entorno `http_proxy`. El código de este repositorio utiliza conexiones por sockets limpios para evitar que Apache interfiera.

### 2. Entornos Administrados Externamente (`PEP 668`)
Si al intentar instalar librerías mediante `%pip install` en tu consola de Spyder recibes el error `externally-managed-environment`, puedes usar entornos virtuales (`venv`) o forzar la instalación local de las dependencias base de la siguiente manera:
```bash
pip install langchain langchain-community pandas --break-system-packages
```

---

## 💻 Ejemplos de Uso

### Ejemplo 1: Análisis de Datos (Pandas + Ollama Nativo)
Este script procesa una tabla de datos mediante Pandas, elude proxies del sistema utilizando la librería nativa `http.client` e interroga al modelo `llama3.2`.

```python
import http.client
import json
import pandas as pd

# 1. Preparar datos con Pandas
filas = [
    {"Producto": "Laptop", "Cantidad": 2, "Precio_Unitario": 1200},
    {"Producto": "Mouse", "Cantidad": 15, "Precio_Unitario": 25},
    {"Producto": "Monitor 4K", "Cantidad": 4, "Precio_Unitario": 450}
]
df = pd.DataFrame(filas)
df['Total'] = df['Cantidad'] * df['Precio_Unitario']

# 2. Construir el Prompt
prompt = f"Analiza el siguiente reporte de ventas e indica el producto estrella:\n{df.to_string(index=False)}"

# 3. Conexión directa (Bypass Apache)
payload = {"model": "llama3.2", "prompt": prompt, "stream": False}
conn = http.client.HTTPConnection("127.0.0.1", 11434)
conn.request("POST", "/api/generate", body=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})

response = conn.getresponse()
resultado = json.loads(response.read().decode('utf-8'))
print(resultado['response'])
conn.close()
```

### Ejemplo 2: Implementación con LangChain
Una vez resueltos los problemas de red, puedes estructurar cadenas avanzadas (cadenas de ejecución o agentes) interactuando directamente mediante las abstracciones de LangChain Comunidad.

```python
from langchain_community.llms import Ollama
import pandas as pd

# Inicializar el modelo a través de LangChain
llm = Ollama(
    base_url="http://127.0.0.1:11434",
    model="llama3.2"
)

# Datos estructurados
df = pd.DataFrame([{"Cliente": "Ana", "Gasto": 350}, {"Cliente": "Luis", "Gasto": 1200}])

# Consulta combinada
contexto = f"Datos actuales de clientes:\n{df.to_string()}"
pregunta = f"{contexto}\n\nPregunta: ¿Qué cliente requiere atención prioritaria por mayor volumen de cuenta?"

respuesta = llm.invoke(pregunta)
print(respuesta)
```

---

## 📊 Modelos Disponibles de Ollama

Puedes verificar el estado y los nombres exactos de tus modelos locales ejecutando en tu terminal del sistema:
```bash
ollama list
```
* Asegúrate de invocar exactamente `llama3.2` o `nomic-embed-text` en las configuraciones de tus scripts de Python.
