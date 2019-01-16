from __future__ import print_function
# coding=utf-8
from util.session_utils import *
import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, Flask
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app as app

import sys

from util.errores import *
from negocio.UsuarioABM import UsuarioABM
from negocio.DocenteABM import DocenteABM
from negocio.EstudianteABM import EstudianteABM
from negocio.CursoABM import CursoABM
from datos.Docente import Docente
from datos.Usuario import Usuario

usuarioABM = UsuarioABM()
docenteABM = DocenteABM()
estudianteABM = EstudianteABM()
cursoABM = CursoABM()

bp = Blueprint('miCuenta', __name__, url_prefix='/miCuenta')


@bp.route('/', methods=('GET', 'POST'))
def myAccount():
    try:
        content = request.values
        print("/miCuenta() -> Content : " + str(content), file=sys.stdout)
        print("Username global : " + str(getCurrentUser(session)), file=sys.stdout)
        try:
            username = getCurrentUser(session)
            estudianteProfesor = docenteABM.traerDocente(username)

            if estudianteProfesor is not None:
                cursos = cursoABM.traerCursosPorIdDocente(estudianteProfesor.getIdDocente())
                print(str(cursos.__len__()), file=sys.stdout)
                return render_template("miCuentaDocente.html", docente=estudianteProfesor, user=username, cursos=cursos)
            else:
                estudianteProfesor = estudianteABM.traerEstudiante(username)
                return render_template("miCuentaEstudiante.html", estudiante=estudianteProfesor, user=username)
        except:
            username = None
            user = None
            print("User : " + str(user), file=sys.stdout)
            return render_template("miCuentaEstudiante.html", userObj=user, user=username)
    except Exception as e:
        print("ERROR : " + e.message)


@bp.route('/editarCuenta', methods=('GET', 'POST'))
def editarCuenta():
    content = request.values
    user = getCurrentUser(session)
    idUsuario = content.get('idusuario')
    username = content.get('username')
    contrasena = content.get('contrasena')
    email = content.get('email')
    nombre = content.get('nombre')
    apellido = content.get('apellido')
    fechaNacimiento = content.get('fechaNacimiento')
    usuario = Usuario(username, contrasena, email, nombre, apellido, fechaNacimiento)


    try:
        usuarioViejo = usuarioABM.traerUsuarioPorId(idUsuario)
        usuarioABM.editarUsuario(usuarioViejo.getUsername(), usuario)
        docente = docenteABM.traerDocente(username)
        if docente is not None:
            cursos = cursoABM.traerCursosPorIdDocente(docente.getIdDocente())
            return render_template("MiCuentaDocente.html", user=user, docente=docente, cursos=cursos)
        else:
            estudiante = estudianteABM.traerEstudiante(username)
            return render_template("MiCuentaEstudiante.html", user=user, estudiante=estudiante)
    except Exception as e:
        print("Error : " + e.message)
        docente = docenteABM.traerDocente(username)
        return render_template("MiCuentaDocente.html", user=user, docente=docente)

@bp.route ('/cambiarContrasena', methods=('GET','POST'))
def cambiarContrasena():
    content = request.values
    user = getCurrentUser(session)
    contrasenaActual = content.get('contrasenaActual')
    id = content.get('idusuario')
    contrasenaNueva = content.get('contrasenaNueva')
    confirmacion = content.get('contrasenaConfirmacion')
    error = None
    estudiante = estudianteABM.traerEstudiante(user)
    try:
        if not contrasenaActual:
            error = "Ingrese Contrasena actual"
        elif not contrasenaNueva:
            error = "Ingrese Contrasena nueva"
        elif not confirmacion:
            error = "Repita la nueva contrasena"

        if error is None:
            usuario = usuarioABM.traerUsuarioPorId(id)
            if contrasenaActual == usuario.getPassword():
                if contrasenaNueva == confirmacion:
                    usuario.setPassword(contrasenaNueva)
                    usuarioABM.editarUsuario(usuario.getUsername(), usuario)
                else:
                    error = "La contrasena nueva no coincide"
            else:
                error = "Contrasena incorrecta"
        if estudiante is not None:
           return render_template("MiCuentaEstudiante.html", error=error, user=user, estudiante=estudiante)
        else:
            docente = docenteABM.traerDocente(user)
            return render_template("MiCuentaDocente.html", error=error, user=user, docente=docente)
    except Exception as e:
        print("Error : "+ e.message,file=sys.stdout)
        return render_template("MiCuentaEstudiante.html", error=error, user=user, estudiante=estudiante)




