from negocio.CursoABM import CursoABM
from negocio.DocenteABM import DocenteABM
from negocio.JuegoABM import JuegoABM


def test_AgregarCurso():
    curso = CursoABM()
    docente = DocenteABM()
    juego = JuegoABM()
    resultado = curso.agregarCurso(True, "nombre", "descripcion", docente.traerDocente("Profe"), juego.traerJuego("Juego Nuevo"))
    assert resultado == 1


def test_traerCurso():
    curso = CursoABM()
    c = curso.traerCurso(1)
    assert c.getIdCurso() == 1


