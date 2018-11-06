# coding=utf-8
__author__ = "Martin Rios"
__copyright__ = "None"
__credits__ = ["Martin Rios", "Gonzalo Montaña", "Ignacio Oliveto"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Martin Rios"
__email__ = "riosmartin93@gmail.com"
__status__ = "Prototype"


import json
from flask import current_app as app

def crearError(errorCode, errorText):
    data = {
        "error": errorCode,
        "errorText": errorText
    }
    return json.dumps(data)

def createResponseAsJSON(data):
    return json.dumps(data)