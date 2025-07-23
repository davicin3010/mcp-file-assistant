from mcp_client import MCPFilesystemClient

class FileAgent:
    def __init__(self):
        self.client = MCPFilesystemClient()

    def handle_message(self, message):
        message = message.lower().strip()

        if message.startswith("leer ") or "lee el archivo" in message:
            file_name = self._extract_filename(message)
            if not file_name:
                return "No se pudo identificar el nombre del archivo."
            try:
                content = self.client.read_file(file_name)
                return f"📄 Contenido de '{file_name}':\n\n{content}"
            except Exception as e:
                return f"Error al leer el archivo: {e}"

        elif message.startswith("escribí") or "escribe" in message:
            file_name, content = self._extract_write_command(message)
            if not file_name or content is None:
                return "No se pudo interpretar qué escribir ni en qué archivo."
            try:
                self.client.write_file(file_name, content)
                return f"✅ Archivo '{file_name}' escrito correctamente."
            except Exception as e:
                return f"Error al escribir el archivo: {e}"

        else:
            return "🤖 No entendí tu mensaje. Probá con:\n- 'leer archivo.txt'\n- 'escribí hola en nuevo.txt'"

    def _extract_filename(self, message):
        tokens = message.split()
        for token in tokens:
            if token.endswith(".txt"):
                return token
        return None

    def _extract_write_command(self, message):
        try:
            if "en" not in message:
                return None, None
            parts = message.split("en")
            content = parts[0].replace("escribí", "").replace("escribe", "").strip()
            filename = parts[1].strip()
            return filename, content
        except:
            return None, None