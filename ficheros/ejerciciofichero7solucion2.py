#importamos el módulo os
import os

#desarrollamos la funcion init para administar archivos y carpetas
def init():
    print("ADMINISTRACION DE ARCHIVOS Y CARPETAS")
    opcion = input("teclea una opcion  c = crear y e = eliminar:")
    if opcion == "c":
        ruta = input("indica la ruta terminando en /:")
        #si la ruta es la actual
        if ruta == "":
            ruta = os.getcwd()+"/"
        #comprobamos si la ruta existe
        if os.path.isdir(ruta):
            #pedimos el tipo de archivo
            tipo = input("indica el tipo de archivo a = archivo y c = carpeta")
            #si es un archivo normal, pedimos su nombre y lo creamos
            if tipo == "a":
                nom_archivo = input("nombre de archivo:")
                #creamos el archivo
                archivo = open(ruta+nom_archivo, "w")
                archivo.close()
                print("archivo ", nom_archivo," creado con éxito")
            #si es una carpeta pedimos su nombre y la creamos
            elif tipo == "c":
                carpeta = input("nombre de carpeta:")
                os.mkdir(ruta+carpeta)
                print("carpeta ", carpeta, "creada con éxito")
            else:
                #reiniciamos la función
                init()
    elif opcion == "e":
        ruta = input("indica la ruta, sino lo haces, la ruta será la actual:")
        # si la ruta es la actual
        if ruta == "":
            ruta = os.getcwd() + "/"
        nom_fichero = input("nombre del archivo o carpeta a eliminar:")
        #si es un archivo ordinario
        if os.path.isfile(ruta + nom_fichero):
            os.remove(ruta+nom_fichero)
            print("archivo ", nom_fichero, " eliminado con éxito")
        elif os.path.isdir(ruta + nom_fichero):
            os.rmdir((ruta + nom_fichero))
            print("carpeta ", nom_fichero, " eliminado con éxito")
        else:
            # reiniciamos la función
            init()
    else:
        # reiniciamos la función
        init()


init()




