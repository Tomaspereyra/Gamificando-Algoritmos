# coding=utf-8
__author__ = "Martin Rios"
__copyright__ = "None"
__credits__ = ["Martin Rios", "Gonzalo Montaña", "Ignacio Oliveto"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Martin Rios"
__email__ = "riosmartin93@gmail.com"
__status__ = "Prototype"

import sys
from util.session_utils import *

reload(sys)
sys.setdefaultencoding('ISO-8859-1')

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, Flask
)
from controladores import auth, home, Usuario, cursos
from flask_cors import CORS

app = Flask(__name__,
            template_folder="web/templates",
            static_folder="web/static",
            static_url_path='/web/static')

app.config.from_mapping(
    SECRET_KEY='dev',
)
app.config['CORS-HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.register_blueprint(auth.bp)
app.register_blueprint(home.bp)
app.register_blueprint(Usuario.bp)
app.register_blueprint(cursos.bp)


def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line


@app.route('/')
def hello():
    list_routes()
    return render_template("index.html", user=getCurrentUser(session))


@app.route('/jugarTest')
def jugarTest():
    return render_template("laberinto.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
