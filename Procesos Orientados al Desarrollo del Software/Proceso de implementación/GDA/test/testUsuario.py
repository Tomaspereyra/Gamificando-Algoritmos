from dao.UsuarioDao import UsuarioDao
from datos.Usuario import Usuario


class testUsuario:

    usuario = UsuarioDao()
    user = usuario.traerUsuario('tomas')
    print user


