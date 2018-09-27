from Docente import Docente


class Curso:
    def __init__(self, sePuedeSaltear, nombre):
        self.sePuedeSaltear = sePuedeSaltear
        self.nombre = nombre
        self.docente = 0
        self.escenario = []

    def setIdCurso(self, idCurso):
        self.idCurso = idCurso

    def setPuedeSaltear(self, sePuede):
        self.sePuedeSaltear = sePuede

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDocente(self, docente):
        self.docente = docente

    def setListaEscenario(self, escenario):
        self.escenario.append(escenario)

    def getIdCurso(self):
        return self.idCurso

    def getSepuedeSaltar(self):
        return self.sePuedeSaltear

    def getNombre(self):
        return self.nombre

    def getDocente(self):
        return self.docente

    def getEscenario(self):
        return self.escenario

    def __str__(self):
        return str(
            "ID: " + str(self.getIdCurso()) + " Se puede saltear: " + str(self.getSepuedeSaltar()) + " Nombre:  " +
            self.getNombre() + " Docente: " + str(self.getDocente()))
