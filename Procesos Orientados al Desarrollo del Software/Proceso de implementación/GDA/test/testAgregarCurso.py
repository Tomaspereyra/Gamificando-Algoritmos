from negocio.CursoABM import CursoABM
from negocio.DocenteABM import DocenteABM
from negocio.JuegoABM import JuegoABM


class Test:
    def __init__(self):
        pass

    def agregarCurso(self,sePuedeSaltar, nombre, descripcion, usuarioDocente, nombreJuego):
        curso = CursoABM()
        docente = DocenteABM()
        juego = JuegoABM()
        curso.agregarCurso(sePuedeSaltar, nombre, descripcion, docente.traerDocente(usuarioDocente), juego.traerJuego(nombreJuego))


test = Test()

test.agregarCurso(0, "Nuevo Curso", "Desc", "Profe", "Juego Nuevo")