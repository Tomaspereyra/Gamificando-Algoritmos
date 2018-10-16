from negocio.DocenteABM import DocenteABM


class TestTraerDocente:
    def __init__(self):
        pass

    def traerDocente(self, username):
        docenteabm = DocenteABM()

        return docenteabm.traerDocente(username)


test = TestTraerDocente()
docente = test.traerDocente("Profe")

print docente
