import sys

def leer_contador():
    try:
        with open("contador.txt", "r") as f:
            contenido = f.read()
            return int(contenido)
    except FileNotFoundError:
        return 0

def incrementar_contador():
    contador = leer_contador()
    contador += 1
    with open("contador.txt", "w") as f:
        f.write(str(contador))
    print("Contador incrementado: ", contador)

def decrementar_contador():
    contador = leer_contador()
    contador -= 1
    with open("contador.txt", "w") as f:
        f.write(str(contador))
    print("Contador decrementado: ", contador)

def mostrar_contador():
    contador = leer_contador()
    print("Valor del contador:", contador)

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            incrementar_contador()
        elif sys.argv[1] == "dec":
            decrementar_contador()
        else:
            mostrar_contador()
    else:
        mostrar_contador()
main()