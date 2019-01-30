import requests
import xml.etree.ElementTree as ET


def get_station(station, direction=''):
    r = requests.get(
        'http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=' + station + '&NumMins=10')
    tree = ET.fromstring(r.text)

    l = [[tree[i][j].text for j in range(len(tree[i]))] for i in range(len(tree))]

    for i in range(len(l)):
        if l[i][10] == 'En Route':
            print("Destination: {} ETA: {} Status: {}".format(l[i][7], l[i][14], l[i][11]))





def all_stations():
    r = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML")
    tree = ET.fromstring(r.text)
    print(tree)


def chat():
    yes = ['yes', 'yeah', 'ye', 'i am', 'si']
    if (input('Hello there!!\nAre you travelling by train today?')) in yes:
        if (input("Are you looking for information for a particular station?")) == 'yes':
            stat = input("Which station?")
            dest = input("What direction are you going Northbound or Southbound?")
            get_station(stat, dest)

    else:
        print('Unable to help')
    input()


if __name__ == '__main__':
    #chat()
    get_station('Raheny',)