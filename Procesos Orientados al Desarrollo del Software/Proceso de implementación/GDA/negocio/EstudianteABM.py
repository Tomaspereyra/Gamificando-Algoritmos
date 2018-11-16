from dao.EstudianteDao import EstudianteDao

from negocio.UsuarioABM import UsuarioABM


class EstudianteABM:
    def __init__(self):
        self.dao = EstudianteDao()

    def traerEstudiante(self, username):
        usuarioabm = UsuarioABM()
        estudiante = None

        try:
            usuario = usuarioabm.traerUsuario(username)
            estudiante = self.dao.traerEstudiante(usuario.getId())

        finally:
            return estudiante

    def agregarEstudiante(self, username, password, email, nombre, apellido, fechaNacimiento):
        agregado = 0
        if self.traerEstudiante(username) is None:
            usuarioabm = UsuarioABM()
            usuarioabm.registrarUsuario(username, password, email, nombre, apellido, fechaNacimiento)
            agregado = self.dao.agregar(usuarioabm.traerUsuario(username))
        else:
            print "Error, el usuario ya es un estudiante"

        return agregado

    def eliminarEstudiante(self, username):
        estudiante = self.traerEstudiante(username)
        if estudiante is not None:
            self.dao.eliminar(estudiante)
        else:
            print "Error el estudiante no existe"
