from __future__ import print_function
import MySQLdb
import sys
from Conexion import Sesion
from datos.Escenario import Escenario
from dao.EscenarioLaberintoDao import EscenarioLaberintoDao


class EscenarioDao:

    def iniciarOperacion(self):

        try:
            sesion = Sesion()  # iniciar sesion con la bd
        except MySQLdb.OperationalError:
            print ("Error en la conexion")
            sesion = None

        return sesion

    def agregar(self, bloquesPermitidos, cantBloquesMax, hint, posibleSolucion, descripcion, idCurso):

        sesion = self.iniciarOperacion()

        cursor = sesion.obtenerCursor()
        filasAfectadas = 0
        try:
            filasAfectadas = cursor.execute("""insert into Escenario (bloquesPermitidos, cantBloquesMax, hint, posibleSolucion,
                           descripcion,Curso_idCurso) values('%s','%i','%s','%s','%s','%i')""" % (
                bloquesPermitidos, int(cantBloquesMax), hint, posibleSolucion, descripcion, int(idCurso)))
            sesion.commit()
        except Exception as e:
            print ("Error en la ejecucion de la query : " + e.message)
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()
            return filasAfectadas

    def actualizarEscenario(self, escenario):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""update Escenario set descripcion='%s',cantBloquesMax='%s', hint='%s', posibleSolucion='%s' where idEscenario = '%s'""" % (
                escenario.getDescripcion(), escenario.getCantBloquesMax(),
                escenario.getHint(), escenario.getPosiblesSolucion(), escenario.getIdEscenario()))
            sesion.commit()
        except:
            print ("Error, no se pudo actualizar")
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()

    def eliminar(self, escenario):
        sesion = self.iniciarOperacion()

        cursor = sesion.obtenerCursor()
        try:
            cursor.execute(
                """delete Escenario from Escenario where Escenario.idEscenario = '%i'""" % (escenario.getIdEscenario()))
            sesion.commit()
        except:
            print ("Error, no se pudo eliminar el escenario")
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()

    def traerEscenariosPorCurso(self, idCurso):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        resultado = None
        escenariolab = EscenarioLaberintoDao()
        escenarios = []
        try:
            cursor.execute("""select * from Escenario where Escenario.Curso_idCurso='%i'""" % idCurso)
            resultado = cursor.fetchall()
            print("Resultado : " + str(resultado), file=sys.stdout)
            if resultado is not None:
                for tuple in resultado:
                    e = Escenario(tuple[1], tuple[2], tuple[3], tuple[4], tuple[5])
                    e.setIdEscenario(tuple[0])
                    e.setIdCurso(tuple[6])
                    escenarios.append(e)

        except:
            print ("Error no se pudo traer los escenarios", file=sys.stdout)
        finally:
            cursor.close()
            sesion.cerrarConexion()
        return escenarios

    def traerEscenario(self, idEscenario):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        resultado = None
        escenario = Escenario()
        try:
            cursor.execute("""select * from Escenario where Escenario.idEscenario='%i'""" % int(idEscenario))
            resultado = cursor.fetchone()
            if resultado is not None:
                escenario = Escenario(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
                escenario.setIdEscenario(resultado[0])
        finally:
            cursor.close()
            sesion.cerrarConexion()
        return escenario

    def traerUltimoEscenario(self):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        resultado = None
        escenario = None
        try:
            idMax = cursor.execute("""select * from Escenario where idEscenario = (select min(idEscenario) Escenario)""")
            cursor.close()
            cursor = sesion.obtenerCursor()
            cursor.execute("""select * from Escenario where Escenario.idEscenario='%i'""" % idMax)
            resultado = cursor.fetchone()
            if resultado is not None:
                escenario = Escenario(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
                escenario.setIdEscenario(resultado[0])

        except:
            print("Error no se pudo traer los escenarios")
        finally:
            cursor.close()
            sesion.cerrarConexion()
        return escenario