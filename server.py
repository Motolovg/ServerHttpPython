from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler

ip = "127.0.0.1"
porta = 8000

class Http(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Me arruma um estágio professor</h1></body></html>"))


server = HTTPServer((ip, porta), Http)
print("servidor rodando...")

server.serve_forever()
server.server_close()
print("Server parado")