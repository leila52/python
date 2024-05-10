from nodo import *

class ListaEnlazada:

    # constructor
    def __init__(self):
        # inicio apunta al primer nodo de la lista
        self.inicio = None

        # inserta un nodo al principio de la lista
    def insertar_principio(self, info):
        # instanciamos un nuevo nodo
        nuevo = Nodo(info, self.inicio)
        self.inicio = nuevo

    def get_info_ultimo_nodo(self):
        # nos situamos alprincipio de la lista
        actual = self.inicio
        # nos situamos en el último nodo
        while actual.enlace is not None:
            actual = actual.enlace
        return actual.info




