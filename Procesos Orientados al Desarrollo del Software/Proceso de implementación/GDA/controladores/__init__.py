from flask import Flask
from controladores import registro

app = Flask(__name__)
app.config.from_mapping(
        SECRET_KEY='dev'
    )


app.register_blueprint(registro.bp)


@app.route('/')


def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
