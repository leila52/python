from pila import Pila

def main():
    abecedario="abcdefghijklmnñopqlrstuvwxyz"
    pila = Pila()
    for letra in abecedario:
        pila.apilar(letra)

    #vaciamos toda la pila y enviamos la pantalla
    while not pila.vacia():
        print(pila.desapilar(),end="")