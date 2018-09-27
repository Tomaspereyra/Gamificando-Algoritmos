from datos.Usuario import Usuario


class Docente(Usuario):

    def __init__(self, username, password, email, nombre, apellido):
        Usuario.__init__(self, username, password, email, nombre, apellido)
        self.cursosCreados =[]

    def agregarCursos(self, curso):
       self.cursosCreados.append(curso)

    def getCursosCreados(self):
        return self.cursosCreados

    def setIdDocente(self, id):
        self.idDocente=id

    def getIdDocente(self):
        return self.idDocente

    def __str__(self):
        print "Datos Usuario: ", self.getUsername(), self.getNombre()
        print self.getCursosCreados()

docente = Docente("tomas", "ppp", "uuu", "eee", "ee")