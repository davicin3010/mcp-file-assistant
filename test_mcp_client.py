from mcp_client import MCPFilesystemClient

if __name__ == "__main__":
    client = MCPFilesystemClient()

    # Prueba de lectura
    try:
        content = client.read_file("example.txt")
        print("✅ Contenido del archivo 'example.txt':\n")
        print(content)
    except Exception as e:
        print("Error al leer el archivo:", e)

    # Prueba de escritura (opcional)
    try:
        client.write_file("example_output.txt", "Esto fue escrito desde el cliente MCP.")
        print("\n✅ Archivo 'example_output.txt' escrito correctamente.")
    except Exception as e:
        print("Error al escribir el archivo:", e)
