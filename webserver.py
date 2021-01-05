"""Basic hello message for flask app"""
import os
from flask import Flask
APP = Flask(__name__)


@APP.route("/")
def hello():
    """Basic hello message for flask app"""

    try:
        variable_value = os.environ['MYVAR']
    except KeyError:
        variable_value = "DEFAULT, Key error -MYVAR not set in environment Variable"

    return "New hello v2 from inside the contianer variable = {}".format(variable_value)

APP.run(debug=True, host="0.0.0.0")
