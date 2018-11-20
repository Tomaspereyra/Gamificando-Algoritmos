from dao.EscenarioEnProcesoDao import EscenarioEnProcesoDao
from datos.Escenario import Escenario


class EscenarioEnProcesoABM:

    def __init__(self):
        self.dao = EscenarioEnProcesoDao()

    def traerEscenario(self,idEscenario):
        return self.dao.traerEscenario(idEscenario)

    def comenzarEscenario(self, fechaInicio, idEscenario, idCursoIniciado):
        return self.dao.comenzarEscenario(fechaInicio, idEscenario, idCursoIniciado)

    def terminarEscenario(self, escenarioEnProceso):
        return self.dao.terminarEscenario(escenarioEnProceso)


#escenarioabm = EscenarioEnProcesoABM()




#escenario = escenarioabm.traerEscenario(3)
#escenario.setPuntajeObtenido(15)
#escenario.setSolucionBrindada("una")
#escenario.setFechaFinalizacion("2018/10/30")
#escenario.setCantidadBloquesUtilizados(10)
#escenario.setTiempoSolucion(10)
#escenario.setIntentos(2)
#escenarioabm.terminarEscenario(escenario)
