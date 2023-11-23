import struct
import base64
import socketserver
from cryptography.fernet import Fernet

fileContent = "false";

def OpenWriter(file, content):
    f = open(file, "a")
    f.write(content)
    f.close()
    return true

def OpenReader(file):
    contents = None

    with open(file, 'r') as fp:
        r = fp.readlines()
    return r

def OpenBinaryWriter(file, content):
    with open(file, 'br+') as f:
        f.write(bytes(content))

def OpenBinaryReader(file):
    with open(file, mode='rb') as file: # b is important -> binary
        fileContent = file.read()
    return fileContent

def GetBinaryStart(fileContent):
    r = struct.unpack("i" * ((len(fileContent) -24) // 4), fileContent[20:-4])
    return r

def GetBinaryEnd(fileContent):
    r = struct.unpack("i", fileContent[-4:])
    return r

def OpenBase64Reader(file):
    content = open(file, 'rb')
    reader = content.read()
    r = base64.encodebytes(reader)
    return r

def OpenBase64Writer(file, content):
    content = open(file, 'rb')
    reader = content.read()
    r = base64.encodebytes(reader)
    OpenWriter(file, r)
    return true

def GenerateCriptoKey():
    key = Fernet.generate_key() #this is your "password"
    return key

def CriptographyContent(content, key):
    cipher_suite = Fernet(key)
    r = cipher_suite.encrypt(b"Hello stackoverflow!")
    return r

def Uncripto(content, key):
    cipher_suite = Fernet(key)
    r = cipher_suite.decrypt(content)
    return r

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
        with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
            server.serve_forever()
    return true