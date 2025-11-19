import http.server
import socketserver
import os

PORT = 3000

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(__file__), **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Frontend сервер запущено на http://localhost:{PORT}")
    print("📁 Обслуговує файли з поточної теки")
    httpd.serve_forever()