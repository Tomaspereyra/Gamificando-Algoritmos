from negocio.EscenarioABM import EscenarioABM
from dao.EscenarioDao import EscenarioDao

def test_agregarEscenario():
    escenario = EscenarioABM()
    filasAfectadas = escenario.agregarEscenario(10, 5, "hint", "posibleSolucion", "descripcion", 1)
    assert filasAfectadas == 1

def test_traerUltimoEscenario():
    escenario = EscenarioDao()
    print (escenario.traerUltimoEscenario().getIdEscenario())

test_traerUltimoEscenario()