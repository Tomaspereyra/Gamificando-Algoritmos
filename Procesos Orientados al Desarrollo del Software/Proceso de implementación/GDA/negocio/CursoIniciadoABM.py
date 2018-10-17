from dao.CursoIniciadoDao import CursoIniciadoDao
from datos.CursoIniciado import CursoIniciado


class CursoIniciadoABM:
    def __init__(self):
        self.dao = CursoIniciadoDao()

    def traerCursosIniciadosPorEstudiante(self, estudiante):
        return self.dao.traerCursosPorEstudiante(estudiante.getIdEstudiante())

    def agregarCursoIniciado(self, estudiante, curso):
        self.dao.agregar(estudiante.getIdEstudiante(), curso.getIdCurso())

    def eliminarCursoIniciado(self, cursoIniciado):
        self.dao.eliminar(cursoIniciado)
