import requests
import xml.etree.ElementTree as ET


def print_trains(start, index, var, train_type):
    r = requests.get(
        'http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=' + start + '&NumMins=10')
    tree = ET.fromstring(r.text)
    info = [[tree[i][j].text for j in range(len(tree[i]))] for i in range(len(tree))]
    count = 0
    for i in range(len(info)):
        if info[i][10] == 'En Route' and info[i][index] == var and info[i][19] == train_type:
            print("Destination: {} ETA: {} Status: {}".format(info[i][7], info[i][14], info[i][11]))
            count += 1
    if count == 0:
        print("No Trains Running")


def find_dart_destination(start, finish):
    stations = ["Greystones", "Bray", "Shankill", "Killiney", "Dalkey", "Glenageary", "Sandycove and Glasthule",
                "Dun Laoghaire", "Salthill and Monkstown", "Seapoint", "Booterstown", "Sydney Parade", "Sandymount",
                "Lansdowne Road", "Grand Canal Dock", "Pearse", "Tara Street", "Connolly", "Clontarf Road", "Killester",
                "Harmonstown", "Raheny", "Kilbarrack", "Howth Junction"]
    malahide = ["Clongriffen", "Portmarnock", "Malahide"]
    howth = ["Bayside", "Sutton", "Howth"]

    if finish in malahide:
        print_trains(start, 7, "Malahide", "DART")
    elif finish in howth:
        print_trains(start, 7, "Howth", "DART")
    else:
        if start in malahide or start and finish in stations:
            print_trains(start, 18, "Southbound", "DART")
        elif stations.index(start) > stations.index(finish):
            print_trains(start, 18, "Southbound", "DART")
        elif stations.index(start) < stations.index(finish):
            print_trains(start, 18, "Northbound", "DART")
        elif start not in stations or finish not in stations:
            print("Unable to find station")


def all_stations():
    r = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML")
    tree = ET.fromstring(r.text)
    station_list = [[tree[i][j].text for j in range(len(tree[i]))] for i in range(len(tree))]
    for n in range(len(station_list)):
        print(station_list[n])


def chat():
    yes = ['yes', 'yeah', 'ye', 'i am', 'si']
    if (input('Hello there!!\nAre you travelling by train today?')) in yes:
        if (input("Are you looking for information for a particular station?")) == 'yes':
            stat = input("Which station?")
            dest = input("What is your destination?")
            find_dart_destination(stat, dest)
    else:
        print('Unable to help')
    input()


if __name__ == '__main__':
    # all_stations()
    print_trains("Howth", 18, "Northbound", "Train")
    """
    print("\nMALAHIDE\n")
    find_dart_destination("Clontarf Road", "Portmarnock")
    print("\nHOWTH\n")
    find_dart_destination("Malahide", "Raheny")
    print("\nNorthbound\n")
    find_dart_destination("Clontarf Road", "Kilbarrack")
    print("\nSouthbound\n")
    find_dart_destination("Portmarnock", "Sandymount")

    chat()
    """