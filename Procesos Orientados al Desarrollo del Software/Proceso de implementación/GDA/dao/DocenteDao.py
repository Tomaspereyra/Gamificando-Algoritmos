import MySQLdb
from Conexion import Sesion
from datos.Docente import Docente
from dao.CursoDao import CursoDao


class DocenteDao:

    def iniciarOperacion(self):

        try:
            sesion = Sesion()  # iniciar sesion con la bd
        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def agregarDocente(self, idUsuario):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        resultado = 0
        try:
           resultado = cursor.execute("""insert into Docente(Usuario_idUsuario) 
           values('%i')""" % idUsuario)
           sesion.commit()
        except:
            print "Error en ejecucion de la query"
            sesion.getEstado().rollback()  # volver al estado anterior

        finally:
            cursor.close()
            sesion.cerrarConexion()
            return resultado

    def eliminar(self, docente):

        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        try:
            cursor.execute("""delete Docente from Docente where Docente.idDocente
            = '%i'""" % (docente.getIdDocente()))
            sesion.commit()
        except:
            print "Error no se pudo eliminar el docente"
            sesion.getEstado().rollback()
        finally:
            cursor.close()
            sesion.cerrarConexion()

    def traerDocente(self, idUsuario):
        sesion = self.iniciarOperacion()
        cursor = sesion.obtenerCursor()
        docente = None
        try:
            cursor.execute("""select * from Docente where Docente.Usuario_idUsuario='%i'""" % idUsuario)  # traigo el docente
            resultado = cursor.fetchone()
            if resultado is not None:  # pregunto si el docente existe
                cursor.execute("""select * from Usuario where Usuario.idUsuario='%i'""" % idUsuario)  # pido el usuario
                usuario = cursor.fetchone()
                cursoDao = CursoDao()
                lstCursos = cursoDao.traerCursosPorDocente(idUsuario)
                docente = Docente(usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6])
                docente.setIdUsuario(usuario[0])
                docente.setIdDocente(resultado[0])
                docente.agregarCursos(lstCursos)

        finally:
            cursor.close()
            sesion.cerrarConexion()

        return docente



