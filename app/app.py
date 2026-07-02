from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "CloudHealth API",
        "status": "running",
        "hostname": socket.gethostname(),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "Application is running successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)