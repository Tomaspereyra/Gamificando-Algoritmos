from datos.Escenario import Escenario
from negocio.EscenarioABM import EscenarioABM

class EscenarioEnProceso:
    def __init__(self, puntajeObtenido=0, solucionBrindada="-", cantidadBloquesUtilizados=0, tiempoSolucion=0, intentos=0, fechaInicio=0, fechaFinalizacion=0):
        self.puntajeObtenido=puntajeObtenido
        self.solucionBrindada=solucionBrindada
        self.cantidadBloquesUtilizados = cantidadBloquesUtilizados
        self.tiempoSolucion = tiempoSolucion
        self.intentos = intentos
        self.fechaInicio = fechaInicio
        self.fechaFinalizacion = fechaFinalizacion

    def finalizado(self):
        return self.puntajeObtenido is not None

    def setId(self, idEscenario):
        self.id = idEscenario

    def getId(self):
        return self.id

    def getEscenario(self):
        abm = EscenarioABM()
        return abm.traerEscenario(self.idEscenario)

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

    def __str__(self):
        return str("id escenario en proceso: "+str(self.getId())+" Solucion: "+self.getSolucionBrindada() + " intentos:  "+ str(self.getIntentos()))