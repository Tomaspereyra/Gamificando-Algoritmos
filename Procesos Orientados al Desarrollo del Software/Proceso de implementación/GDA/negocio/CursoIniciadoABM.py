from dao.CursoIniciadoDao import CursoIniciadoDao


class CursoIniciadoABM:
    def __init__(self):
        self.dao = CursoIniciadoDao()

    def traerCursosIniciadosPorEstudiante(self, estudiante):
        return self.dao.traerCursosPorEstudiante(estudiante.getIdEstudiante())

    def comenzarCurso(self, estudiante, curso):
        self.dao.agregar(estudiante.getIdEstudiante(), curso.getIdCurso())

    def eliminarCursoIniciado(self, cursoIniciado):
        self.dao.eliminar(cursoIniciado)

    def traerCurso(self, idCurso):
        return self.dao.traerCurso(idCurso)
