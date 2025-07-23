# 📂 MCP File Assistant (Option A)

Implementación de la opción **A: File Assistant** del challenge técnico. Este agente puede leer y analizar archivos locales, responder preguntas simples sobre su contenido y realizar operaciones básicas de archivo utilizando el protocolo **Model Context Protocol (MCP)** simulado localmente.

---

## 🚀 Características principales

- ✅ **Lectura de archivos locales** mediante el protocolo MCP
- ✅ **Análisis básico** del contenido (visualización por chat)
- ✅ **Operaciones simples**: lectura, escritura
- ✅ **Interfaz de conversación** en Streamlit
- ✅ 100% autocontenible, sin necesidad de Docker ni servicios externos

---

## 📁 Estructura del proyecto

```
mcp-file-assistant/
├── agent.py              # Lógica del agente de conversación
├── interface.py          # Interfaz Streamlit
├── mcp_client.py         # Cliente MCP Filesystem (JSON-RPC)
├── server.py             # Servidor MCP simulado (Flask)
├── test_mcp_client.py    # Test manual del cliente
├── example.txt           # Archivo de ejemplo para pruebas
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
```

---

## 🧑‍💻 Requisitos

- Python 3.9+ (funciona con Anaconda o venv)
- Flask
- Streamlit
- Requests

Instalación recomendada:

```bash
pip install -r requirements.txt
```

---

## ▶️ Cómo correr el proyecto

### 1. Iniciar el servidor MCP simulado

```bash
python server.py
```

Este servidor acepta llamadas JSON-RPC 2.0 y permite leer y escribir archivos locales desde el cliente.

### 2. Probar el cliente MCP

```bash
python test_mcp_client.py
```

Verifica que el agente pueda leer y escribir archivos correctamente.

### 3. Ejecutar la interfaz conversacional

```bash
streamlit run interface.py
```

Se abrirá una app web donde podés interactuar con el agente.

---

## 💬 Ejemplos de uso

Desde la interfaz de chat:

- `leer example.txt`
- `escribí hola mundo en nuevo.txt`
- `leer nuevo.txt`

---

## 📌 Notas técnicas

- El servidor MCP está simulado con Flask y responde a llamadas JSON-RPC en `/`
- El cliente implementa el protocolo como si se conectara a un servidor MCP real
- La lógica del agente puede escalarse fácilmente con LLMs si se desea

---

## 🧠 Autor y propósito

Este proyecto fue desarrollado por **David Pedemonte** como parte del bonus challenge técnico, implementando la opción **A: File Assistant** con foco en agentes inteligentes, integración MCP, y uso de herramientas modernas como Streamlit.