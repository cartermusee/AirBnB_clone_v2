#!/usr/bin/python3
"""flask to run app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_st(exception):
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    states = storage.all("State")
    sortedd = sorted(states.values(), key=lambda state: state.name)
    return render_template("9-states.html", states=sortedd)


@app.route("/states/<id>", strict_slashes=False)
def state_cities(id):
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", states=state, mode="id")
    return render_template("9-states.html", states=state, mode="none")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
