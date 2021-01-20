#!/usr/bin/python3
""" List of states Module """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    from models.state import State
    States = storage.all(State).value()
    return render_template('7-states_list.html', states=States)


@app.teardown_appcontext
def end_session():
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
