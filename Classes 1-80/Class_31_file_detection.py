import os

path = "C:\\Users\\migue\\Desktop\\Novo Documento de Texto (2).txt"

if os.path.exists(path):
    print("This location Exists!")
    if os .path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("This location Doesn't exists")
    os.mkdir(path)