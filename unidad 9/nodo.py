class Nodo:
    def __init__(self, info, enlace):
        self.info = info
        self.enlace = enlace

class Lista_enlazada_simple:
    def __init__(self):
        self.inicio = None

    def insertar_principio(self, objeto):
        # Creamos nuevo nodo
        nuevo = Nodo(objeto, self.inicio)
        self.inicio = nuevo

    def vacia(self):
        return self.inicio == None

    def insertar_final(self, objeto):
        # Creamos un nuevo nodo
        nuevo = Nodo(objeto, None)
        # Comprobamos si la lista está vacía
        if self.vacia():
            self.inicio = nuevo
        else:
            # Nos situamos en el último nodo
            actual = self.inicio
            while actual.enlace != None:
                actual = actual.enlace
            # Enlazamos el último nodo con el nuevo nodo
            actual.enlace = nuevo

    def imprimir_lista(self):
        # Referencia para moverme por la lista. Nos situamos en el primer nodo
        actual = self.inicio
        # Mientras no sea fin lista imprimimos información
        while actual != None:
            print(actual.info)
            actual = actual.enlace

    def eliminar(self, buscado):
        anterior = None
        # Nos situamos al principio de la lista
        actual = self.inicio
        encontrado = False
        while actual != None and not encontrado:
            if actual.info == buscado:
                encontrado = True
            else:
                # Avanzamos al siguiente nodo
                anterior = actual
                actual = actual.enlace
        # Averiguamos si lo ha encontrado
        if encontrado:
            # Comprobamos si es el primero
            if anterior == None:
                self.inicio = self.inicio.enlace
            else:
                # Enlazamos el nodo anterior con
                # el siguiente
                anterior.enlace = actual.enlace
        return encontrado
    

    def buscar(self, buscado):
        actual = self.inicio
        encontrado = False
        while actual != None and not encontrado:
            if actual.info == buscado:
                encontrado = True
            else:
                actual = actual.enlace
        return encontrado

    def contar_elementos(self):
        contador = 0
        actual = self.inicio
        while actual != None:
            contador += 1
            actual = actual.enlace
        return contador

# Creación de la lista enlazada y operaciones sobre ella
lista = Lista_enlazada_simple()
lista.insertar_principio("hola")
lista.insertar_principio("que")
lista.insertar_principio("pasa")

lista.insertar_final("hola")
lista.insertar_final("que")
lista.insertar_final("pasa")


lista.insertar_final("todo")
lista.insertar_final("bien")

# Imprimir lista
print("Elementos de la lista:")
lista.imprimir_lista()

# Eliminar un elemento
elemento_a_eliminar = "que"
if lista.eliminar(elemento_a_eliminar):
    print(f"Se eliminó el elemento '{elemento_a_eliminar}' de la lista.")

# Buscar un elemento
elemento_a_buscar = "bien"
if lista.buscar(elemento_a_buscar):
    print(f"El elemento '{elemento_a_buscar}' está en la lista.")
else:
    print(f"El elemento '{elemento_a_buscar}' no está en la lista.")

# Contar elementos
cantidad_elementos = lista.contar_elementos()
print(f"La lista tiene {cantidad_elementos} elementos.")
