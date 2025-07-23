import streamlit as st
from agent import FileAgent

st.set_page_config(page_title="MCP File Assistant", page_icon="📂")

st.title("📂 MCP File Assistant")
st.markdown("Conversá con tu asistente de archivos usando lenguaje natural.\n\nEjemplos:")
st.code("leer example.txt", language="markdown")
st.code("escribí Hola en nuevo.txt", language="markdown")

# Inicializar agente
if "agent" not in st.session_state:
    st.session_state.agent = FileAgent()

# Inicializar historial
if "messages" not in st.session_state:
    st.session_state.messages = []

# Entrada del usuario
user_input = st.text_input("Escribí tu mensaje:", "")

if user_input:
    st.session_state.messages.append(("🧑", user_input))
    with st.spinner("Procesando..."):
        response = st.session_state.agent.handle_message(user_input)
    st.session_state.messages.append(("🤖", response))

# Mostrar conversación
for speaker, text in st.session_state.messages:
    if speaker == "🧑":
        st.markdown(f"**Tú:** {text}")
    else:
        st.markdown(f"**Agente:** {text}")
