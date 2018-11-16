from negocio.CursoIniciadoABM import CursoIniciadoABM
from negocio.EstudianteABM import EstudianteABM
from negocio.CursoABM import CursoABM


def test_traerCursoIniciado():
    curso = CursoIniciadoABM()
    c = curso.traerCurso(1)
    assert c.getIdCursoIniciado() == 1


def test_ComenzarCurso():
    cursoIniciado = CursoIniciadoABM()
    estudiante = EstudianteABM()
    curso = CursoABM()
    filasAfectadas = cursoIniciado.comenzarCurso(estudiante.traerEstudiante("tomas") , curso.traerCurso(1))
    assert filasAfectadas == 1