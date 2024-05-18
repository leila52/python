from contacto import *
from lista_enlazada import *
import pickle

# Solicita al usuario que introduzca los datos de un contacto
def intro_datos_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce el teléfono del contacto: ")
    email = input("Introduce el email del contacto: ")
    return Contacto(nombre, telefono, email)

# Añade un nuevo contacto a la lista enlazada
def anadir(lista):
    contacto = intro_datos_contacto()
    lista.insertar_orden(contacto)

# Elimina un contacto de la lista enlazada
def eliminar(lista):
    if lista.esta_vacia():
        print("La agenda está vacía.")
    else:
        nombre = input("Introduce el nombre del contacto que deseas eliminar: ")
        lista.eliminar(nombre)

# Consulta un contacto en la lista enlazada y muestra su información
def consultar(lista):
    if lista.esta_vacia():
        print("La agenda está vacía.")
    else:
        # busca el contacto por nombre
        nombre = input("Introduce el nombre del contacto que deseas consultar: ")
        contacto = lista.consultar(nombre)
        if contacto is None:
            print("El contacto no existe en la agenda.")
        else:
            # muestra la información del contacto encontrado
            print(contacto)

# Lista todos los contactos en la agenda
def listado(lista):
    if lista.esta_vacia():
        print("La agenda está vacía.")
    else:
        lista.imprimir()

 # Edita la información de un contacto existente
def editar(lista):
    if lista.esta_vacia():
        print("La agenda está vacía.")
    else:
        nombre = input("introduce el nombre del contacto que deseas editar: ")
        contacto = lista.consultar(nombre)
        if contacto is None:
            print("El contacto no existe en la agenda.")
        else:
            print("Datos actuales del contacto:")
            print(contacto)
            nuevo_nombre = input("Introduce el nuevo nombre del contacto (deja en blanco para mantener el mismo): ")
            nuevo_telefono = input("Introduce el nuevo teléfono del contacto (deja en blanco para mantener el mismo): ")
            nuevo_email = input("Introduce el nuevo email del contacto (deja en blanco para mantener el mismo): ")
            #si no introduce nada no se cambia
            if nuevo_nombre != "":
                contacto.nombre = nuevo_nombre
            if nuevo_telefono != "":
                contacto.telefono = nuevo_telefono
            if nuevo_email != "":
                contacto.email = nuevo_email

def menu(lista):
    print("agenda de contactos de leila")
    print("Elige una opción del siguiente menú de contactos:")
    print("1. Añadir un nuevo contacto")
    print("2. Eliminar un contacto")
    print("3. Consultar un contacto")
    print("4. Editar un contacto")
    print("5. Listar la agenda")
    print("6. Salir")

    opcion = input("Introduce una opcción: ")

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
    arrancar_aplicacion()
