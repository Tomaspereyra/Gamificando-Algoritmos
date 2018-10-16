import MySQLdb

from Conexion import Sesion
from datos.Estudiante import Estudiante
from datos.CursoIniciado import CursoIniciado
from dao.CursoDao import CursoDao
from dao.EscenarioEnProcesoDao import EscenarioEnProcesoDao


class CursoIniciadoDao:

    def iniciarOperacion(self):
        try:
            sesion = Sesion()

        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def agregar(self, idEstudiante,idCurso):

        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()

        try:
            cursor.execute("""insert into CursoIniciado(Estudiante_idEstudiante, Curso_idCurso) 
             values ('%i','%i')""" % (
                idEstudiante, idCurso))
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

    def traerCursosPorEstudiante(self, idEstudiante):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        lstCursos = []
        curso = CursoIniciado()
        cursodao = CursoDao()

        try:
            cursor.execute("""select * from cursoiniciado where cursoiniciado.Estudiante_idEstudiante = '%i'"""
                           % idEstudiante)
            resultado = cursor.fetchall()
            escenarioenproceso = EscenarioEnProcesoDao()
            for fila in range(len(resultado)):
                 for columna in range(len(resultado[fila])):
                     if columna == 0:
                         curso.setIdCursoIniciado(resultado[fila][columna])
                         curso.agregarEscenario(escenarioenproceso.traerEscenariosPorCurso(resultado[fila][columna]))
                     if columna == 2:
                         curso.setCurso(cursodao.traerCurso(resultado[fila][columna]))
                         lstCursos.append(curso)
                         curso = CursoIniciado()
        finally:
            cursor.close()
            sesion.cerrarConexion()
            return lstCursos


