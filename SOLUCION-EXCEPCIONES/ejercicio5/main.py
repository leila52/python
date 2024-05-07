from catalogo import *

def main():
    catalogo = Catalogo()
    catalogo.mostrar()
    catalogo.agregar(Pelicula("Caftán azul", 122,2023))
    catalogo.agregar(Pelicula("Sin novedad en el frente", 140,2022))
    catalogo.mostrar()

main()
