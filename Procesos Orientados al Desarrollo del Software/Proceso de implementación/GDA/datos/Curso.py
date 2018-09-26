from Docente import Docente



class Curso:
    def __init__(self, sePuedeSaltear, nombre):
        self.sePuedeSaltear = sePuedeSaltear
        self.nombre = nombre
        self.docente = Docente
        self.escenario = []

    def setIdCurso(self, idCurso):
        self.idCurso = idCurso

    def sePuedeSaltear(self, sePuede):
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
        print "Datos del Curso:", self.getIdCurso(), self.getSepuedeSaltar(), self.getNombre(), self.getDocente()
        for escenario in self.getEscenario():
            print escenario.__str__()
