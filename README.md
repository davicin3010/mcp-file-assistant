# 📂 MCP File Assistant

Un agente inteligente simple que interactúa con archivos locales a través de un servidor MCP simulado. Permite leer y escribir archivos mediante lenguaje natural desde una interfaz de chat basada en Streamlit.

> ⚙️ Desarrollado como parte de un challenge técnico con integración al protocolo **Model Context Protocol (MCP)**.

---

## 🚀 Características

- 🧠 Agente que interpreta mensajes como “leer archivo.txt” o “escribí hola en nuevo.txt”
- 📡 Cliente MCP compatible con JSON-RPC 2.0
- 💾 Servidor MCP Filesystem simulado con Flask (local)
- 💬 Interfaz conversacional en Streamlit
- ✅ Proyecto autocontenible, sin dependencias externas (como Claude Desktop o Docker)

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

### 1. Ejecutar el servidor MCP local

```bash
python server.py
```

Este comando inicia un servidor JSON-RPC en `http://localhost:5001` que puede leer y escribir archivos locales.

### 2. Probar el cliente directamente (opcional)

```bash
python test_mcp_client.py
```

Verifica que el servidor puede leer y escribir archivos correctamente.

### 3. Ejecutar la interfaz conversacional

```bash
streamlit run interface.py
```

Se abrirá una app en tu navegador en `http://localhost:8501`.

---

## 💬 Ejemplos de uso

En la interfaz Streamlit, probá ingresar:

- `leer example.txt`
- `escribí hola mundo en nuevo.txt`
- `leer nuevo.txt`

---

## 📌 Notas técnicas

- El servidor MCP es una simulación local basada en Flask, compatible con JSON-RPC 2.0.
- Podés reemplazar `server.py` por un servidor MCP real como [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) si lo deseás.
- La lógica del agente es simple, pero puede integrarse fácilmente con LLMs como Gemini o GPT.

---

## 🧠 Autor y propósito

Este proyecto fue desarrollado por **David Pedemonte** como parte de un bonus challenge técnico para demostrar habilidades con agentes, protocolos MCP y herramientas modernas de AI.
