from negocio.EstudianteABM import EstudianteABM


def test_agregarEstudiante():
    estudiante = EstudianteABM()
    e = estudiante.agregarEstudiante("tomas", "password", "email", "nombre", "apellido", "1998/05/01")
    assert e == 1


def test_traerEstudiante():
    estudiante = EstudianteABM()
    e = estudiante.traerEstudiante("tomas")
    assert e.getUsername() == "tomas"
