from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_rpc():
    try:
        data = request.get_json()
        method = data.get("method")
        params = data.get("params", {})
        request_id = data.get("id", None)

        if method == "read_file":
            path = params.get("path")
            if not path or not os.path.isfile(path):
                raise FileNotFoundError(f"File not found: {path}")
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            return jsonify({
                "jsonrpc": "2.0",
                "id": request_id,
                "result": content
            })

        elif method == "write_file":
            path = params.get("path")
            content = params.get("content")
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return jsonify({
                "jsonrpc": "2.0",
                "id": request_id,
                "result": "OK"
            })

        else:
            return jsonify({
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {"code": -32601, "message": "Method not found"}
            })

    except Exception as e:
        return jsonify({
            "jsonrpc": "2.0",
            "id": data.get("id", None),
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    app.run(port=5001)