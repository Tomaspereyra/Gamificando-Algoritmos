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

cursoABM = CursoABM()
cursoIniciadoABM = CursoIniciadoABM()
escenarioEnProcesoABM = EscenarioEnProcesoABM()
escenarioABM = EscenarioABM()
docenteABM = DocenteABM()
juegoABM = JuegoABM()
estudianteABM = EstudianteABM()

bp = Blueprint('escenarios', __name__, url_prefix='/escenarios')


@bp.route('/', methods=('GET', 'POST'))
def cursosGeneral():
    content = request.values

    user = getCurrentUser(session)
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    cursos = cursoABM.traerCursos()
    return render_template("verCursos.html", user=user, cursos=cursos)

@bp.route('/docente', methods=('GET', 'POST'))
def cursosDocente():
    content = request.values
    user = getCurrentUser(session)
    idDocente = content.get("idDocente")
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    cursos = cursoABM.traerCursosPorIdDocente(idDocente)
    return render_template("verCursos.html", user=user, cursos=cursos)

@bp.route('/estudiante', methods=('GET', 'POST'))
def cursosEstudiante():
    content = request.values
    user = getCurrentUser(session)
    idEstudiante = content.get("idEstudiante")
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    cursos = cursoIniciadoABM.traerCursosIniciadosPorIdEstudiante(idEstudiante)
    return render_template("verCursos.html", user=user, cursos=cursos)

@bp.route('/jugar', methods=('GET', 'POST'))
def jugarCurso():

    content = request.values
    user = getCurrentUser(session)
    print("Content : " + str(content), file=sys.stdout)
    idCurso = content.get("idCurso")
    try:
        estudiante = estudianteABM.traerEstudiante(user)
        if not estudiante:
            print("Error : Estudiante " + str(user) + " no existe ", file=sys.stdout)
            return render_template("index.html", user=user)
        curso = cursoABM.traerCurso(idCurso)
        cursoIniciado = cursoIniciadoABM.traerCursoIniciado(estudiante, curso)
        #Ver si existe, si no crearlo y mandarselo a la vista
        if not cursoIniciado:
            #Creamos
            now = datetime.datetime.now()
            print("Creando cursoIniciado... ", file=sys.stdout)
            cursoIniciadoABM.comenzarCurso(estudiante, curso)
            cursoIniciado = cursoIniciadoABM.traerCursoIniciado(estudiante, curso)
            for e in curso.escenario:
                print("Escenario : " + str(e), file=sys .stdout)
                escenarioEnProcesoABM.comenzarEscenario(now, e.idEscenario, cursoIniciado.idCursoIniciado)
            cursoIniciado = cursoIniciadoABM.traerCursoIniciado(estudiante, curso)  # Traemos de vuelta para actualizar escenarios
            print("Creado : " + str(cursoIniciado), file=sys.stdout)
        else:
            print("Curso Iniciado existe : " + str(cursoIniciado), file=sys.stdout)
        return render_template("escenariosEnCurso.html", user=user, curso=cursoIniciado, nombreCurso=curso.nombre)
    except Exception as e:
        print("Error encontrado : " + repr(e) + " - " + e.message , file=sys.stdout)
        traceback.print_exc()
        return render_template("index.html", user=user)

@bp.route('/editar', methods=('GET', 'POST'))
def editarCurso():
    content = request.values
    user = getCurrentUser(session)
    idCurso = content.get("idCurso")
    cursos = cursoIniciadoABM.traerCurso(idCurso)
    #Ver si existe, si no crearlo y mandarselo a la vista
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    return render_template("verCursos.html", user=user, curso=curso)

@bp.route('/crear', methods=('GET', 'POST'))
def crearCurso():

    content = request.values
    print("Content : " + str(content), file=sys.stdout)
    user = getCurrentUser(session)
    sePuedeSaltear = bool(content.get("sePuedeSaltear"))
    nombre = content.get("nombre")
    descripcion = content.get("descripcion")
    descripcion = content.get("descripcion")
    idJuego = content.get("idJuego")
    try:
        docente = docenteABM.traerDocente(user)
        curso = cursoABM.agregarCurso(sePuedeSaltear, nombre, descripcion, docente, juegoABM.traerJuego(idJuego))
        #Ver si existe, si no crearlo y mandarselo a la vista
        return render_template("editarCurso.html", user=user, curso=curso)
    except Exception as e:
        print("Error encontrado : " + e.message, file=sys.stdout)
        return render_template("index.html", user=user)
