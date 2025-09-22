def OpenBinaryWriter(file, content):
    with open(file, 'wb') as f:
        if(type(content) == bytes):
            f.write(content)
            f.close()
            return True
    return False

def OpenBinaryReader(file):
    with open(file, mode='rb') as f:
        fileContent = f.read()
        f.close()
    return fileContent

def GetBinaryStart(fileContent):
    r = struct.unpack("i" * ((len(fileContent) -24) // 4), fileContent[20:-4])
    return r

def GetBinaryEnd(fileContent):
    r = struct.unpack("i", fileContent[-4:])
    return r
