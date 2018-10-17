from datos.Usuario import Usuario


class Estudiante(Usuario):
    def __init__(self, username="-", password="-", email="-", nombre="-", apellido="-", fechaNacimiento=0):
        Usuario.__init__(self, username, password, email, nombre, apellido, fechaNacimiento)
        self.cursosIniciados = []

    def agregarCursos(self, cursos):
        self.cursosIniciados.append(cursos)

    def getCursosIniciados(self):
        return self.cursosIniciados

    def setIdEstudiante(self, idEstudiante):
        self.idEstudiante = idEstudiante

    def getIdEstudiante(self):
        return self.idEstudiante

    def __str__(self):
        return str("ID estudiante: " + str(self.getId()) + " Nombre de usuario: " + self.getUsername() + " Email: " +
                   self.getEmail() + " Nombre :" + self.getNombre() + " Apellido: " + self.getApellido() +
                   " CursosIniciados: \n" + str(self.imprimirLista()))

    def imprimirLista(self):
        return ''.join('\n'.join(map(str, sl)) for sl in self.getCursosIniciados())

