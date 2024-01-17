from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'about'


@app.route('/contact/')
def contact():
    return 'contact'


@app.route('/<int:a>/<int:b>')
def summa(a, b):
    return str(a + b)


@app.route('/<string:text>/')
def string(text):
    return str(len(text))


@app.route('/index/')
def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
