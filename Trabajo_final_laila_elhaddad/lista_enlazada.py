from nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def insertar_al_principio(self, info):
        nuevo_nodo = Nodo(info)
        nuevo_nodo.enlace = self.primero
        self.primero = nuevo_nodo

    def insertar_orden(self, contacto):
        nuevo_nodo = Nodo(contacto)
        if self.primero is None or self.primero.info.nombre >= contacto.nombre:
            nuevo_nodo.enlace = self.primero
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.enlace is not None and actual.enlace.info.nombre < contacto.nombre:
                actual = actual.enlace
            nuevo_nodo.enlace = actual.enlace
            actual.enlace = nuevo_nodo

    def eliminar(self, nombre):
        actual = self.primero
        anterior = None
        while actual is not None and actual.info.nombre != nombre:
            anterior = actual
            actual = actual.enlace
        if actual is not None:
            if anterior is None:
                self.primero = actual.enlace
            else:
                anterior.enlace = actual.enlace

    def consultar(self, nombre):
        actual = self.primero
        while actual is not None and actual.info.nombre != nombre:
            actual = actual.enlace
        if actual is None:
            return None
        else:
            return actual.info

    def esta_vacia(self):
        return self.primero is None

    def imprimir(self):
        actual = self.primero
        while actual is not None:
            print(actual.info)
            actual = actual.enlace
