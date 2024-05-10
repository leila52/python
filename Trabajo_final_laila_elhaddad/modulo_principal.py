from contacto import *
from lista_enlazada import *

def intro_datos_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce el teléfono del contacto: ")
    email = input("Introduce el email del contacto: ")
    return Contacto(nombre, telefono, email)

def anadir(lista):
    contacto = intro_datos_contacto()
    lista.insertar_orden(contacto)

def eliminar(lista):
    if lista.esta_vacia():
        print("La agenda está vacía.")
    else:
        nombre = input("Introduce el nombre del contacto que deseas eliminar: ")
        lista.eliminar(nombre)

def consultar(lista):
    if lista.esta_vacia():
        print("La agenda está vacía.")
    else:
        nombre = input("Introduce el nombre del contacto que deseas consultar: ")
        contacto = lista.consultar(nombre)
        if contacto is None:
            print("El contacto no existe en la agenda.")
        else:
            print(contacto)

def listado(lista):
    if lista.esta_vacia():
        print("La agenda está vacía.")
    else:
        lista.imprimir()

def editar(lista):
    if lista.esta_vacia():
        print("La agenda está vacía.")
    else:
        nombre = input("Introduce el nombre del contacto que deseas editar: ")
        contacto = lista.consultar(nombre)
        if contacto is None:
            print("El contacto no existe en la agenda.")
        else:
            print("Datos actuales del contacto:")
            print(contacto)
            nuevo_nombre = input("Introduce el nuevo nombre del contacto (deja en blanco para mantener el mismo): ")
            nuevo_telefono = input("Introduce el nuevo teléfono del contacto (deja en blanco para mantener el mismo): ")
            nuevo_email = input("Introduce el nuevo email del contacto (deja en blanco para mantener el mismo): ")
            if nuevo_nombre != "":
                contacto.nombre = nuevo_nombre
            if nuevo_telefono != "":
                contacto.telefono = nuevo_telefono
            if nuevo_email != "":
                contacto.email = nuevo_email

def menu(lista):
    print("AGENDA DE CONTACTOS")
    print("Elige una opción (1, 2, 3, 4, 5 o 6) del siguiente menú de contactos:")
    print("1. Añadir un nuevo contacto")
    print("2. Eliminar un contacto")
    print("3. Consultar un contacto")
    print("4. Editar un contacto")
    print("5. Listar la agenda")
    print("6. Salir")

    opcion = input("Introduce la opción y pulsa enter: ")

    if opcion == "1":
        anadir(lista)
    elif opcion == "2":
        eliminar(lista)
    elif opcion == "3":
        consultar(lista)
    elif opcion == "4":
        editar(lista)
    elif opcion == "5":
        listado(lista)
    elif opcion == "6":
        print("Ha salido de la aplicación.")
        exit()
    else:
        print("Opción no válida.")

def arrancar_aplicacion():
    lista_contactos = ListaEnlazada()
    try:
        with open("agenda.datos", "rb") as archivo:
            lista_contactos = pickle.load(archivo)
    except FileNotFoundError:
        print("El fichero agenda.datos todavía no existe. Se creará al salir de la aplicación.")

    while True:
        menu(lista_contactos)
        try:
            with open("agenda.datos", "wb") as archivo:
                pickle.dump(lista_contactos, archivo)
        except Exception as e:
            print(f"Ha ocurrido un error al guardar los datos de la agenda: {e}")

if __name__ == "__main__":
    import pickle
    arrancar_aplicacion()
