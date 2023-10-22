#!/usr/bin/python3
"""module for flask to display hell hbnb"""


from flask import Flask

app = (__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
