import socketserver

def OpenFileServer(host, port, file):
    class MyTCPHandler(socketserver.BaseRequestHandler):
        def handle(self):
            self.data = self.request.recv(1024).strip()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            content = OpenReader(file)
            self.request.sendall(content)
    if __name__ == "__main__":
        HOST, PORT = host, port
        with socketserver.TCPServer((HOST,PORT), MyTCPHandler) as server:
            server.serve_forever()
    return True
