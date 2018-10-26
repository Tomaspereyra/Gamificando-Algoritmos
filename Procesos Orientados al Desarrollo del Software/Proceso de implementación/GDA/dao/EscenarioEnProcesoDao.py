import MySQLdb

from Conexion import Sesion
from datos.EscenarioEnProceso import EscenarioEnProceso
from dao.EscenarioDao import EscenarioDao



class EscenarioEnProcesoDao:

    def iniciarOperacion(self):
        try:
            sesion = Sesion()

        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def comenzarEscenario(self, fechaInicio, idEscenario, idCurso):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()

        try:
            cursor.execute("""insert into EscenarioEnProceso(fechaInicio, Escenario_idEscenario, 
            CursoIniciado_idCursoIniciado) values ('%s', '%i','%i')""" % (fechaInicio, idEscenario, idCurso))
            sesion.commit()
        finally:
             cursor.close()
             sesion.cerrarConexion()

    def terminarEscenario(self, escenarioEnProceso):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()

        try:
            cursor.execute(""" update EscenarioEnProceso set puntajeObtenido ='%i', solucionBrindada = '%s', 
            fechaFinalizacion='%s', cantidadBloquesUtilizados='%i', tiempoSolucion='%i', intentos ='%i' 
            where idEscenarioEnProceso = '%i'""" % (escenarioEnProceso.getPuntajeObtenido(),
                                                   escenarioEnProceso.getSolucionBrindada(),
                                                   escenarioEnProceso.getFechaFinalizacion(),
                                                   escenarioEnProceso.getCantidadBloquesUtilizados(),
                                                   escenarioEnProceso.getTiempoSolucion(),
                                                   escenarioEnProceso.getIntentos(), escenarioEnProceso.getId()))

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

    def traerEscenariosPorCurso(self, idCurso):

        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        lstEscenarios = []

        try:
            cursor.execute("""select * from EscenarioEnProceso where EscenarioEnProceso.CursoIniciado_idCursoIniciado='%i'"""
                           % idCurso)
            resultado = cursor.fetchall()
            if resultado is not None:
                escenarioenproceso = EscenarioEnProceso()
                escenariodao = EscenarioDao()
                for fila in range(len(resultado)):
                    for columna in range(len(resultado[fila])):
                        if columna ==0:
                            escenarioenproceso.setId(resultado[fila][columna])
                        if columna == 1:
                            escenarioenproceso.setPuntajeObtenido(resultado[fila][columna])
                        if columna == 2:
                            escenarioenproceso.setSolucionBrindada(resultado[fila][columna])
                        if columna == 3:
                            escenarioenproceso.setFechaInicio(resultado[fila][columna])
                        if columna == 4:
                            escenarioenproceso.setFechaFinalizacion(resultado[fila][columna])
                        if columna == 5:
                            escenarioenproceso.setCantidadBloquesUtilizados(resultado[fila][columna])
                        if columna == 6:
                            escenarioenproceso.setTiempoSolucion(resultado[fila][columna])
                        if columna == 7:
                            escenarioenproceso.setIntentos(resultado[fila][columna])
                        if columna == 8:
                            escenarioenproceso.setEscenario(escenariodao.traerEscenario(resultado[fila][columna]))
                            lstEscenarios.append(escenarioenproceso)
                            escenarioenproceso = EscenarioEnProceso()
        finally:
            cursor.close()
            sesion.cerrarConexion()
            return lstEscenarios

    def traerEscenario(self, idEscenario):
        sesion = Sesion()
        cursor = sesion.obtenerCursor()
        escenarioEnProceso = EscenarioEnProceso()
        escenario =EscenarioDao()


        try:
            cursor.execute("""select * from EscenarioEnProceso where EscenarioEnProceso.idEscenarioEnProceso ='%i'""" %
                           idEscenario)
            resultado = cursor.fetchone()
            escenarioEnProceso.setId(resultado[0])
            escenarioEnProceso.setPuntajeObtenido(resultado[1])
            escenarioEnProceso.setSolucionBrindada(resultado[2])
            escenarioEnProceso.setFechaInicio(resultado[3])
            escenarioEnProceso.setFechaFinalizacion(resultado[4])
            escenarioEnProceso.setCantidadBloquesUtilizados(resultado[5])
            escenarioEnProceso.setTiempoSolucion(resultado[6])
            escenarioEnProceso.setIntentos(resultado[7])
            escenarioEnProceso.setEscenario(escenario.traerEscenario(resultado[8]))
        finally:
            cursor.close()
            sesion.cerrarConexion()
            return escenarioEnProceso

