from commuter import *
from dart_info import *
import unittest


class TestTrains(unittest.TestCase):

    def test_print_trains(self):
        trains = ["Greystones", "Bray", "Shankill", "Killiney", "Dalkey", "Glenageary", "Sandycove and Glasthule",
                "Dun Laoghaire", "Salthill and Monkstown", "Seapoint", "Booterstown", "Sydney Parade", "Sandymount",
                "Lansdowne Road", "Grand Canal Dock", "Dublin Pearse", "Tara Street", "Dublin Connolly", "Clontarf Road", "Killester",
                "Harmonstown", "Kilbarrack", "Howth Junction","Clongriffin", "Portmarnock", "Malahide","Bayside", "Sutton", "Howth"]

        for i in trains:
            print(i)
            self.assertTrue(print_trains("Raheny", i))


    def test_print_Commuter(self):

        trains = ["Dundalk","Drogheda", "Laytown", "Gormanston", "Balbriggan", "Skerries", "Rush and Lusk", "Donabate", "Malahide", "Portmarnock","Howth Junction"]
        stations = [station for station in trains if station != "Skerries"]
        for i in stations:
            print(i)
            self.assertTrue(print_c("Skerries",i, trains))

if __name__ == '__main__':
    unittest.main()