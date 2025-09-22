def OpenWriter(file, content):
    with open(file, "w+") as f:
        f.write(content)
        f.close()
    return True

def OpenReader(file):
    contents = None
    with open(file, 'r') as f:
        r = f.readlines()
        f.close()
    return r
