from cryptography.fernet import Fernet

def GenerateCriptoKey():
    key = Fernet.generate_key()
    return key

def CriptographyContent(content, key):
    cipher_suite = Fernet(key)
    _content = content.encode()
    r = cipher_suite.encrypt(_content)
    return r

def Uncripto(content, key):
    cipher_suite = Fernet(key)
    r = cipher_suite.decrypt(content)
    return r
