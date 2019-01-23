import MySQLdb
from Conexion import Sesion
from datos.Usuario import Usuario


class UsuarioDao:

    def iniciarOperacion(self):

        try:
            sesion = Sesion()  # iniciar sesion con la bd
        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def agregar(self, usuario):
        sesion = self.iniciarOperacion()

        cursor = sesion.obtenerCursor()
        filasAfectadas = 0
        try:
              filasAfectadas= cursor.execute("""insert into Usuario(username,password,email,nombre,apellido, fechaNacimiento)
              values('%s', '%s', '%s', '%s', '%s', '%s' )""" % (
                usuario.getUsername(), usuario.getPassword(), usuario.getEmail(), usuario.getNombre(),
                usuario.getApellido(), usuario.getFechaNacimiento()))
              sesion.commit()
        except:
            print "Error en ejecucion de la query"
            sesion.getEstado().rollback()  # volver al estado anterior

        finally:
            cursor.close()
            sesion.cerrarConexion()
            return filasAfectadas

    def eliminar(self, usuario):
        sesion = self.iniciarOperacion()

        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""delete Usuario from Usuario where Usuario.username='%s'""" % (usuario.getUsername()))
            sesion.commit()
        except:
            print "Error, no se pudo eliminar"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()

    def traerUsuario(self, username):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        usuario = None
        try:
            cursor.execute("""select * from Usuario where Usuario.username='%s'""" % username)
            resultado = cursor.fetchone()
            if resultado is not None:
                usuario = Usuario(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6])
                usuario.setIdUsuario(resultado[0])
        except:
            print "Error, no se pudo traer el usuario"
        finally:
            cursor.close()
            sesion.cerrarConexion()

        return usuario

    def traerUsuarioPorId(self, id):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        usuario = None
        try:
            cursor.execute("""select * from Usuario where Usuario.idUsuario='%i'""" % int(id))
            resultado = cursor.fetchone()
            if resultado is not None:
                usuario = Usuario(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6])
                usuario.setIdUsuario(resultado[0])

        finally:
            cursor.close()
            sesion.cerrarConexion()

        return usuario

    def actualizarUsuario(self, username, usuarioActualizado):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""update Usuario set username='%s',password='%s',email ='%s',nombre = '%s' , apellido = '%s', fechaNacimiento = '%s' 
                    where username= '%s'""" % (
                usuarioActualizado.getUsername(), usuarioActualizado.getPassword(),
                usuarioActualizado.getEmail(), usuarioActualizado.getNombre(),
                usuarioActualizado.getApellido(), usuarioActualizado.getFechaNacimiento(), username))
            sesion.commit()
        finally:
            cursor.close()
            sesion.cerrarConexion()


