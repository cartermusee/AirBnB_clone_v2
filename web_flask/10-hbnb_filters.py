#!/usr/bin/python3
"""flask to run app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_st(self):
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filter():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
