from datos.Usuario import Usuario


class Docente(Usuario):

    def __init__(self, username, password, email, nombre, apellido, fechaNacimiento):
        Usuario.__init__(self, username, password, email, nombre, apellido, fechaNacimiento)
        self.idDocente=0
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
        return str("ID Usuario: "+str(self.getId())+" Nombre de usuario: " + self.getUsername()+" Email: " +
                   self.getEmail()+ " Nombre: " + self.getNombre() + " Apellido: "+ self.getApellido() +
                   " Fecha Nacimiento: " + str(self.getFechaNacimiento()) + str(self.imprimirLista()))

    def imprimirLista(self):
        return ''.join('\n'.join(map(str, sl)) for sl in self.getCursosCreados())


