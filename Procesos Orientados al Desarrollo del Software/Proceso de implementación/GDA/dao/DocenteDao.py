import MySQLdb
from Conexion import Sesion
from datos import Docente

class DocenteDao:
    def iniciarOperacion(self):

        try:
            sesion = Sesion()  # iniciar sesion con la bd
        except MySQLdb.OperationalError:
            print "Error en la conexion"
            sesion = None

        return sesion

    def agregarDocente(self, docente):
        sesion= self.iniciarOperacion()
        cursor= sesion.obtenerCursor()
        try:
           cursor.execute("""insert into Docente(Usuario_idUsuario) 
           values('%i')""" % (docente.getId()))
           sesion.commit()
        except:
           print "Error en ejecucion de la query"
           sesion.getEstado().rollback()  # volver al estado anterior

        finally:
            cursor.close()
            sesion.cerrarConexion()

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

docente = Docente.Docente("tomas", "ppp", "uuu", "eee", "ee")
docente.setIdUsuario(1)
docenteDao = DocenteDao()

docenteDao.agregarDocente(docente)