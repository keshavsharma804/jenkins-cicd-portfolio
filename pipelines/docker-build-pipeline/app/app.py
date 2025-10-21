from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'app': 'MyDockerApp',
        'version': os.getenv('APP_VERSION', 'unknown'),
        'environment': os.getenv('ENVIRONMENT', 'unknown'),
        'hostname': socket.gethostname(),
        'message': 'Hello from Jenkins + Docker CI/CD!'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
