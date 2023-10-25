#!/usr/bin/python3
"""flask to run app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_st(exc):
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb_filter():
    states = storage.all(State)
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html", states=states,
                           amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
