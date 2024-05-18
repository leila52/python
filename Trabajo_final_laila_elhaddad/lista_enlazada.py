from nodo import Nodo

class ListaEnlazada:
    # inicializa la lista enlazada con el primer nodo como None 
    def __init__(self):
        self.primero = None

    # inserta un nuevo nodo al principio de la lista.
    def insertar_al_principio(self, info):
        nuevo_nodo = Nodo(info)
        nuevo_nodo.enlace = self.primero
        self.primero = nuevo_nodo

    # inserta un nuevo nodo en la lista de manera ordenada (por nombre).
    def insertar_orden(self, contacto):
        nuevo_nodo = Nodo(contacto)
        # Si la lista está vacía o el primer nodo debe ir después del nuevo nodo.
        if self.primero is None or self.primero.info.nombre >= contacto.nombre:
            nuevo_nodo.enlace = self.primero
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.enlace is not None and actual.enlace.info.nombre < contacto.nombre:
                actual = actual.enlace
            nuevo_nodo.enlace = actual.enlace
            actual.enlace = nuevo_nodo

    # elimina el nodo que contiene el nombre especificado.
    def eliminar(self, nombre):
        actual = self.primero
        anterior = None
        # busca el nodo a eliminar.
        while actual is not None and actual.info.nombre != nombre:
            anterior = actual
            actual = actual.enlace
        # Si el nodo a eliminar es el primero.
        if actual is not None:
            if anterior is None:
                self.primero = actual.enlace
            else:
                anterior.enlace = actual.enlace

    # busca y devuelve la información del nodo que contiene el nombre especificado.
    def consultar(self, nombre):
        actual = self.primero
        while actual is not None and actual.info.nombre != nombre:
            actual = actual.enlace
        if actual is None:
            return None
        else:
            return actual.info

    # devuelve true si la lista está vacía, False en caso contrario.
    def esta_vacia(self):
        return self.primero is None

    # imprime la información de todos los nodos en la lista.
    def imprimir(self):
        actual = self.primero
        # recorre la lista e imprime la información de cada nodo.
        while actual is not None:
            print(actual.info)
            actual = actual.enlace
