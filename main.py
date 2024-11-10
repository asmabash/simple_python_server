from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "192.168.1.171"
PORT = 9999

class MyHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1 style=\"color:blue;\">Hello World</h1></body></html>", "utf-8"))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        self.wfile.write(bytes(f'{{"time": "{date}"}}', "utf-8"))
    

server = HTTPServer((HOST, PORT), MyHandler)
print(f"Server started at {HOST}:{PORT}")
server.serve_forever()
server.server_close()
print(f"Server stopped...")
