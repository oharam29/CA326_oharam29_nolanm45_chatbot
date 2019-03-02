import requests
import xml.etree.ElementTree as ET


def print_c(start, finish):
        stations = ["Dundalk", "Drogheda", "Laytown", "Gormanston", "Balbriggan", "Skerries", "Rush and Lusk",
                    "Donabate", "Malahide", "Portmarnock", "Howth Junction"
            , "Dublin Connolly", "Tara Street", "Dublin Pearse", "Grand Canal Dock", "Lansdowne Road", "Sydeny Parade",
                    "Blackrock", "Dun Laoghaire", "Bray"]
        direction = ""
        if start in stations and finish in stations:
            if stations.index(start) > stations.index(finish):
                direction = "Northbound"
            elif stations.index(start) < stations.index(finish):
                direction = "Southbound"

            r = requests.get(
                'http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=' + start + '&NumMins=10')
            tree = ET.fromstring(r.text)
            call_api = [[tree[i][j].text for j in range(len(tree[i]))] for i in range(len(tree))]

            s = "Current trains running from {} to {}:\n".format(start, finish)

            count = 0
            for i in range(len(call_api)):
                if call_api[i][10] == 'En Route' and call_api[i][18] == direction and call_api[i][19] == "Train":
                    s += "Destination: {} ETA: {} Status: {}\n".format(call_api[i][7], call_api[i][14], call_api[i][11])
                    count += 1

            if count == 0:
                return "No Trains Running"
            else:
                return str(s)
