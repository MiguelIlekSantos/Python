import os

source = 'ola'
destination = 'C:\\Users\\Aluno\\Desktop\\ola'

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " Not Found ")

