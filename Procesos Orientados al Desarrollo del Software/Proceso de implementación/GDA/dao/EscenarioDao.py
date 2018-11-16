import MySQLdb
from Conexion import Sesion
from datos.Escenario import Escenario
from dao.EscenarioLaberintoDao import EscenarioLaberintoDao


class EscenarioDao:

    def iniciarOperacion(self):

        try:
            sesion = Sesion()  # iniciar sesion con la bd
        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def agregar(self, bloquesPermitidos, cantBloquesMax, hint, posibleSolucion, descripcion, idCurso):

        sesion = self.iniciarOperacion()

        cursor = sesion.obtenerCursor()
        filasAfectadas = 0
        try:
            filasAfectadas = cursor.execute("""insert into Escenario (bloquesPermitidos, cantBloquesMax, hint, posibleSolucion,
                           descripcion,Curso_idCurso) values('%i','%i','%s','%s','%s','%i')""" % (
                bloquesPermitidos, cantBloquesMax, hint, posibleSolucion, descripcion, idCurso))
            sesion.commit()
        except:
            print "Error en la ejecucion de la query"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()
            return filasAfectadas

    def eliminar(self, escenario):
        sesion = self.iniciarOperacion()

        cursor = sesion.obtenerCursor()
        try:
            cursor.execute(
                """delete Escenario from Escenario where Escenario.idEscenario = '%i'""" % (escenario.getIdEscenario()))
            sesion.commit()
        except:
            print "Error, no se pudo eliminar el escenario"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()

    def traerEscenariosPorCurso(self, idCurso):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        resultado = None
        escenariolab = EscenarioLaberintoDao()
        try:
            cursor.execute("""select * from Escenario where Escenario.Curso_idCurso='%i'""" % idCurso)
            resultado = cursor.fetchall()
        except:
            print "Error no se pudo traer los escenarios"
        finally:
            cursor.close()
            sesion.cerrarConexion()
        return resultado

    def traerEscenario(self, idEscenario):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        resultado = None
        escenario = None
        try:
            cursor.execute("""select * from Escenario where Escenario.idEscenario='%i'""" % idEscenario)
            resultado = cursor.fetchone()
            if resultado is not None:
                escenario = Escenario(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
                escenario.setIdEscenario(resultado[0])

        except:
            print "Error no se pudo traer los escenarios"
        finally:
            cursor.close()
            sesion.cerrarConexion()
        return escenario
