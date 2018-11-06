from flask import Flask
from controladores import registro
from flask_cors import CORS

app = Flask(__name__)
app.config.from_mapping(
        SECRET_KEY='dev',
    )
app.config['CORS-HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"*": {"origins": "*"}})


app.register_blueprint(registro.bp)


@app.route('/')


def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
