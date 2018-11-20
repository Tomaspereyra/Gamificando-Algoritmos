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
        filasAfectadas = 0
        print("ids : " + str(idEstudiante) + " - " + str(idCurso))
        try:
            filasAfectadas = cursor.execute("""insert into CursoIniciado(Estudiante_idEstudiante, Curso_idCurso) 
             values ('%i','%i')""" % (long(idEstudiante), long(idCurso)))
            sesion.commit()
        except Exception as e:
            print "Error en la ejecucion de la query : " + e.message
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()
            return filasAfectadas

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

    def traerCurso(self, idCurso):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        curso = CursoIniciado()
        cursodao = CursoDao()
        try:
            cursor.execute("""select * from cursoiniciado where cursoiniciado.idCursoIniciado='%i'""" % idCurso)
            daoEscenario = EscenarioEnProcesoDao()
            resultado = cursor.fetchone()
            curso.setIdCursoIniciado(resultado[0])
            curso.setCurso(cursodao.traerCurso(resultado[2]))
            curso.setEscenarios(daoEscenario.traerEscenariosPorCurso(curso.getIdCursoIniciado()))
        finally:
            cursor.close()
            sesion.cerrarConexion()
            return curso

    def traerCursoIniciado(self, estudiante, curso):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        cursodao = CursoDao()
        cursoIniciado = None
        try:
            cursor.execute("""select * from cursoiniciado where cursoiniciado.Estudiante_idEstudiante='%i' AND cursoiniciado.Curso_idCurso='%i'""" % (estudiante.idEstudiante, curso.idCurso))
            daoEscenario = EscenarioEnProcesoDao()
            resultado = cursor.fetchone()
            cursoIniciado = CursoIniciado()
            cursoIniciado.setIdCursoIniciado(resultado[0])
            cursoIniciado.setCurso(cursodao.traerCurso(resultado[2]))
            cursoIniciado.setEscenarios(daoEscenario.traerEscenariosPorCurso(cursoIniciado.getIdCursoIniciado()))
        except Exception as e:
            print("Error en Query : " + e.message)
            return None
        finally:
            cursor.close()
            sesion.cerrarConexion()
            return cursoIniciado

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


