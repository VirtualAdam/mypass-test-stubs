#
# ATD - CR3 Download API
#


import re
import datetime
from os import environ as env
from flask import Flask, request, redirect, jsonify

APP = Flask(__name__)




# Controllers API
@APP.route("/")
def healthcheck():
    """No access token required to access this route
    """
    now = datetime.datetime.now()
    response = "Test API - Health Check - Available @ %s" % now.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(message=response)


@APP.route("/test-api/DID/<test_id>")
def download_test_id(test_id):
    """A valid access token is required to access this route
    """
    # We only care for an integer string, anything else is not safe:
    safe_test_id = re.sub("[^0-9]", "", test_id)

    math = int(safe_test_id) +1

    return jsonify(message=math)


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=env.get("PORT", 3010))
