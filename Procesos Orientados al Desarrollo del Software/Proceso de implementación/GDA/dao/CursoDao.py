import MySQLdb
from Conexion import Sesion


class CursoDao:
    def iniciarOperacion(self):

        try:
            sesion = Sesion()  # iniciar sesion con la bd
        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def agregar(self, curso):

        sesion = self.iniciarOperacion()

        cursor = sesion.obtenerCursor()

        try:
            cursor.execute("""insert into Curso (sePuedeSaltear,nombre,docente_idDocente)
             values('%s', '%s','%i')""" % (curso.getSepuedeSaltar(), curso.getNombre(),
                                           curso.getDocente().getIdDocente()))
            sesion.commit()
        except:
            print "Error en la ejecucion de la query"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()

    def eliminar(self, curso):

        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""delete Curso from Curso where Curso.idCurso 
            = '%i'""" % (curso.getIdCurso()))
            sesion.commit()
        except:
            print "Error no se pudo eliminar el curso"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()
