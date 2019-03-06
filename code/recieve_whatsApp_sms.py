from flask import Flask, request, make_response
from dart_info import *
from commuter import *
import json

app = Flask(__name__)


@app.route("/")
def disply():
    return "<h1>Hullo</h1>"


@app.route("/sms", methods=["POST"])
def sms_reply():

    req = request.get_json(silent=True, force=True)

    result = req.get("queryResult")
    action = result.get("action")
    if action == "find_trains":
        parameters = result.get("parameters")
        station1, station2 = parameters.get("train_station"), parameters.get("train_station1")
        m = print_trains(station1,station2)

    elif action in ["find_commuter","find_route2","find_route3"] :

        parameters = result.get("parameters")
        station1, station2 = parameters.get("commuter_station"), parameters.get("commuter_station1")
        if action == "find_commuter":
            station_lst = ["Dundalk","Drogheda", "Laytown", "Gormanston", "Balbriggan", "Skerries", "Rush and Lusk", "Donabate", "Malahide", "Portmarnock","Howth Junction and Donaghmede"]
        elif action == "find_route2":
            station_lst = ["Longford", "Edgeworthstown", "Mullingar","Enfield","Kilock", "Maynooth" ,  "Leixlip (Louisa Bridge)", "Leixlip (Confey)", "Clonsilla", "Coolmine", "Castleknock", "Navan Road Parkway","Ashtown", "Broombridge", "Drumcondra", "Dublin Connolly"]
        elif action == "find_route3":
            station_lst = ["Newbridge", "Sallins", "Hazelhatch" , "Adamstown", "Clondalkin", "Cherry Orchard", "Drumcondra","Dublin Connolly","Tara Street", "Dublin Pearse", "Grand Canal Dock" ]

        m = print_c(station1,station2,station_lst)


    elif action == "input.unknown":
        m = g_search(result.get("queryText"))


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