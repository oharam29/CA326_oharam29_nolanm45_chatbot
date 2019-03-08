import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta


def print_c(start, finish, stations):
	try:
		if start in stations and finish in stations:
			if stations.index(start) > stations.index(finish):
				direction = "Northbound"
			elif stations.index(start) < stations.index(finish):
				direction = "Southbound"

			r = requests.get('http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=' + start + '&NumMins=10')
			tree = ET.fromstring(r.text)
			call_api = [[tree[i][j].text for j in range(len(tree[i]))] for i in range(len(tree))]

			s = "Current trains running from {} to {}:\n".format(start, finish)

			count = 0
			for i in range(len(call_api)):
				if within_half_an_hour(call_api[i][4][:-3],call_api[i][15]) and call_api[i][18] == direction and call_api[i][19] == "Train":
					s += "Destination: {} ETA: {} Direction: {}\n".format(call_api[i][7], call_api[i][14], call_api[i][18])
					count += 1

			if count == 0:
				return "No Trains Running"
			else:
				return str(s)

	except ValueError:
		return "Cannot connect to Irish Rail"


def within_half_an_hour(time1, time2):
    # compare the query time with the eta
    return datetime.strptime(time2, "%H:%M") < (datetime.strptime(time1, "%H:%M") + timedelta(hours=1))


if __name__ == '__main__':

    print(print_c(input() , input()))


