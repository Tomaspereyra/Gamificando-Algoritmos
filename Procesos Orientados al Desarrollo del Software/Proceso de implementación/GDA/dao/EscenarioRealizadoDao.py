import MySQLdb

from Conexion import Sesion


class EscenarioRealizadoDao:

    def iniciarOperacion(self):
        try:
            sesion = Sesion()

        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def agregar(self, escenarioRealizado):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()

        try:
            cursor.execute("""insert into EscenarioRealizado(puntajeObtenido, solucionBrindada,
                            CursoIniciado_idCursoIniciado, Escenario_idEscenario) values('%i','%s','%i','%i')""" %
                           (escenarioRealizado.getPuntajeObtenido(), escenarioRealizado.getSolucionBrindada(),
                            escenarioRealizado.getCurso().getIdCurso(),
                            escenarioRealizado.getEscenario().getIdEscenario()))
            sesion.commit()
        except:
            print "Error en la ejecucion de la query"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()

    def eliminar(self, escenarioRealizado):

        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""delete EscenarioRealizado from EscenarioRealizado where EscenarioRealizado.idEscenarioRealizado 
            = '%i'""" % (escenarioRealizado.getEscenario().getIdEscenario()))  # no estoy trayendo el id del
            # escenario realizado si no el del escenario#
            sesion.commit()
        except:
            print "Error no se pudo eliminar el escenario realizado"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()
