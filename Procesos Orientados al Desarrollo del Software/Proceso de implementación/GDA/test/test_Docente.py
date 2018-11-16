from negocio.DocenteABM import DocenteABM


def test_agregarDocente():
    docente = DocenteABM()
    filasAfectadas = docente.registrarDocente("Profee", "Pass", "email", "nombre", "apellido", "2018-10-16")
    assert filasAfectadas == 1


def test_traerDocente():
    docente = DocenteABM()
    d = docente.traerDocente("Profee")
    assert d.getUsername() == "Profee"

