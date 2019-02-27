import requests
import xml.etree.ElementTree as ET


def get_trains(s):
    # refines input
    stations = ["Greystones", "Bray", "Shankill", "Killiney", "Dalkey", "Glenageary", "Sandycove and Glasthule",
                "Dun Laoghaire", "Salthill and Monkstown", "Seapoint", "Booterstown", "Sydney Parade", "Sandymount",
                "Lansdowne Road", "Grand Canal Dock", "Pearse", "Tara Street", "Connolly", "Clontarf Road", "Killester",
                "Harmonstown", "Raheny", "Kilbarrack", "Howth Junction"]
    s = s.split()
    for i in range(len(s)):
        if " ".join(s[0:i]) in stations:
            return " ".join(s[0:i]), " ".join(s[i:])


def print_trains(text):
    start, finish = get_trains(text)

    r = requests.get(
        'http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=' + start + '&NumMins=10')
    tree = ET.fromstring(r.text)
    info = [[tree[i][j].text for j in range(len(tree[i]))] for i in range(len(tree))]
    count = 0
    s = "Current trains running from {} to {}:\n".format(start, finish)
    result = find_dart_destination(start, finish)

    if start in ["Malahide", "Howth", "Greystones", "Bray"]:
        for i in range(len(info)):
            if info[i][6] == start and info[i][result[0]] == result[1] and info[i][19] == "DART":
                s += "Destination: {} Expected Departure: {} Due: {} mins\n".format(info[i][7], info[i][15], info[i][12])
                count += 1

    else:

        for i in range(len(info)):
            if info[i][10] == 'En Route' and info[i][result[0]] == result[1] and info[i][19] == "DART":
                s += "Destination: {} ETA: {} Status: {}\n".format(info[i][7], info[i][14], info[i][11])
                count += 1

    if count == 0:
        return "No Trains Running"
    else:
        return s


def find_dart_destination(start, finish):

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
            return [7, "Malahide"]
        elif finish in howth:
            return [7, "Howth"]

    elif start in malahide:
        if finish in stations:
            return [18, "Southbound"]
        elif finish in malahide:
            return get_parameters(malahide, start, finish)

    elif start in howth:
        if finish in stations:
            return [18, "Southbound"]
        elif finish in howth:
            return get_parameters(howth, start, finish)

    else:
        pass


def get_parameters(trains, start, finish):
    if trains.index(start) > trains.index(finish):
        return [18, "Southbound"]
    elif trains.index(start) < trains.index(finish):
        return [18, "Northbound"]



def all_stations():
    r = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML")
    tree = ET.fromstring(r.text)
    station_list = [[tree[i][j].text for j in range(len(tree[i]))] for i in range(len(tree))]
    for n in range(len(station_list)):
        print(station_list[n])




if __name__ == '__main__':
    
    print(get_trains("Howth Junction Dublin Pearse"))
    #print(print_trains("Raheny Tara Street"))
    # print(get_trains("Howth Junction Raheny"))
    # print(get_trains("Grand Canal Dock Salthill and Monkstown"))

    #print(print_trains("Howth","Sandymount"))
    # print(print_trains("Greystones", "Portmarnock"))
    # print(print_trains("Sutton", "Howth"))    working
    # print(print_trains("Malahide", "Raheny"))
    # print(print_trains("Clongriffin", "Portmarnock")) working
    # print(print_trains("Portmarnock", "Malahide")) working
    #print(print_trains("Malahide", "Portmarnock"))    # print(print_trains("Killester", "Howth")) working
    # print(print_trains("Raheny", "Sandymount")) working
    # print(print_trains("Raheny", "Malahide"))   working
