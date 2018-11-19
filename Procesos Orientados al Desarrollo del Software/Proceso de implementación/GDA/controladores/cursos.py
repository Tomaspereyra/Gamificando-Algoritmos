# coding=utf-8
from __future__ import print_function

import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, Flask
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app as app

import sys

from util.errores import *
from negocio.CursoABM import CursoABM
from negocio.CursoIniciadoABM import CursoIniciadoABM

cursoABM = CursoABM()
cursoIniciadoABM = CursoIniciadoABM()

bp = Blueprint('cursos', __name__, url_prefix='/cursos')


@bp.route('/', methods=('GET', 'POST'))
def cursosGeneral():
    content = request.values
    user = content.get("username")
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    cursos = cursoABM.traerCursos()
    return render_template("verCursos.html", username=user, cursos=cursos)

@bp.route('/docente', methods=('GET', 'POST'))
def cursosDocente():
    content = request.values
    user = content.get("username")
    idDocente = content.get("idDocente")
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    cursos = cursoABM.traerCursosPorIdDocente(idDocente)
    return render_template("verCursos.html", username=user, cursos=cursos)

@bp.route('/estudiante', methods=('GET', 'POST'))
def cursosEstudiante():
    content = request.values
    user = content.get("username")
    idEstudiante = content.get("idEstudiante")
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    cursos = cursoIniciadoABM.traerCursosIniciadosPorIdEstudiante(idEstudiante)
    return render_template("verCursos.html", username=user, cursos=cursos)

@bp.route('/jugar', methods=('GET', 'POST'))
def jugarCurso():
    content = request.values
    user = content.get("username")
    idCurso = content.get("idCurso")
    cursos = cursoIniciadoABM.traerCurso(idCurso)
    #Ver si existe, si no crearlo y mandarselo a la vista
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    return render_template("verCursos.html", username=user, cursos=cursos)

@bp.route('/editar', methods=('GET', 'POST'))
def editarCurso():
    content = request.values
    user = content.get("username")
    idCurso = content.get("idCurso")
    cursos = cursoIniciadoABM.traerCurso(idCurso)
    #Ver si existe, si no crearlo y mandarselo a la vista
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    return render_template("verCursos.html", username=user, cursos=cursos)

@bp.route('/crear', methods=('GET', 'POST'))
def crearCurso():
    content = request.values
    user = content.get("username")
    sePuedeSaltear = bool(content.get("sePuedeSaltear"))
    nombre = content.get("nombre")
    descripcion = content.get("descripcion")
    descripcion = content.get("descripcion")
    idJuego = content.get("idJuego")
    docente = docenteABM.traerDocente(user)
    curso = cursoABM.agregarCurso(sePuedeSaltear, nombre, descripcion, docente, juego)
    #Ver si existe, si no crearlo y mandarselo a la vista
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    return render_template("verCursos.html", username=user, cursos=cursos)