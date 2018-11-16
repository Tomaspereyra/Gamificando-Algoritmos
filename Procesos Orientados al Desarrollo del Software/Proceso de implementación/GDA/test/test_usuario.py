from negocio.UsuarioABM import UsuarioABM
from datos.Usuario import Usuario


def test_agregarUsuario():
    usuario = UsuarioABM()
    u = usuario.registrarUsuario("username", "password", "email", "nombre", "apellido", "1998/05/01")
    assert u == 1


def test_traerUsuario():
    usuario = UsuarioABM()
    u = usuario.traerUsuario("username")
    assert u.getUsername() == "username"


def test_editarUsuario():
    usuario = UsuarioABM()
    usuarioExistente = usuario.traerUsuario("username")
    nuevoUsuario = Usuario("tomas", "password", "email", "nombre", "apellido", "1998/05/01")
    usuario.editarUsuario(usuarioExistente , nuevoUsuario)
    usuarioModificado = usuario.traerUsuario("tomas")

    assert usuarioModificado.getUsername() == "tomas"