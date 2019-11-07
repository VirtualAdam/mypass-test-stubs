#

import re
import datetime
from os import environ as env
from flask import Flask, request, redirect, jsonify
from imagerec import palm_check

APP = Flask(__name__)


# Controllers API
@APP.route("/")
def healthcheck():
    """No access token required to access this route
    """
    now = datetime.datetime.now()
    response = "Test API - Health Check - Available @ %s" % now.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(message=response)


@APP.route("/test-api/bio/<filename>")
def bio_test_id(filename):
    """A valid access token is required to access this route
    """
    result = palm_check(filename)

    return jsonify(message=result)


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=env.get("PORT", 3010))
