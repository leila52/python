# Ejercicio 7: Administración de archivos y carpetas
import os

def init():
    print("ADMINISTRACIÓN DE ARCHIVOS Y CARPETAS")
    opcion = input("Teclea una opción: c = crear, e = eliminar: ")
    ruta = input("Indica la ruta (dejar en blanco para usar la actual): ")
    if not ruta:
        ruta = os.getcwd()  # Obtener la ruta actual si no se proporciona ninguna.

    tipo = input("Indica el tipo de archivo (a = archivo, c = carpeta): ")

    if opcion == 'c':
        nombre = input("Nombre de {}: ".format("archivo" if tipo == 'a' else "carpeta"))
        try:
            if tipo == 'a':
                with open(os.path.join(ruta, nombre), "w") as f:
                    print("{} creado con éxito.".format("Archivo" if tipo == 'a' else "Carpeta"))
            elif tipo == 'c':
                os.mkdir(os.path.join(ruta, nombre))
                print("Carpeta {} creada con éxito.".format(nombre))
        except Exception as e:
            print("Error:", e)
    elif opcion == 'e':
        nombre = input("Nombre de {}: ".format("archivo" if tipo == 'a' else "carpeta"))
        try:
            if tipo == 'a':
                os.remove(os.path.join(ruta, nombre))
                print("Archivo {} eliminado con éxito.".format(nombre))
            elif tipo == 'c':
                os.rmdir(os.path.join(ruta, nombre))
                print("Carpeta {} eliminada con éxito.".format(nombre))
        except Exception as e:
            print("Error:", e)
    else:
        print("Opción no válida.")
        init()  # Si la opción no es válida, reiniciar la función.

init()
