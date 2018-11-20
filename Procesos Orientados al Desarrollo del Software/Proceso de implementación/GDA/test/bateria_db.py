from negocio.CursoIniciadoABM import CursoIniciadoABM
from negocio.EstudianteABM import EstudianteABM
from negocio.UsuarioABM import UsuarioABM
from negocio.CursoABM import CursoABM
from negocio.EscenarioABM import EscenarioABM
from negocio.DocenteABM import DocenteABM
from negocio.JuegoABM import JuegoABM
from negocio.EscenarioLaberintoABM import EscenarioLaberintoABM
def bateria_Prueaba():
    cursoIniciadoABM = CursoIniciadoABM()
    estudianteABM = EstudianteABM()
    usuarioABM = UsuarioABM()
    cursoAbm = CursoABM()
    escenarioABM = EscenarioABM()
    docenteABM = DocenteABM()
    juegoABM = JuegoABM()
    escenarioLaberintoABM = EscenarioLaberintoABM()

    for x in range(1, 6):
        docenteABM.registrarDocente("usuario"+str(x),"password", "usuario"+str(x)+"@mail.com", "nombre"+str(x), "apellido"+str(x), "29/9/2018")
    for x in range(6, 11):
        estudianteABM.agregarEstudiante("usuario"+str(x),"password", "usuario"+str(x)+"@mail.com", "nombre"+str(x), "apellido"+str(x), "29/9/2018")
    for x in range (1, 3):
        juegoABM.agregarJuego("juego"+str(x), "DecripcionJuego"+str(x))
    for x in range (1,3):
        cursoAbm.agregarCurso(True, "Curso"+str(x), "DescripcionCurso"+str(x), docenteABM.traerDocente("usuario"+str(x)), juegoABM.traerJuego("juego1"))
    cursoIniciadoABM.comenzarCurso(estudianteABM.traerEstudiante("usuario6"),cursoAbm.traerCurso(1))
    escenarioLaberintoABM.agregarEscenarioLaberinto(10, 5, "hint", "posibleSolucion", "descripcion", 1,"1111111111111111111")

def bateria_prueba_traer():
    cursoIniciadoABM = CursoIniciadoABM()
    estudianteABM = EstudianteABM()
    usuarioABM = UsuarioABM()
    cursoAbm = CursoABM()
    escenarioABM = EscenarioABM()
    docenteABM = DocenteABM()
    juegoABM = JuegoABM()
    escenarioLaberintoABM = EscenarioLaberintoABM()
    docenteABM.registrarDocente("docente", "password", "usuario@mail.com", "docente", "apellido", "29/9/2018")
    estudianteABM.agregarEstudiante("estudiante", "password", "usuario@mail.com", "estudiante", "apellido", "29/9/2018")
    juegoABM.agregarJuego("juego", "DecripcionJuego")
    cursoAbm.agregarCurso(True, "nombreCurso", "DescripcionCurso",docenteABM.traerDocente("docente"), juegoABM.traerJuego("juego"))
    cursoIniciadoABM.comenzarCurso(estudianteABM.traerEstudiante("estudiante"), cursoAbm.traerCurso(1))

bateria_prueba_traer()


