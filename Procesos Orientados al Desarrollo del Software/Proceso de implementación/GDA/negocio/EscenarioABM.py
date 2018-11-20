from dao.EscenarioDao import EscenarioDao


class EscenarioABM:

    def __init__(self):
        self.dao = EscenarioDao()

    def traerEscenario(self, idEscenario):
        return self.dao.traerEscenario(idEscenario)

    def actualizarEscenario(self, escenario):
        return self.dao.actualizarEscenario(escenario)

    def agregarEscenario(self, bloquesPermitidos, cantBloquesMax, hint, posibleSolucion, descripcion, idCurso):

        return self.dao.agregar(bloquesPermitidos, cantBloquesMax, hint, posibleSolucion, descripcion, idCurso)

    def traerEscenariosPorCursos(self, idCurso):
        return self.dao.traerEscenariosPorCurso(idCurso)
