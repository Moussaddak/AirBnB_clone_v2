#!/usr/bin/python3
""" Python is fun! """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def say_hello():
    """ print Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    return "HBNB"


@app.route('/c/<text>')
def Cisfun(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def Pythonisfun(text=None):
    if text:
        return "Python {}".format(text.replace('_', ' '))
    return 'Python is cool'


@app.route('/number/<int:n>')
def only_numbers(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
