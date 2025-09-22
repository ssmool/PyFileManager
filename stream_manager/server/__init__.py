import http.server
import socketserver
import threading
import time
import os

# Server configuration
HOST = "localhost"
PORTADDR = 80  # Use 8080 if permission is denied
FILE_NAME = "file.txt"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == f"/{FILE_NAME}":
            if os.path.exists(FILE_PATH):
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                with open(FILE_PATH, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "File not found.")
        else:
            self.send_error(404, "Not found.")

def run_webserver():
    with socketserver.ThreadingTCPServer((HOST, PORTADDR), CustomHTTPRequestHandler) as httpd:
        print(f"Serving {FILE_NAME} on http://{HOST}:{PORTADDR}/{FILE_NAME}")
        httpd.serve_forever()

def start_server_thread():
    server_thread = threading.Thread(target=run_webserver, daemon=True)
    server_thread.start()
    print("Server thread started.")

def OpenFileServer(address,port,_file):
    print(f"Open File Server: http://{address}:{port}/{_file}")
    global FILE_NAME
    global HOST
    global PORTADDR
    print(f"Open File Server: {_file} exists")
    if os.path.exists(_file):
        print(f"Open File Server: {_file} exists")
        HOST = address
        PORTADDR = port
        FILE_NAME = str(_file)
        print(f"Open File Server[STARTING]: http://{HOST}:{PORTADDR}/{FILE_NAME}")
        start_server_thread()
    try:
        print(f"Open File Server[AWAITNG]: http://{HOST}:{PORTADDR}/{FILE_NAME}")
        while True:
            print(f"Open File Server[WHILE]: http://{HOST}:{PORTADDR}/{FILE_NAME}")
            time.sleep(500)
            pass
    except KeyboardInterrupt:
        print("Server stopped.")

