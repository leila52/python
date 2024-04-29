class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.telefono == otro.telefono and self.email == otro.email
