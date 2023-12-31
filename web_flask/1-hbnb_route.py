#!/usr/bin/python3
"""
a script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def displayHbnb():
    return "HBNB"


host = '0.0.0.0'
port = 5000

if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)
