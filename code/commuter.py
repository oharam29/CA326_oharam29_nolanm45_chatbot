import requests
import xml.etree.ElementTree as ET 

def station(s):
	station = ["Skerries", "Rush and Lusk", "Drogheda", "Donabate", "Malahide"]

	s = s.split()
	for i in range(len(s)):
		if " ".join(s[0:i]) in station:
			return " ".join(s[0:i]), " ".join(s[i:])

def print_c(text):
	start, finish = station(text)

	r = requests.get('http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=' + start + '&NumMins=10')
	tree = ET.fromstring(r.text)
	info = [[tree[i][j].text for j in range(len(tree[i]))] for i in range(len(tree))]

	s = "Current trains running from {} to {}:\n".format(start, finish)
	
	count = 0
	if start in ["Drogheda"]:
		for i in range(len(info)):
			if info[i][6] == start and info[i][19] == "Train":
				s += "Destination: {} Expected Departure: {} Due: {} mins\n".format(info[i][7], info[i][15], info[i][12])
				count += 1

	else:
		for i in range(len(info)):
			if info[i][10] == 'En Route' and info[i][19] == "Train":
				s += "Destination: {} ETA: {} Status: {}\n".format(info[i][7], info[i][14], info[i][11])
				count += 1


	if count == 0:
		return "No Trains Running"
	else:
		return str(s)


if __name__ == '__main__':
    
    print(print_c("Donabate Skerries"))