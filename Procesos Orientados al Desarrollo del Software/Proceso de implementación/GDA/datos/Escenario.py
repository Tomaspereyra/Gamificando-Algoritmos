from datos.Curso import Curso


class Escenario:

    def __init__(self, bloquesPermitidos=0, cantBloquesMax=0, hint="-", posibleSolucion="-", descripcion="-"):
        self.bloquesPerimitidos = bloquesPermitidos
        self.cantBloquesMax = cantBloquesMax
        self.hint = hint
        self.posiblesSolucion = posibleSolucion
        self.descripcion = descripcion
        self.idEscenario = -1
        self.idCurso = -1

    def setIdCurso(self, idCurso):
        self.idCurso = idCurso

    def setIdEscenario(self, idEscenario):
        self.idEscenario=idEscenario

    def setBloquesPermitidos(self, bloques):
        self.bloquesPerimitidos = bloques

    def setCantBloquesMax(self, bloquesMax):
        self.bloquesMax= bloquesMax

    def setHint(self, hint):
        self.hint = hint

    def setPosiblesSolucion(self, posibleSolucion):
        self.posiblesSolucion = posibleSolucion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getBloquesPerimitidos(self):
        return self.bloquesPerimitidos

    def getCantBloquesMax(self):
        return self.cantBloquesMax

    def getHint(self):
        return self.hint

    def getPosiblesSolucion(self):
        return self.posiblesSolucion

    def getDescripcion(self):
        return self.descripcion

    def getIdEscenario(self):
        return self.idEscenario

    def __str__(self):
        return str("Datos Escenario:" + str(self.getBloquesPerimitidos()) + str(self.getCantBloquesMax()) +
                   self.getHint() + self.getPosiblesSolucion() + self.getDescripcion())

