import MySQLdb

from Conexion import Sesion


class EstudianteDao:

    def iniciarOperacion(self):

        try:
            sesion = Sesion()  # iniciar sesion con la bd
        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def agregarEstudiente(self, estudiante):
        sesion = self.iniciarOperacion()

        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""insert into Estudiante(Usuario_idUsuario)
              values('%i')""" % (estudiante.getId()))

            sesion.commit()
        except:
            print "Error en la ejecucion de la query"

            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()

    def eliminar(self, estudiante):
        sesion = self.iniciarOperacion()

        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""delete Estudiante from Estudiante where Estudiante.Usuario_idUsuario='%i'""" % (estudiante.getId()))
            sesion.commit()
        except:
            print "Error, no se pudo eliminar"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()
