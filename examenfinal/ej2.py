def generar_cesta():
    cesta = {}
    continuar = "sí"
    while continuar == "sí":
        articulo = input('Introduce un artículo: ')
        precio = float(input('Introduce el precio de ' + articulo + ': '))
        cesta[articulo] = precio
        continuar = input("¿Quieres añadir artículos a la lista (sí/no)? ")
    return cesta


def lista_coste(cesta):
    coste = 0
    print("Lista de la compra")
    for articulo in cesta:
        print(articulo, '\t',cesta[articulo])
        coste += cesta[articulo]
    print('Coste total: ', coste)


def main():
    cesta =generar_cesta()
    lista_coste(cesta)


main()