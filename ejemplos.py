from flask import Flask, render_template

app = Flask(__name__)
name = "Peoppe"
@app.route('/')
def index():
    return "Index"

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/hola')
def hola():
    return "Hola Mundo"

@app.route('/template')
@app.route('/template/<name>')
def template(name=None):
  return render_template('index.html', name=name)

@app.route('/test')
def test(name=name):
    return render_template('index.html', name=name)

@app.route('/test2')
@app.route('/test2/<word>')
def test2(word="pene"):
  return render_template('index.html', name=word)

if __name__ == "__main__":
    app.run()
