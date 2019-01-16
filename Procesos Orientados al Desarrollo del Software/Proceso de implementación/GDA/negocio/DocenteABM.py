from negocio.UsuarioABM import UsuarioABM
from datos.Docente import Docente
from dao.DocenteDao import DocenteDao


class DocenteABM:

    def __init__(self):
        self.dao = DocenteDao()

    def traerDocente(self, username):
        usuario = UsuarioABM()
        docente = None
        if usuario.traerUsuario(username) is not None:
            docente = self.dao.traerDocente(usuario.traerUsuario(username).getId())

        return docente

    def registrarDocente(self, username, password, email, nombre, apellido, fechaNacimiento):
        agregado = 0
        if self.traerDocente(username) is None:
            usuario = UsuarioABM()
            usuario.registrarUsuario(username, password, email, nombre, apellido, fechaNacimiento)

            agregado = self.dao.agregarDocente(int(usuario.traerUsuario(username).getId()))

        else:
            print "Nombre de usuario en uso."

        return agregado

    def eliminarDocente(self, username):
        docente = self.traerDocente(username)
        print docente.getIdDocente()
        if docente is not None:
            self.dao.eliminar(docente)
            print docente.getUsername()
        else:
            print "Error, el docente no existe"
