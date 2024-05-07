import pickle
from pelicula import *

class Catalogo:
    peliculas = []
    # Constructor de clase
    def __init__(self):
        self.cargar()

    def cargar(self):

        try:
            fichero = open("catalogo.datos", "rb")
            self.peliculas = pickle.load(fichero)
        except :
            print("Fichero no se puede cargar")
        finally:
            fichero.close



    def agregar(self, p):
            self.peliculas.append(p)
            self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo está vacío")
            return
        for p in self.peliculas:
            print(p)


    def guardar(self):
         fichero = open("catalogo.datos", "wb")
         pickle.dump(self.peliculas, fichero)
         fichero.close()
         print("fichero actualizado")

