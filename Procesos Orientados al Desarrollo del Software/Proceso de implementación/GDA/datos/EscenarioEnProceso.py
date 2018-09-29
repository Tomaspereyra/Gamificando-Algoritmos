from datos.Escenario import Escenario


class EscenarioEnProceso:
    def __init__(self, puntajeObtenido, solucionBrindada, cantidadBloquesUtilizados, tiempoSolucion, intentos, fechaInicio, fechaFinalizacion):
        self.puntajeObtenido=puntajeObtenido
        self.solucionBrindada=solucionBrindada
        self.cantidadBloquesUtilizados = cantidadBloquesUtilizados
        self.tiempoSolucion = tiempoSolucion
        self.intentos = intentos
        self.fechaInicio = fechaInicio
        self.fechaFinalizacion = fechaFinalizacion

    def setId(self, idEscenario):
        self.id = idEscenario

    def getId(self):
        return self.id

    def getPuntajeObtenido(self):
        return self.puntajeObtenido

    def setPuntajeObtenido(self, puntaje):
        self.puntajeObtenido = puntaje

    def getSolucionBrindada(self):
        return self.solucionBrindada

    def setSolucionBrindada(self, solucion):
        self.solucionBrindada = solucion

    def getEscenario(self):
        return self.escenario

    def setEscenario(self, escenario):
        self.escenario = escenario

    def setCurso(self, cursoIniciado):
        self.cursoIniciado = cursoIniciado

    def getCurso(self):
        return self.cursoIniciado

    def setCantidadBloquesUtilizados(self, cantidad):
        self.cantidadBloquesUtilizados = cantidad

    def getCantidadBloquesUtilizados(self):
        return self.cantidadBloquesUtilizados

    def setTiempoSolucion(self, tiempo):
        self.tiempoSolucion = tiempo

    def getTiempoSolucion(self):
        return self.tiempoSolucion

    def setIntentos(self, intentos):
        self.intentos = intentos

    def getIntentos(self):
        return self.intentos

    def setFechaInicio(self, fecha):
        self.fechaInicio = fecha

    def getFechaInicio(self):
        return self.fechaInicio

    def setFechaFinalizacion(self, fecha):
        self.fechaFinalizacion = fecha

    def getFechaFinalizacion(self):
        return self.fechaFinalizacion