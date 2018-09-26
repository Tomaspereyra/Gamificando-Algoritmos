import MySQLdb

from Conexion import Sesion


class CursoIniciadoDao:

    def iniciarOperacion(self):
        try:
            sesion = Sesion()

        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def agregar(self, cursoIniciado):

        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()

        try:
            cursor.execute("""insert into CursoIniciado(Estudiante_idEstudiante, Curso_idCurso) 
             values ('%i','%i')""" % (
                cursoIniciado.getEstudiante().getIdEstudiante(), cursoIniciado.getCurso().getIdCurso()))
            sesion.commit()
        except:
            print "Error en la ejecucion de la query"
            sesion.getEstado().rollback()

        finally:
            cursor.close()
            sesion.cerrarConexion()

    def eliminar(self, cursoIniciado):

        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""delete CursoIniciado from CursoIniciado where CursoIniciado.idCursoIniciado 
            = '%i'""" % (cursoIniciado.getIdCursoIniciado()))
            sesion.commit()
        except:
            print "Error no se pudo eliminar el curso"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()
