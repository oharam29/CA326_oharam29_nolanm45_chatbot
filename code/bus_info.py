import requests


def bus_stop(stop, route=''):
    json_data = requests.get(
        'https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?stopid=' + stop + '&routeid=' + route).json()
    for i in range(json_data['numberofresults']):
        print('Route: {} Arrival: {} Destination {}'.format(json_data['results'][i]['route'],
                                                            json_data['results'][i]['arrivaldatetime'],
                                                            json_data['results'][i]['destination']))


def get_route(route_no):
    try:
        print("One moment please")

        data = requests.get(
            'https://data.smartdublin.ie/cgi-bin/rtpi/routeinformation?routeid=' + route_no + '&operator=bac').json()
        if not data['results']:
            print('No route information available')
        else:
            s = data['results'][0]['stops']
            print("Good news, this is what I found online:")
            for i in range(len(s)):
                print('Stop: {} Location: {}'.format(s[i]['stopid'], s[i]['shortname']))
    except ValueError:
        print("Cannot connect")


def get_all_stops():
    data = requests.get('https://data.smartdublin.ie/cgi-bin/rtpi/busstopinformation?operator=bac')
    print(data['results'][0])


def chat():
    yes = ['yes', 'yeah', 'ye', 'i am', 'si']
    if (input('Hello there!!\nAre you travelling by bus today?')) in yes:
        if (input("Are you looking for real-time informtaion for Route or a Stop ")) == 'route':
            get_route(input('which route? '))
        else:
            bus_stop(input('which bus stop? '))
    else:
        print('Unable to help')
    input()


if __name__ == '__main__':
    get_route('31')
    #chat()
