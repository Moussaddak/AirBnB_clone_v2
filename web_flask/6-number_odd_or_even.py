#!/usr/bin/python3
""" Odd or even? """
from flask import Flask, render_template

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


@app.route('/number_template/<int:n>')
def display_HTML(n):
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    if n % 2:
        return render_template('6-number_odd_or_even.html', n=n, even_odd='odd')
    return render_template('6-number_odd_or_even.html', n=n, even_odd='even')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
