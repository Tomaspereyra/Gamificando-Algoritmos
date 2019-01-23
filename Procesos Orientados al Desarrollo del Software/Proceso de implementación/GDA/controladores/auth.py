from __future__ import print_function
import json
from util.session_utils import *
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

usuarioABM = UsuarioABM()
docenteABM = DocenteABM()
estudianteABM = EstudianteABM()

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/', methods=('GET', 'POST'))
def enter():
    return render_template("loginRegister.html")

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        try:
            print('/register -> POST()', file=sys.stdout)
            content            = request.values
            username = content.get('username')
            password = content.get('password')
            mail = content.get('email')
            nombre = content.get('nombre')
            apellido = content.get('apellido')
            fechaNacimiento = content.get('fechaNacimiento')
            esDocente = bool(content.get('esDocente'))

            error = None

            if not username:
                error = 'Username is required.'
            elif not password:
                error = 'Password is required.'
            elif usuarioABM.traerUsuario(username) is not None:
                error = 'User {} is already registered.'.format(username)

            if error is None:
                if esDocente:
                    docenteABM.registrarDocente(username, password, mail, nombre, apellido, fechaNacimiento)
                else:
                    estudianteABM.agregarEstudiante(username, password, mail, nombre, apellido, fechaNacimiento)
                return render_template("index.html", user=username)
            else:
                return render_template("loginRegister.html", error=error)
        except:
            return render_template("loginRegister.html", error="Hubo un error")

@bp.route('/login', methods=('GET', 'POST'))
def login():
    error = None
    #print('Req : ' + str(request))
    content = request.values
    #print('Content  : ' + str(content))
    print('/login -> ' + request.method, file=sys.stdout)
    try:


        user = usuarioABM.traerUsuario(content['username'])
        #print('Pre-Validacion', file=sys.stdout)

        if user is None:
            error = 'Incorrect username.'
        elif not content['password'] == user.password:
            error = 'Incorrect password.'

        #print('Error : ' + str(error), file=sys.stdout)

        if error is None:

            session.clear()
            session['user_id'] = content['username']
            data = {
                "loged_in_user": content['username'],
                "loged_in_password": content['password']
            }

            return render_template("index.html", user=user.username)
        else:
            return render_template("loginRegister.html", error=error)

    except Exception as e:
        print('Error found : ' + str(e.message), file=sys.stdout)
        return render_template("loginRegister.html", error="Hubo un error")


@bp.route('/test', methods=('GET', 'POST'))
def test():
    if request.method == 'POST':
        username = request.form['username']
        error = None

        if usuarioABM.traerUsuario(username).idUsuario == session['user_id']:
            error = "Logged in as" + str(session['user_id'])
        else:
            error = 'You are not logged in'

        flash(error)

    return jsonify(error)

@bp.route('/logout')
def logout():
    print (str(session['user_id']))
    session.clear()
    return render_template("index.html")


