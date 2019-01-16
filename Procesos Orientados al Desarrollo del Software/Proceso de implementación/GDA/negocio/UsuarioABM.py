from __future__ import print_function
from dao.UsuarioDao import UsuarioDao
from datos.Usuario import Usuario

import sys


class UsuarioABM:
    def __init__(self):
        self.dao = UsuarioDao()

    def traerUsuario(self, username):
        return self.dao.traerUsuario(username)

    def traerUsuarioPorId(self, id):
        return self.dao.traerUsuarioPorId(id)

    def registrarUsuario(self, username, password, email, nombre, apellido, fechaNacimiento):
        filasAfectadas = 0
        if self.traerUsuario(username) is None:
            usuario = Usuario(username, password, email, nombre, apellido, fechaNacimiento)
            filasAfectadas = self.dao.agregar(usuario)
        else:
            print('El usuario ya esta registrado', file=sys.stdout)

        return filasAfectadas

    def eliminarUsuario(self, usuario):
        usuarioBuscado = self.traerUsuario(usuario.getUsername())
        eliminado = False

        if usuarioBuscado is not None:
            self.dao.eliminar(usuarioBuscado)
            eliminado = True
        else:
            print('El usuario no esta registrado', file=sys.stdout)

        return eliminado

    def editarUsuario(self, username, usuarioEditado):
        if username != usuarioEditado.getUsername():

            if self.traerUsuario(usuarioEditado.getUsername()) is None \
                    and self.traerUsuario(username) is not None:
                self.dao.actualizarUsuario(username, usuarioEditado)
            else:
                print("Error, no se pudo actualizar", file=sys.stdout)
        else:
            self.dao.actualizarUsuario(username, usuarioEditado)
