from __future__ import print_function
import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, Flask
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app as app

import sys

from util.errores import *
from negocio.UsuarioABM import UsuarioABM

usuarioABM = UsuarioABM()
bp = Blueprint('auth', __name__, url_prefix='/auth')



@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        print('/register -> POST()', file=sys.stdout)
        content = request.args
        username = content.get('username')
        password = content.get('password')
        mail = content.get('email')
        nombre = content.get('nombre')
        apellido = content.get('apellido')
        fechaNacimiento = content.get('fechaNacimiento')
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif usuarioABM.traerUsuario(username) is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            usuarioABM.registrarUsuario(username, password, mail, nombre, apellido, fechaNacimiento)
            print('Response data : ' + username + " pw:" + password, file=sys.stdout)
            data = {
                "loged_in_user" : username,
                "loged_in_password" : password
            }
            return createResponseAsJSON(data)
        else:
            return crearError(-2, error)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    error = None
    if request.method == 'POST':
        print('/login -> POST()', file=sys.stdout)
        content = request.args

        user = usuarioABM.traerUsuario(content['username'])
        #print('Pre-Validacion', file=sys.stdout)
        if user is None:
            error = 'Incorrect username.'
        elif not content['password'] == user.password:
            error = 'Incorrect password.'

        print('Error : ' + str(error), file=sys.stdout)

        if error is None:

            session.clear()
            session['user_id'] = content['username']
            data = {
                    "loged_in_user": content['username'],
                    "loged_in_password": content['password']
            }

            return createResponseAsJSON(data)
        else:
            return createResponseAsJSON(crearError(-1, error))
    else:
        print('/register -> No Post!!', file=sys.stdout)

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
    return str(session)
