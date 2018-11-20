from dao.CursoIniciadoDao import CursoIniciadoDao


class CursoIniciadoABM:
    def __init__(self):
        self.dao = CursoIniciadoDao()

    def traerCursosIniciadosPorEstudiante(self, estudiante):
        return self.dao.traerCursosPorEstudiante(estudiante.getIdEstudiante())

    def traerCursosIniciadosPorIdEstudiante(self, idEstudiante):
        return self.dao.traerCursosPorEstudiante(idEstudiante)

    def traerCursoIniciado(self, estudiante, curso):
        return self.dao.traerCursoIniciado(estudiante, curso)

    def comenzarCurso(self, estudiante, curso):
        return self.dao.agregar(estudiante.getIdEstudiante(), curso.getIdCurso())

    def eliminarCursoIniciado(self, cursoIniciado):
        self.dao.eliminar(cursoIniciado)

    def traerCurso(self, idCursoIniciado):
        return self.dao.traerCurso(idCursoIniciado)
