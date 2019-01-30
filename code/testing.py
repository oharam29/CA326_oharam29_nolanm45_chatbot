"""
import requests
import xml.etree.ElementTree as ET
r=requests.get('http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML')

tree = ET.fromstring(r.text)

all_stations = [[tree[i][j].text for j in range(len(tree[i]))] for i in range(len(tree))]
#print(all_stations)

for n in range(len(all_stations)):
    print(all_stations[n])
"""
import requests
import xml.etree.ElementTree as ET


def get_station(station, destination):
    r = requests.get(
        'http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=' + station + '&NumMins=10')
    tree = ET.fromstring(r.text)
    l = [[tree[i][j].text for j in range(len(tree[i]))] for i in range(len(tree))]
    find_dart_destination(l,station,destination)


def find_dart_destination(info, start, finish):
    stations = ["Greystones", "Bray", "Shankill", "Killiney", "Dalkey", "Glenageary", "Sandycove and Glasthule",
                "Dun Laoghaire", "Salthill and Monkstown", "Seapoint", "Booterstown","Sydney Parade", "Sandymount",
                "Lansdowne Road", "Grand Canal Dock", "Pearse", "Tara Street", "Connolly","Clontarf Road","Killester",
                "Harmonstown", "Raheny", "Kilbarrack", "Howth Junction"]
    malahide = ["Clongriffen", "Portmarnock", "Malahide"]
    howth = ["Bayside","Sutton", "Howth"]

    if finish in malahide:
        for i in range(len(info)):
            if info[i][10] == 'En Route' and info[i][7] == "Malahide":
                print("Destination: {} ETA: {} Status: {}".format(info[i][7], info[i][14], info[i][11]))
    elif finish in howth:
        for i in range(len(info)):
            if info[i][10] == 'En Route' and info[i][7] == "Howth":
                print("Destination: {} ETA: {} Status: {}".format(info[i][7], info[i][14], info[i][11]))
    else:
        if stations.index(start) > stations.index(finish):
            for i in range(len(info)):
                if info[i][10] == 'En Route' and info[i][18] == "Southbound":
                    print("Destination: {} ETA: {} Status: {}".format(info[i][7], info[i][14], info[i][11]))
        elif stations.index(start) < stations.index(finish):
            for i in range(len(info)):
                if info[i][10] == 'En Route' and info[i][18] == "Northbound":
                    print("Destination: {} ETA: {} Status: {}".format(info[i][7], info[i][14], info[i][11]))


def all_stations():
    r = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML")
    tree = ET.fromstring(r.text)
    print(tree)


def chat():
    yes = ['yes', 'yeah', 'ye', 'i am', 'si']
    if (input('Hello there!!\nAre you travelling by train today?')) in yes:
        if (input("Are you looking for information for a particular station?")) == 'yes':
            stat = input("Which station?")
            dest = input("What is your destination?")
            get_station(stat, dest)

    else:
        print('Unable to help')
    input()


if __name__ == '__main__':
    print("\nMALAHIDE\n")
    get_station("Raheny", "Portmarnock")
    print("\nHOWTH\n")
    get_station("Raheny", "Bayside")
    print("\nNorthbound\n")
    get_station("Clontarf Road", "Kilbarrack")
    print("\nSouthbound\n")
    get_station("Raheny", "Sandymount")

    chat()

