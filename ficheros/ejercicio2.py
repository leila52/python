#abrimos el fichero creado
archivo=open("ejercicio.txt","r+")
print(archivo.read())
#obtenemos los datos del fichero
#no cambiar ruta del txt
print(archivo.name)
print(archivo.mode)
print(archivo.encoding)
#lo cerramos
archivo.close()