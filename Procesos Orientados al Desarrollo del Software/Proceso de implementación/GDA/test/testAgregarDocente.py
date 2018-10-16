from negocio.DocenteABM import DocenteABM


class TestAgregarDocente:

    def __init__(self):
        pass

    def agregarDocente(self, username, password, email, nombre, apellido, fechaNacimiento):
        docenteabm = DocenteABM()
        print docenteabm.registrarDocente(username, password, email, nombre, apellido, fechaNacimiento)


test = TestAgregarDocente()

test.agregarDocente("Profe", "Pass", "email", "nombre", "apellido", "2018-10-16")
