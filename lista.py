"""
Una lista enlazada simple es una colección de nodos

La lista siempre tendrá la referencia al primer nodo
El final de la lista es cuando no se referencie a ningun otro
Cada nodo tiene dos atributos: 
    -info -> cualquier objeto
    -enlace -> referencia al siguiente nodo
"""
from nodo import *
class Lista_enlazada_simple:
    def __init__(self):
        self.inicio = None


    def insertar_principio(self, objeto):
        #creamos nuevo nodo
        nuevo = Nodo(objeto, self.inicio)
        self.inicio = nuevo


    def vacia(self):
       return self.inicio == None

    def insertar_final(self, objeto):
        #creamos un nuevo nodo
        nuevo = Nodo(objeto, None)
        #Comprobamos si la lista esta vacia
        if self.vacia():
            self.inicio = nuevo
        else:
            #nos situamos en el ultimo nodo
            actual = self.inicio
            while actual.enlace != None:
                actual = actual.enlace
            #enlazamos el ultimo nodo con el nuevo nodo
            actual.enlace = nuevo


    def imprimir_lista(self):
        #referencia para moverme por la lista. Nos situamos en el primer nodo
        actual = self.inicio
        #mientras no sea fin lista imprimimos informacion
        while actual != None:
            print(actual.info)
            actual = actual.enlace


    def eliminar(self,buscado):
        anterior = None
        #nos situamos al principio de la lista
        actual = self.inicio
        encontrado = False
        while actual != None and not encontrado:
            if actual.info == buscado:
                encontrado = True
            else:
                #avanzamos al siguiente nodo
                anterior = actual
                actual = actual.enlace
        #averiguamos si lo ha encontrado
        if encontrado:
            #comprobamos si es el primero
            if anterior == None:
                self.inicio=self.inicio.enlace
            else:
                #enlazamos el nodo anterior con
                #el siguiente
                anterior.enlace = actual.enlace
        return encontrado


    