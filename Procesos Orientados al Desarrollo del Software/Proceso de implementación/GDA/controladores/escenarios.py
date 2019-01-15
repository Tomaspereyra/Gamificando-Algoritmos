# coding=utf-8
from __future__ import print_function
import datetime
from util.session_utils import *
import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, Flask
)
import traceback
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app as app

import sys

from util.errores import *
from negocio.CursoABM import CursoABM
from negocio.EscenarioABM import EscenarioABM
from negocio.CursoIniciadoABM import CursoIniciadoABM
from negocio.DocenteABM import DocenteABM
from negocio.EstudianteABM import EstudianteABM
from negocio.JuegoABM import JuegoABM
from negocio.EscenarioEnProcesoABM import EscenarioEnProcesoABM
from datos.Escenario import Escenario

cursoABM = CursoABM()
cursoIniciadoABM = CursoIniciadoABM()
escenarioEnProcesoABM = EscenarioEnProcesoABM()
escenarioABM = EscenarioABM()
docenteABM = DocenteABM()
juegoABM = JuegoABM()
estudianteABM = EstudianteABM()

bp = Blueprint('escenarios', __name__, url_prefix='/escenarios')


@bp.route('/crearEscenario', methods=('GET', 'POST'))
def crearEscenario():
    content = request.values
    print("Content : " + str(content), file=sys.stdout)
    user = getCurrentUser(session)
    bloquesPermitidos = content.get("bloquesPermitidos")
    cantidadDeBloques = content.get("cantidadDeBloques")
    hint = content.get("hint")
    descripcion = content.get("descripcion")
    posibleSolucion = content.get("posibleSolucion")
    idcurso = content.get("curso")
    try:

        escenarioABM.agregarEscenario(bloquesPermitidos, cantidadDeBloques, hint, posibleSolucion, descripcion, idcurso)
        curso = cursoABM.traerCurso(idcurso)

        return render_template("editarCurso.html", curso=curso, user=user)
    except Exception as e:
        print("Error encontrado : " + e.message, file=sys.stdout)
        return render_template("index.html", user=user)


@bp.route('/editarEscenario', methods=('GET', 'POST'))
def editarEscenario():
    content = request.values
    print("Content : " + str(content), file=sys.stdout)
    user = getCurrentUser(session)
    idEscenario = content.get("idEscenario")
    try:
        escenario = escenarioABM.traerEscenario(idEscenario)

        return render_template("editarEscenario.html", escenario=escenario, user=user)
    except Exception as e:
        print ("Error encontrado: " + e.message, file=sys.stdout)
        return render_template("index.html", user=user)

@bp.route('/actualizarEscenario',methods =('GET', 'POST'))
def actualizarEscenario():
    content = request.values
    print("Content : " + str(content), file=sys.stdout)
    user = getCurrentUser(session)
    idEscenario = content.get("idescenario")

    bloquesPermitidos = content.get("bloquesPermitidos")
    bloquesMax = content.get("bloquesMax")
    hint = content.get("hint")
    descripcion = content.get("descripcion")
    posibleSolucion = content.get("posibleSolucion")

    escenario = Escenario(bloquesPermitidos, bloquesMax, hint, posibleSolucion, descripcion)
    escenario.setIdEscenario(idEscenario)
    



    try:
        escenarioABM.actualizarEscenario(escenario)
        escenario = escenarioABM.traerEscenario(idEscenario)
        return render_template("editarEscenario.html", user = user, escenario=escenario)
    except Exception as e:
        print ("Error encontrado: "+ e.message, file=sys.stdout)
        return render_template("editarEscenario.html", user=user)



