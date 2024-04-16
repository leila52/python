# Ejercicio 6: Listar ficheros y carpetas en una ruta
import glob
import os

# Listar todos los ficheros en la ruta "/home/luis/*"
todos = glob.glob("/home/leila_16/*")
print("Ficheros en la ruta:")
for archivo in todos:
    if os.path.isfile(archivo):
        print(archivo)

# Listar todas las carpetas en la ruta "/home/luis/*"
print("\nCarpetas en la ruta:")
for archivo in todos:
    if os.path.isdir(archivo):
        print(archivo)