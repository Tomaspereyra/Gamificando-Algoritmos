from datos.Curso import Curso
from datos.Estudiante import Estudiante


class CursoIniciado:

    def __init__(self, curso="-"):
        self.curso = curso
        self.escenarioRealizado = []
        self.idCursoIniciado = -1;

    def setCurso(self, curso):
        self.curso = curso

    def agregarEscenario(self, escenarioRealizado):
        self.escenarioRealizado.append(escenarioRealizado)

    def setIdCursoIniciado(self, cursoIniciado):
        self.idCursoIniciado = cursoIniciado

    def getIdCursoIniciado(self):
        return self.idCursoIniciado

    def getCurso(self):
        return self.curso

    def getEscenarios(self):
        return self.escenarioRealizado

    def setEscenarios(self, escenarios):
        self.escenarioRealizado = []
        self.escenarioRealizado.extend(escenarios)

    def __str__(self):
        return str(self.getCurso().__str__() + "Escenarios: " + str(self.imprimirLista()))

    def imprimirLista(self):
        try:
            return ''.join('\n'.join(map(str, sl)) for sl in self.getEscenarios())
        except:
            return "[]"
