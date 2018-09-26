import Curso


class CursoIniciado:

    def __init__(self):
        self.curso = Curso
        self.escenarioRealizado = []
        self.estudiante = estudiante

    def setCurso(self, curso):
        self.curso = curso

    def agregarEscenario(self, escenarioRealizado):
        self.escenarioRealizado.append(escenarioRealizado)

    def setEstudiante(self, estudiante):
        self.estudiante = estudiante

    def setIdCursoIniciado(self,cursoIniciado):
        self.idCursoIniciado=cursoIniciado

    def getIdCursoIniciado(self):
        return self.idCursoIniciado

    def getCurso(self):
        return self.curso

    def getEstudiante(self):
        return self.estudiante
