from dao.JuegoDao import JuegoDao
from datos.Juego import Juego


class JuegoABM:
    def __init__(self):
        self.dao = JuegoDao()

    def traerJuego(self, nombre):
        return self.dao.traerJuego(nombre)

    def agregarJuego(self, nombre, descripcion):
        agregado = False
        if self.traerJuego(nombre) is None:
            self.dao.agregar(nombre, descripcion)
            agregado = True

        return agregado

    def eliminarJuego(self, nombre):
        self.dao.eliminar(self.traerJuego(nombre))

