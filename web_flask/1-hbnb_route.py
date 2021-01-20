#!/usr/bin/python3
""" HBNB Module """
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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
