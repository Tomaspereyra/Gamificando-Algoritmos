from Docente import Docente


class Curso:
    def __init__(self, sePuedeSaltear=False, nombre="-", juego="-", descripcion="-"):
        self.sePuedeSaltear = sePuedeSaltear
        self.nombre = nombre
        self.escenario = []
        self.juego = juego
        self.descripcion = descripcion
        self.idCurso = -1

    def setIdCurso(self, idCurso):
        self.idCurso = idCurso

    def setPuedeSaltear(self, sePuede):
        self.sePuedeSaltear = sePuede

    def setNombre(self, nombre):
        self.nombre = nombre

    def setListaEscenario(self, escenarios):
        self.escenario = []
        self.escenario.extend(escenarios)

    def getIdCurso(self):
        return self.idCurso

    def getSepuedeSaltar(self):
        return self.sePuedeSaltear

    def getNombre(self):
        return self.nombre

    def getEscenario(self):
        return self.escenario

    def setJuego(self, juego):
        self.juego = juego

    def getJuego(self):
        return self.juego

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getDescripcion(self):
        return self.descripcion

    def __str__(self):
        return str(
            "ID: " + str(self.getIdCurso()) + " Se puede saltear: " + str(self.getSepuedeSaltar()) + " Nombre:  " +
            self.getNombre() + " Juego: "+str(self.getJuego().__str__()))

