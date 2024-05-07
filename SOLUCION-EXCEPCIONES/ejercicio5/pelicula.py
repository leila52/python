class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion,año_estreno):
        self.titulo = titulo
        self.duracion = duracion
        self.año_estreno = año_estreno

    def __str__(self):
        return (self.titulo + " " + str(self.duracion) + " " + str(self.año_estreno))