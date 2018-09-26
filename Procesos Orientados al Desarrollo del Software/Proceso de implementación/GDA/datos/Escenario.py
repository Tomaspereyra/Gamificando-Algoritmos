from Curso import Curso


class Escenario:

    def __init__(self, bloquesPermitidos, cantBloquesMax, hint, posibleSolucion, descripcion):
        self.bloquesPerimitidos = bloquesPermitidos
        self.cantBloquesMax = cantBloquesMax
        self.hint = hint
        self.posiblesSolucion = posibleSolucion
        self.descripcion = descripcion
        self.curso = Curso


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

    def setCurso(self, curso):
        self.curso=curso

    def getCurso(self):
        return self.curso

    def __str__(self):
        print "Datos Escenario:", self.getBloquesPerimitidos(), self.getCantBloquesMax(), self.getHint(), self.getPosiblesSolucion(), self.getDescripcion()

cursoNuevo = Curso(False, "nombre")
escenarioo = Escenario('5', '3', "HINT", "Una buena solucion", "Juego facil")
cursoNuevo.setListaEscenario(escenarioo)
escenarioo.setCurso(cursoNuevo)