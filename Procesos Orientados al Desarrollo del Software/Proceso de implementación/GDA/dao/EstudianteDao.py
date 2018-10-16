import MySQLdb

from Conexion import Sesion
from datos.Estudiante import Estudiante
from dao.CursoIniciadoDao import CursoIniciadoDao
from datos.CursoIniciado import CursoIniciado


class EstudianteDao:

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
        try:
            cursor.execute("""insert into Estudiante(Usuario_idUsuario)
              values('%i')""" % (usuario.getId()))

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
            cursor.execute(
                """delete Estudiante from Estudiante where Estudiante.Usuario_idUsuario='%i'""" % (estudiante.getId()))
            sesion.commit()
        except:
            print "Error, no se pudo eliminar"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()

    def traerEstudiante(self, idUsuario):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        estudiante = None
        try:
            cursor.execute("""select * from usuario inner join estudiante where usuario.idUsuario = '%i' and 
            estudiante.Usuario_idUsuario = '%i'""" % (idUsuario, idUsuario))
            resultado = cursor.fetchone()
            estudiante = Estudiante(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6])
            estudiante.setIdUsuario(resultado[0])
            estudiante.setIdEstudiante(resultado[7])
            cursoiniciadodao = CursoIniciadoDao()
            estudiante.agregarCursos(cursoiniciadodao.traerCursosPorEstudiante(estudiante.getIdEstudiante()))

        finally:
            cursor.close()
            sesion.cerrarConexion()
            return estudiante




