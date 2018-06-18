from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Index"

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/hola')
def hola():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run()
