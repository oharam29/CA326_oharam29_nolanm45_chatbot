import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from googlesearch import search


def g_search(query):
    s = "Im not sure, Here's some links I found online: \n"
    for j in search(query, tld="co.in", num=3, stop=1, pause=2):
        s+= j + "\n"
    return s



def get_trains(s):
    # refines input, not needed due to entity recognition
    stations = ["Greystones", "Bray", "Shankill", "Killiney", "Dalkey", "Glenageary", "Sandycove and Glasthule",
                "Dun Laoghaire", "Salthill and Monkstown", "Seapoint", "Booterstown", "Sydney Parade", "Sandymount",
                "Lansdowne Road", "Grand Canal Dock", "Pearse", "Tara Street", "Connolly", "Clontarf Road", "Killester",
                "Harmonstown", "Raheny", "Kilbarrack", "Howth Junction"]
    s = s.split()
    for i in range(len(s)):
        if " ".join(s[0:i]) in stations:
            return " ".join(s[0:i]), " ".join(s[i:])


def print_trains(start,finish):


    r = requests.get(
        'http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=' + start + '&NumMins=10')
    tree = ET.fromstring(r.text)
    info = [[tree[i][j].text for j in range(len(tree[i]))] for i in range(len(tree))]

    count = 0
    s = "Current trains running from {} to {}:\n".format(start, finish)
    result = find_dart_destination(start, finish)

    for i in range(len(info)):
        if within_half_an_hour(info[i][4][:-3],info[i][15]) and info[i][result[0]] == result[1] and info[i][19] == "DART":
            s += "Destination: {} ETA: {} Due: {} mins\n".format(info[i][7], info[i][14], info[i][12])
            count += 1

    if count == 0:
        return "No Trains Running"
    else:
        return s


def within_half_an_hour(time1, time2):
    # compare the query time with the eta
    return datetime.strptime(time2, "%H:%M") < (datetime.strptime(time1, "%H:%M") + timedelta(minutes=30))


def find_dart_destination(start, finish):
    # dart splits at Howth junction
    stations = ["Greystones", "Bray", "Shankill", "Killiney", "Dalkey", "Glenageary", "Sandycove and Glasthule",
                "Dun Laoghaire", "Salthill and Monkstown", "Seapoint", "Booterstown", "Sydney Parade", "Sandymount",
                "Lansdowne Road", "Grand Canal Dock", "Dublin Pearse", "Tara Street", "Dublin Connolly", "Clontarf Road", "Killester",
                "Harmonstown", "Raheny", "Kilbarrack", "Howth Junction"]
    malahide = ["Clongriffin", "Portmarnock", "Malahide"]
    howth = ["Bayside", "Sutton", "Howth"]

    if start in stations:

        if finish in stations:
            return get_parameters(stations, start, finish)
        elif finish in malahide:
            # 7 is position of the destination
            return [7, "Malahide"]
        elif finish in howth:
            return [7, "Howth"]

    elif start in malahide:
        if finish in stations:
            # 18 position of direction
            return [18, "Southbound"]
        elif finish in malahide:
            return get_parameters(malahide, start, finish)

    elif start in howth:
        if finish in stations:
            return [18, "Southbound"]
        elif finish in howth:
            return get_parameters(howth, start, finish)


def get_parameters(trains, start, finish):
    # compares the index of the start and finish to find direction
    if trains.index(start) > trains.index(finish):
        return [18, "Southbound"]
    elif trains.index(start) < trains.index(finish):
        return [18, "Northbound"]


def all_stations():
    # lists out every station from the api
    r = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML")
    tree = ET.fromstring(r.text)
    station_list = [[tree[i][j].text for j in range(len(tree[i]))] for i in range(len(tree))]
    for n in range(len(station_list)):
        print(station_list[n])

