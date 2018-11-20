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

usuarioABM = UsuarioABM()

bp = Blueprint('miCuenta', __name__, url_prefix='/miCuenta')

@bp.route('/', methods=('GET', 'POST'))
def myAccount():
    try:
        content = request.values
        print ("/miCuenta() -> Content : " + str(content), file=sys.stdout)
        print ("Username global : " + str(getCurrentUser(session)), file=sys.stdout)
        try:
            username = getCurrentUser(session)
            user = usuarioABM.traerUsuario(username)
        except:
            username = None
            user = None
        print ("User : " + str(user), file=sys.stdout)
        return render_template("myAccount.html", userObj=user, user=username)
    except Exception as e:
        print("ERROR : " + e.message)
