from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from Flask on Vercel!',
        'status': 'working',
        'vercel': os.getenv('VERCEL', 'false')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run()

from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            "message": "Hello from Vercel serverless function!",
            "status": "working",
            "vercel": os.getenv("VERCEL", "false"),
            "path": self.path
        }
        
        self.wfile.write(json.dumps(response).encode())
        return
    
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                post_data = self.rfile.read(content_length)
                try:
                    data = json.loads(post_data)
                except json.JSONDecodeError:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    error_response = {
                        "error": "Invalid JSON",
                        "message": "Invalid JSON in request body"
                    }
                    self.wfile.write(json.dumps(error_response).encode())
                    return
            else:
                data = {}
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "message": "Received POST request",
                "status": "working",
                "vercel": os.getenv("VERCEL", "false"),
                "path": self.path,
                "data": data
            }
            
            self.wfile.write(json.dumps(response).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            error_response = {
                "error": "Internal Server Error",
                "message": str(e)
            }
            self.wfile.write(json.dumps(error_response).encode())
