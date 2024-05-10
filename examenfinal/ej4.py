from ej3 import *
import pickle
import os.path

def guardar(lista):
    try:
        fichero = open("lista.datos", "wb", )
        pickle.dump(lista, fichero)
        fichero.close()
    except:
        print("No se ha podido guardar la lista en el fichero")


def cargar():
    try:
        fichero = open("lista.datos", "rb")
        return pickle.load(fichero)
    except:
        print("no se ha podido cargar la lista")



def main():
    if os.path.exists("lista.datos"):
        lista = cargar()
        lista.ver_lista()
    else:
        lista = ListaEnlazada()
        lista.insertar_principio("Javier")
        lista.insertar_principio("Nuria")
        lista.insertar_principio("Graciela")
        print(lista.get_info_ultimo_nodo())
    guardar(lista)

main()