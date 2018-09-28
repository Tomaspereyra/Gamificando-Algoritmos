class Juego:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setId(self, idJuego):
        self.idJuego = idJuego

    def getId(self):
        return self.idJuego

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getDescripcion(self):
        return self.descripcion

    def __str__(self):
        return str("Id juego: " + str(self.getId()) + " Nombre: " + self.getNombre() + " Descripcion: " +
                   self.getDescripcion())
