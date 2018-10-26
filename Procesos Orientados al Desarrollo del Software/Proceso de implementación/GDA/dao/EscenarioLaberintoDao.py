from Conexion import Sesion
from datos.EscenarioLaberinto import EscenarioLaberinto


class EscenarioLaberintoDao:

    def iniciarOperacion(self):

        try:
            sesion = Sesion()  # iniciar sesion con la bd
        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def agregar(self, escenarioLaberinto):

        sesion = self.iniciarOperacion()

        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""insert into EscenarioLaberinto(mapa, idEscenario)
              values('%s', '%i')""" % (escenarioLaberinto.getMapa(), escenarioLaberinto.getIdEscenario()))
            sesion.commit()
        except:
            print "Error en ejecucion de la query"
            sesion.getEstado().rollback()  # volver al estado anterior

        finally:
            cursor.close()
            sesion.cerrarConexion()

    def eliminar(self, idEscenario):
        sesion = self.iniciarOperacion()

        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""delete EscenarioLaberinto from EscenarioLaberinto where 
            EscenarioLaberinto.Escenario_idEscenario='%i'""" % idEscenario)
            sesion.commit()
        except:
            print "Error, no se pudo eliminar"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()

    def traerEscenarioLaberinto(self, idEscenario):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        escenarioLaberinto = None
        try:
            cursor.execute("""select * from Escenario inner join Escenariolaberinto where 
            escenariolaberinto.Escenario_idEscenario = '%i' and escenario.idEscenario = '%i'""" % (idEscenario,
                                                                                                   idEscenario))
            resultado = cursor.fetchone()
            if resultado is not None:
                escenarioLaberinto = EscenarioLaberinto(resultado[1], resultado[2], resultado[3], resultado[4],
                                                        resultado[5], resultado[7])
                escenarioLaberinto.setIdEscenario(resultado[0])

        finally:
            cursor.close()
            sesion.cerrarConexion()
            return escenarioLaberinto


escenarioLab = EscenarioLaberintoDao()

print escenarioLab.traerEscenarioLaberinto(1)
