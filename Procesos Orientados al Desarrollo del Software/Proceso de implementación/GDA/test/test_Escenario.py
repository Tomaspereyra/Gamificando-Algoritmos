from negocio.EscenarioABM import EscenarioABM


def test_agregarEscenario():
    escenario = EscenarioABM()
    filasAfectadas = escenario.agregarEscenario(10, 5, "hint", "posibleSolucion", "descripcion", 1)
    assert filasAfectadas == 1

