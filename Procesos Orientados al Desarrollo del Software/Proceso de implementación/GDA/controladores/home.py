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
bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/', methods=('GET', 'POST'))
def goHome():
    content = request.args
    print ("Content : " + str(content), file=sys.stdout)
    user = content.get("username")
    print ("User : " + str(user), file=sys.stdout)
    print('/home -> POST/GET() - User : ' + str(user), file=sys.stdout)

    print(' -> POST/GET()', file=sys.stdout)
    return render_template("index.html", username=user)



@bp.route('/explorarCursos', methods=('GET', 'POST'))
def goToExplore():

    print('/explorarCursos -> POST/GET()', file=sys.stdout)
    return render_template("exploreGames.html")


