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
        return str(self.getNombre())
