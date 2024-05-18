class Contacto:
     # metodo constructor que inicializa los atributos nombre, telefono y email.
    def __init__(self, nombre, telefono, email):

        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    # metodo  que devuelve una representación en cadena del objeto.
    # sirve para mostrar información del objeto de forma legible.
    def __str__(self):
        return f"nombre: {self.nombre}, teléfono: {self.telefono}, email: {self.email}"

    # metodo que compara dos objetos de la clase Contacto.
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.telefono == otro.telefono and self.email == otro.email
