import unittest
import datetime

from pyjcd.models import City, Contract, Station
from pyjcd.interface import JCDecauxInterface

class PyJCDTestModels(unittest.TestCase):
    def setUp(self):
        super().setUp();

    def test_can_create_city(self):
        city = City(name="Dublin")

        self.assertEqual(city.name, "Dublin")

    def test_can_create_contract(self):
        city1 = City(name="Verdaud")
        city2 = City(name="Calibours")

        interface = JCDecauxInterface()

        contract = Contract(name="Lyon", commercial_name="Vélov",
            country_code="FR", cities=[city1, city2], interface=interface)

        self.assertEqual(contract.country_code, "FR")
        self.assertEqual(len(contract.cities), 2)

    def test_can_create_station(self):
        city = City(name="Hunnestad")

        interface = JCDecauxInterface()

        contract = Contract(name="Mattmar", commercial_name="Trak",
            country_code="SWE", cities=[city], interface=interface)

        station = Station(name="Hundbergsvägen 15", number="406", \
            address="Hundbergsvägen 15", lat=60.2989303, lng=15.4837905, \
            banking=True, bonus=False, status="OPEN", contract=contract, \
            bike_stands=16, available_bike_stands=12, available_bikes=4, 
            last_update=1468422595000)

        self.assertEqual(station.contract.name, "Mattmar")