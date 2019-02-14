from dao.CursoDao import CursoDao
from negocio.JuegoABM import JuegoABM


class CursoABM:

    def __init__(self):
        self.dao = CursoDao()

    def traerCurso(self, idCurso):
        return self.dao.traerCurso(idCurso)

    def actualizarCurso(self, curso):
        return self.dao.actualizarCurso(curso)

    def agregarCurso(self, sePuedeSaltear, nombre, descripcion, docente, juego, fechaCreacion):
        juegoabm = JuegoABM()
        return self.dao.agregar(sePuedeSaltear, nombre, descripcion, docente.getIdDocente(), juegoabm.traerJuego(juego.getNombre()), fechaCreacion)

    def traerCursos(self):
        return self.dao.traerCursos()

    def traerCursosPorDocente(self, docente):
        return self.dao.traerCursosPorDocente(docente)

    def traerCursosPorIdDocente(self, idDocente):
        return self.dao.traerCursosPorDocente(idDocente)

    def eliminar(self, idCurso):
        curso = self.dao.traerCurso(idCurso)
        if curso is not None:
            self.dao.eliminar(curso)
            return True
        else:
            return False


