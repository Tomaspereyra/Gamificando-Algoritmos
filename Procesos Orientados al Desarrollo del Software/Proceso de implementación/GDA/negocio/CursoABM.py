from dao.CursoDao import CursoDao
from negocio.JuegoABM import JuegoABM


class CursoABM:

    def __init__(self):
        self.dao = CursoDao()

    def traerCurso(self, idCurso):
        return self.dao.traerCurso(idCurso)

    def agregarCurso(self, sePuedeSaltear, nombre, descripcion, docente, juego):
        juegoabm = JuegoABM()
        return self.dao.agregar(sePuedeSaltear, nombre, descripcion, docente.getIdDocente(), juegoabm.traerJuego(juego.getNombre()))

