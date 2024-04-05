from nodo import *

class Cola:
    def __init__(self):
        self.primero=None
        self.ultimo=None


    def vacia(self):
        return self.primero==None
    


    def encolar(self):
        
        #crear un nuevo nodo
        nuevo= Nodo(object,None)

        #comprobar si esta vacia
        if self.vacia():
            self.primero=nuevo
            self.ultimo=nuevo
        else :
            #enlazamos el ultimo nodocon el nuevo
            self.ultimo.enlace=nuevo
            
        self.ultimo=nuevo
    
    def desencolar(self):
        if self.vacia():
            print("error la cola esta vaciaaaaa")
            return None
        else:
            aux=self.primero.info
            #enlazamos primero con el nodo sigfuiente
            