from datos.Curso import Curso
from datos.Estudiante import Estudiante


class CursoIniciado:

    def __init__(self, curso="-"):
        self.curso = curso
        self.escenarioRealizado = []

    def setCurso(self, curso):
        self.curso = curso

    def agregarEscenario(self, escenarioRealizado):
        self.escenarioRealizado.append(escenarioRealizado)


    def setIdCursoIniciado(self,cursoIniciado):
        self.idCursoIniciado=cursoIniciado

    def getIdCursoIniciado(self):
        return self.idCursoIniciado

    def getCurso(self):
        return self.curso

    def __str__(self):
        return str(self.getCurso().__str__())
