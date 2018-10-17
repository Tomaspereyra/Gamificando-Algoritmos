from dao.UsuarioDao import UsuarioDao
from datos.Usuario import Usuario


class UsuarioABM:
    def __init__(self):
        self.dao = UsuarioDao()

    def traerUsuario(self, username):
        return self.dao.traerUsuario(username)

    def registrarUsuario(self, username, password, email, nombre, apellido, fechaNacimiento):
        if self.traerUsuario(username) is None:
            usuario = Usuario(username, password, email, nombre, apellido, fechaNacimiento)
            self.dao.agregar(usuario)
        else:
            print "El usuario ya esta registrado"

    def eliminarUsuario(self, usuario):
        usuarioBuscado=self.traerUsuario(usuario.getUsername())
        eliminado=False

        if usuarioBuscado is not None:
            self.dao.eliminar(usuarioBuscado)
            eliminado = True
        else:
            print "El usuario no esta registrado"

        return eliminado

    def editarUsuario(self, usuario, usuarioEditado):
        if self.traerUsuario(usuarioEditado.getUsername()) is None \
                and self.traerUsuario(usuario.getUsername()) is not None:
            self.dao.actualizarUsuario(usuario, usuarioEditado)
        else:
            print "Error, no se pudo actualizar"




