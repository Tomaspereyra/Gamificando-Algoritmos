import MySQLdb
from Conexion import Sesion
from dao.EscenarioDao import EscenarioDao
from datos.Curso import Curso
from dao.JuegoDao import JuegoDao


class CursoDao:

    def iniciarOperacion(self):

        try:
            sesion = Sesion()  # iniciar sesion con la bd
        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def agregar(self, sePuedeSaltear, nombre, descripcion, idDocente, juego):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        resultado = 0
        try:
            resultado = cursor.execute("""insert into Curso (sePuedeSaltear,nombre,descripcion, docente_idDocente, Juego_idJuego)
             values('%i', '%s','%s', '%i','%i')""" % (sePuedeSaltear, nombre, descripcion, idDocente, juego.getId()))
            sesion.commit()
        finally:
            cursor.close()
            sesion.cerrarConexion()
            return resultado


    def eliminar(self, curso):

        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""delete Curso from Curso where Curso.idCurso 
            = '%i'""" % (curso.getIdCurso()))
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
        curso = Curso(False, "-", "-", "-")
        escenario = EscenarioDao()
        try:
            cursor.execute("""select * from Curso where Curso.idCurso = '%i'""" % idCurso)
            resultado = cursor.fetchone()
            if resultado is not None:
                juego = JuegoDao()
                curso = Curso(resultado[1], resultado[2], juego.traerJuegoPorId(resultado[5]), resultado[3])
                curso.setIdCurso(resultado[0])
                curso.setListaEscenario(escenario.traerEscenariosPorCurso(curso.getIdCurso()))

        finally:
            cursor.close()
            sesion.cerrarConexion()
            return curso

    def traerCursosPorDocente(self, idDocente):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        lstCursos = []
        curso = Curso()
        escenario = EscenarioDao()
        try:
            cursor.execute("""select * from Curso where Curso.Docente_idDocente='%i'""" % idDocente)
            resultado = cursor.fetchall()
            for fila in range(len(resultado)):
                for columna in range(len(resultado[fila])):
                    if columna == 0:
                        curso.setIdCurso(resultado[fila][columna])

                    if columna == 1:
                        curso.setPuedeSaltear(resultado[fila][columna])
                    if columna == 2:
                        curso.setNombre(resultado[fila][columna])
                    if columna == 3:
                        curso.setDescripcion(resultado[fila][columna])
                        curso.setListaEscenario(escenario.traerEscenariosPorCurso(curso.getIdCurso()))
                    if columna == 5:
                        juego = JuegoDao()
                        curso.setJuego(juego.traerJuegoPorId(resultado[fila][columna]))
                        lstCursos.append(curso)
                        curso = Curso()  # creo una nueva instancia por que se maneja
                        #  por referencia, si no, se pisan en la lista.
        finally:
            cursor.close()
            sesion.cerrarConexion()

        return lstCursos



