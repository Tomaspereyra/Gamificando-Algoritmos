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

bp = Blueprint('maze', __name__, url_prefix='/maze')


@bp.route('/', methods=('GET', 'POST'))
def enter():
    return render_template("JugarLaberinto.html")