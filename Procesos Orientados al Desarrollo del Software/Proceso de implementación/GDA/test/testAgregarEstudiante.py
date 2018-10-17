from negocio.EstudianteABM import EstudianteABM


class TestAgregarEstudiante:

    def __init__(self):
        pass

    def agregarEstudiante(self, username, password, email, nombre, apellido, fechaNacimiento):
        estudianteabm = EstudianteABM()
        print estudianteabm.agregarEstudiante(username, password, email, nombre, apellido, fechaNacimiento)


test = TestAgregarEstudiante()

test.agregarEstudiante("User", "Pass", "email", "nombre", "apellido", "2018-10-16")  # cambiar el nombre de usuario
# para seguir agregando
