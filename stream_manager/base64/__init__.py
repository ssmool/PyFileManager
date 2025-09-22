import base64
import stream_manager.binary as BINARY

def OpenBase64Writer(file, content):
    if(type(content) != bytes):
        _b = content.encode('ascii')
        _b64 = base64.encodebytes(_b)
    if(type(content) == bytes):
        _b64 = base64.encodebytes(content)
    r = BINARY.OpenBinaryWriter(file, _b64)
    return r

def OpenBase64Reader(file):
    f = BINARY.OpenBinaryReader(file)
    r = base64.decodebytes(f)
    return r
