#!/usr/bin/python3
"""module for flask to display hell hbnb"""


from flask import Flask

app = (__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"
