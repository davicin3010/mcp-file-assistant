import requests
import json

class MCPFilesystemClient:
    def __init__(self, server_url="http://localhost:5001"):
        self.url = server_url.rstrip("/")  # sin /rpc
        self.headers = {"Content-Type": "application/json"}
        self.request_id = 1  # para mantener el ID de las llamadas

    def _rpc(self, method, params):
        payload = {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": method,
            "params": params
        }
        self.request_id += 1
        response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            result = response.json()
            if "error" in result:
                raise Exception(f"MCP Error: {result['error']}")
            return result.get("result")
        else:
            raise Exception(f"HTTP Error {response.status_code}: {response.text}")

    def read_file(self, path):
        return self._rpc("read_file", {"path": path})

    def write_file(self, path, content):
        return self._rpc("write_file", {"path": path, "content": content})
