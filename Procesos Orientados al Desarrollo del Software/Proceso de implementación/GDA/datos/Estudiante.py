import Usuario


class Estudiante(Usuario.Usuario):
    def __init__(self, username, password, email, nombre, apellido):
        Usuario.Usuario.__init__(self, username, password, email, nombre, apellido)
        self.cursosIniciados = []

    def agregarCursos(self, cursos):
        self.cursosIniciados.append(cursos)

    def getCursosIniciados(self):
        return self.cursosIniciados

    def getIdEstudiante(self):
        return self.getId()
