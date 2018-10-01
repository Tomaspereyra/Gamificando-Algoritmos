import MySQLdb

from Conexion import Sesion
from datos.EscenarioEnProceso import EscenarioEnProceso
from dao.EscenarioDao import EscenarioDao
from datos.Escenario import Escenario


class EscenarioEnProcesoDao:

    def iniciarOperacion(self):
        try:
            sesion = Sesion()

        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def agregar(self, escenarioEnProceso, idCurso):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()

        try:
            cursor.execute("""insert into EscenarioEnProceso(puntajeObtenido, solucionBrindada, fechaInicio, 
            fechaFinalizacion, cantidadBloquesUtilizados, tiempoSolucion, intentos,CursoIniciado_idCursoIniciado,
             Escenario_idEscenario) values('%i','%s','%s','%s','%i','%i','%i','%i','%i')""" %
                           (escenarioEnProceso.getPuntajeObtenido(), escenarioEnProceso.getSolucionBrindada(),
                            escenarioEnProceso.getFechaInicio(), escenarioEnProceso.getFechaFinalizacion(),
                            escenarioEnProceso.getCantidadBloquesUtilizados(), escenarioEnProceso.getTiempoSolucion(),
                            escenarioEnProceso.getIntentos(), idCurso, escenarioEnProceso.getEscenario().getIdEscenario()))
            sesion.commit()

        finally:
            cursor.close()
            sesion.cerrarConexion()

    def eliminar(self, escenarioEnProceso):

        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""delete EscenarioEnProceso from EscenarioEnProceso where EscenarioEnProceso.idEscenarioEnProceso
            = '%i'""" % (escenarioEnProceso.getId()))
            sesion.commit()
        except:
            print "Error no se pudo eliminar el escenario en proceso"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()


escenario = EscenarioEnProcesoDao()
esce = EscenarioEnProceso(1, "solucionBrindada", 5, 10, 2, "2018-09-29", "2018-09-30")
escenarioPrueba = EscenarioDao()
esc = escenarioPrueba.traerEscenario(1)

esce.setEscenario(esc)
escenario.agregar(esce, 1)
