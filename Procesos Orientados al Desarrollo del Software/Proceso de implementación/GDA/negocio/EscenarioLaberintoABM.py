from dao.EscenarioLaberintoDao import EscenarioLaberintoDao
from negocio.EscenarioABM import EscenarioABM
from datos.EscenarioLaberinto import EscenarioLaberinto
class EscenarioLaberintoABM:

    def __init__(self):
        self.dao = EscenarioLaberintoDao()

    def traerEscenario(self, idEscenario):
        return self.dao.traerEscenario(idEscenario)

    def agregarEscenarioLaberinto(self, bloquesPermitidos, cantBloquesMax, hint, posibleSolucion, descripcion, idCurso, mapa):
        escenarioABM = EscenarioABM()
        escenarioABM.agregarEscenario(bloquesPermitidos, cantBloquesMax, hint, posibleSolucion, descripcion, idCurso)

        agregado = self.dao.agregar(mapa)


    def traerEscenariosPorCursos(self, idCurso):
        return self.dao.traerEscenariosPorCurso(idCurso)
