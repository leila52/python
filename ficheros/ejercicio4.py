from io import open

with open("archivo.txt","r") as archivo:
    print(archivo.read())
    print(archivo.name)
    print(archivo.mode)
    print(archivo.encoding)