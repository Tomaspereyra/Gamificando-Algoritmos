from __future__ import print_function
import json
from util.session_utils import  *
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, Flask
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app as app

import sys

from util.errores import *
from negocio.UsuarioABM import UsuarioABM

usuarioABM = UsuarioABM()
bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/', methods=('GET', 'POST'))
def goHome():
    content = request.values
    print ("Content : " + str(content), file=sys.stdout)

    print('/home -> POST/GET() - User : ' + str(getCurrentUser(session)), file=sys.stdout)

    print(' -> POST/GET()', file=sys.stdout)
    return render_template("index.html", user=getCurrentUser(session))

@bp.before_request
def beforeRequest():
    updateCurrentUser(session)

