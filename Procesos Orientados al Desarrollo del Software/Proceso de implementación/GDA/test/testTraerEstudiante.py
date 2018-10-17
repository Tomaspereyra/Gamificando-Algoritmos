from negocio.EstudianteABM import EstudianteABM


class TestTraerEstudiante:

    def __init__(self):
        pass

    def traerEstudiante(self, username):
        estudianteabm = EstudianteABM()

        return estudianteabm.traerEstudiante(username)


test = TestTraerEstudiante()

print test.traerEstudiante("User")
