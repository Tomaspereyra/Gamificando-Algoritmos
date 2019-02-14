# coding=utf-8
from __future__ import print_function
import datetime
from util.session_utils import *
import json
from util.errores import *
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

bp = Blueprint('cursos', __name__, url_prefix='/cursos')

#Cursos general : Todos los cursos sin filtro
@bp.route('/', methods=('GET', 'POST'))
def cursosGeneral():
    content = request.values

    user = getCurrentUser(session)
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    cursos = cursoABM.traerCursos()
    return render_template("verCursos.html", user=user, cursos=cursos)

@bp.route('/misCursos', methods=('GET', 'POST'))
def misCursos():
    user = getCurrentUser(session)
    docente = docenteABM.traerDocente(user)
    if docente:
        return cursosDocente()
    else:
        return cursosEstudiante()


@bp.route('/docente', methods=('GET', 'POST'))
def cursosDocente():
    content = request.values
    user = getCurrentUser(session)
    docente = docenteABM.traerDocente(user)
    idDocente = docente.idDocente
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    cursos = cursoABM.traerCursosPorIdDocente(idDocente)
    juegos = juegoABM.traerJuegos()


    return render_template("verCursos.html", user=user, cursos=cursos, docente=True, juegos = juegos)

@bp.route('/estudiante', methods=('GET', 'POST'))
def cursosEstudiante():
    content = request.values
    user = getCurrentUser(session)
    estudiante = estudianteABM.traerEstudiante(user)
    idEstudiante = estudiante.idEstudiante
    print('/cursos -> POST/GET() - User : ' + str(user), file=sys.stdout)
    print("Content : " + str(content), file=sys.stdout)
    cursosIniciados = cursoIniciadoABM.traerCursosIniciadosPorIdEstudiante(idEstudiante)
    cursos = []
    for cursoIniciado in cursosIniciados:
        cursos.append(cursoIniciado.curso)
    return render_template("verCursos.html", user=user, cursos=cursos, Docente=False)

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

@bp.route('/guardarInfoCurso', methods=('GET', 'POST'))
def guardarInfoCurso():
    content = request.values
    user = getCurrentUser(session)

    try:
        idCurso = int(content.get("idCurso"))
        nombre = content.get("nombre")
        descripcion = content.get("descripcion")
        sePuedeSaltar = content.get("sePuedeSaltear")
        fechaCreacion = content.get("fecha")
        if sePuedeSaltar == "on":
            sePuedeSaltar = 1
        else:
            sePuedeSaltar = 0
        curso = cursoABM.traerCurso(idCurso)
        curso.setNombre(nombre)
        curso.setDescripcion(descripcion)
        curso.setPuedeSaltear(sePuedeSaltar)
        curso.setFechaCreacion(fechaCreacion)
        cursoABM.actualizarCurso(curso)
        data = {
            "success": True
        }
        return createResponseAsJSON(data)
    except Exception as e:
        print("Error encontrado : " + repr(e) + " - " + e.message, file=sys.stdout)
        traceback.print_exc()
        return crearError(-1, "Error al procesar solicitud!")

@bp.route('/guardarInfoEscenario', methods=('GET', 'POST'))
def guardarInfoEscenario():
    content = request.values
    user = getCurrentUser(session)

    try:
        idEscenario= int(content.get("idEscenario"))
        descripcion = content.get("descripcion")
        hint = content.get("hint")
        cantMaxBloques= int(content.get("cantMaxBloques"))
        escenario = escenarioABM.traerEscenario(idEscenario)
        escenario.setDescripcion(descripcion=descripcion)
        escenario.setHint(hint)
        escenario.setCantBloquesMax(cantMaxBloques)
        escenarioABM.actualizarEscenario(escenario)
        data = {
            "success": True
        }
        return createResponseAsJSON(data)
    except Exception as e:
        print("Error encontrado : " + repr(e) + " - " + e.message, file=sys.stdout)
        traceback.print_exc()
        return crearError(-1, "Error al procesar solicitud!")


@bp.route('/editar', methods=('GET', 'POST'))
def editarCurso():
    content = request.values
    user = getCurrentUser(session)
    try:
        idCurso = content.get("idCurso")
        curso = cursoABM.traerCurso(idCurso)
        return render_template("editarCurso.html", user=user, curso=curso)
    except Exception as e:
        print("Error encontrado : " + repr(e) + " - " + e.message, file=sys.stdout)
        traceback.print_exc()
        return render_template("index.html", user=user)

@bp.route('/agregarEscenario', methods=('GET', 'POST'))
def agregarEscenario():

    content = request.values
    user = getCurrentUser(session)
    try:
        idCurso = content.get("idCurso")
        escenarioABM.agregarEscenario("", 0, "", "", "Nuevo Escenario", idCurso)
        curso = cursoABM.traerCurso(idCurso)
        return render_template("editarCurso.html", user=user, curso=curso)
    except Exception as e:
        print("Error encontrado : " + e.message, file=sys.stdout)
        return render_template("editarCurso.html", user=user, curso=curso)

@bp.route('/jugarEscenario', methods=('GET', 'POST'))
def jugarEscenario():
    content = request.values
    user = getCurrentUser(session)
    idEscenario = content.get("idEscenario")
    escenario = escenarioABM.traerEscenario(idEscenario)
    if escenario:
        return render_template("jugarEscenario.html", user=user, curso=curso)
    else:
        return render_template("verCursos.html", user=user, curso=curso)

@bp.route('/agregarCurso', methods=('GET', 'POST'))
def crearCurso():

    content = request.values
    print("Content : " + str(content), file=sys.stdout)
    user = getCurrentUser(session)
    sePuedeSaltear = bool(content.get("sePuedeSaltear"))
    nombre = content.get("nombre")

    descripcion = content.get("descripcion")
    idJuego = content.get("juego")
    fechaCreacion = content.get("fecha")

    print ("id"+ idJuego,file=sys.stdout)
    try:
        docente = docenteABM.traerDocente(user)
        curso = cursoABM.agregarCurso(sePuedeSaltear, nombre, descripcion, docente, juegoABM.traerJuegoPorId(idJuego),fechaCreacion)
        #Ver si existe, si no crearlo y mandarselo a la vista
        return render_template("editarCurso.html", user=user, curso=curso)
    except Exception as e:
        print("Error encontrado : " + e.message, file=sys.stdout)
        return render_template("index.html", user=user)

@bp.route('/eliminarCurso', methods=('GET','POST'))
def eliminar():
    content = request.values
    print ("Content: " + str(content), file= sys.stdout)
    user = getCurrentUser(session)
    id = content.get("idcurso")
    error = None
    try:
        error = cursoABM.eliminar(id)
        docente = docenteABM.traerDocente(user)
        cursos = cursoABM.traerCursosPorIdDocente(docente.getIdDocente())
        error = " Curso Eliminado"
        return render_template("verCursos.html", user=user, error=error, cursos=cursos, docente = docente)
    except Exception as e:
        print ("Error encontrado : "+  e.message, file = sys.stdout)
        error = "El curso no pudo eliminar"
        curso = cursoABM.traerCurso(id)
        return render_template("editarCurso.html",user=user, error = error,curso=curso)
