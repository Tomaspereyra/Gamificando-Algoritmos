from negocio.CursoIniciadoABM import CursoIniciadoABM
from negocio.EstudianteABM import EstudianteABM
from negocio.CursoABM import CursoABM

class TestComenzarCurso:

    def __init__(self):
        pass
    def comenzarCurso(self, estudiante, cursoaComenzar):
        curso = CursoIniciadoABM()
        curso.comenzarCurso(estudiante, cursoaComenzar)


test = TestComenzarCurso()
estudiante = EstudianteABM()
curso = CursoABM()
test.comenzarCurso(estudiante.traerEstudiante("User"), curso.traerCurso(1))