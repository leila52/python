import sys
import os

class NumeroArgumentosNoValido(Exception):
    pass
class ValoresNoValidos(Exception):
    pass
def verOpcion():
    print(sys.argv)
    try:
        if len(sys.argv) !=2:
            raise NumeroArgumentosNoValido

        if sys.argv[1] == "inc" or sys.argv[1]=="dec":
            if sys.argv[1]=="inc":
                abrirFichero("inc")
            else:
                abrirFichero("dec")
        else:
            raise ValoresNoValidos

    except NumeroArgumentosNoValido:
        print("Numero de argumentos no valido. ")
    except ValoresNoValidos:
        print("Introduzca un 'inc' para incrementar o un 'dec' para restar ")



def abrirFichero(argumento):
    try:
        contenido_str = leer()
        if os.path.exists("contador.txt") :
            contenido = int(contenido_str)
            if argumento == "dec":
                with open("contador.txt", "w+") as archivo:
                    contenido = contenido - 1
                    archivo.write(str(contenido))
                print("Linea dec", leer())
            elif argumento == "inc":
                contenido = contenido + 1
                with open("contador.txt", "w+") as archivo:
                    archivo.write(str(contenido))
                print("Linea inc", leer())

    except FileNotFoundError:
        print("el fichero no existe, se va a crear")
        archivo=open("contador.txt","w+")
        contenido=0
        archivo.write(str(contenido))
        archivo.close()


def leer():
    archivo=open("contador.txt","r")
    data=archivo.read()
    archivo.close()
    return data

def main():
    verOpcion()

main()
