from negocio.DocenteABM import DocenteABM

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    abmDocente = DocenteABM()

    docente = abmDocente.traerDocente("Profe")
    return docente.__str__()

if __name__ == "__main__":
    app.run()

