from dao.UsuarioDao import UsuarioDao
from datos.Usuario import Usuario


class testUsuario:

    usuario = UsuarioDao()
    user = Usuario("us", "pass", "email", "nombre", "apellido", "29/9/2018")
    usuario.agregar(user)



