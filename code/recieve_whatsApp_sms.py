from flask import Flask, request, make_response
from dart_info import *
import json


app = Flask(__name__)


@app.route("/")
def disply():
    return "<h1>Hullo</h1>"


@app.route("/sms", methods=["POST"])
def sms_reply():

    req = request.get_json(silent=True, force=True)

    result = req.get("queryResult")
    parameters = result.get("parameters")
    station1, station2 = parameters.get("train_station"), parameters.get("train_station1")
    m = print_trains(station1,station2)

    msg = {
        "fulfillmentText": m,
        "source": m
        }

    res = json.dumps(msg , indent=4)


    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r



if __name__ == "__main__":
    app.run(debug=True)