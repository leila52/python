from lista import Lista_enlazada_simple

lista= Lista_enlazada_simple()
lista.insertar_principio("hola")
lista.insertar_principio("que")
lista.insertar_principio("pasa")

# Insertar al final
lista.insertar_final("todo")
lista.insertar_final("bien")

# Imprimir lista
print("Elementos de la lista:")
lista.imprimir_lista()

# Eliminar un elemento
elemento_a_eliminar = "que"
if lista.eliminar(elemento_a_eliminar):
    print(f"Se eliminó el elemento '{elemento_a_eliminar}' de la lista.")
