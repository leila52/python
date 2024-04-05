from nodo import Nodo


class Pila:
    #constructor
    def __init__(self):
        self.cima= None
    
    def apilar(self,objeto):
        #creamos el nuevo nodo
        nuevo = Nodo(objeto,self.cima)
        self.cima=nuevo

    def vacia(self):
        return self.cima == None


    def desapilar(self):
        #comprobamos si esta vacia
        if self.vacia():
            print("error404")
        else:
            aux =self.cima.info
            #enlazamos cima con el nodo anterior
            self.cima=self.cima.enlace
            return aux