import json
import unittest
import datetime

from pyjcd.client import JCDHTTPClient
from key import DEFAULT_API_KEY
from pyjcd.configuration import API_CONTRACT_LIST_URL
from pyjcd.exceptions import APICallError
from pyjcd.interface import JCDecauxInterface

class PyJCDTestInterface(unittest.TestCase):
    def setUp(self):
        super().setUp();

    def test_can_set_API_key(self):
        interface = JCDecauxInterface(DEFAULT_API_KEY)
        self.assertEqual(interface.API_key, DEFAULT_API_KEY)

        interface.set_API_key('foobar')
        self.assertEqual(interface.API_key, 'foobar')
        self.assertEqual(interface.client.API_key, 'foobar')

    def test_can_check_API_is_online(self):
        interface = JCDecauxInterface()
        response = interface.is_API_online()
        self.assertEqual(response, True)

    def test_can_raise_404(self):
        client = JCDHTTPClient(DEFAULT_API_KEY)
        with self.assertRaises(APICallError):
            response = client.call_API('gobbledygook', {})

    def test_can_raise_403(self):
        interface = JCDecauxInterface()
        interface.set_API_key('foobar')
        with self.assertRaises(APICallError):
            response = interface.is_API_online()

    def test_can_get_contract_list(self):
        interface = JCDecauxInterface()
        contracts = interface.get_contract_list()

        names = []
        for c in contracts:
            names.append(c.name)

        self.assertIn("Paris", names)

    def test_can_get_specific_contract(self):
        interface = JCDecauxInterface()
        contract = interface.get_contract('Valence')

        self.assertEqual("Valence", contract.name)


    def test_can_get_station_list(self):
        interface = JCDecauxInterface()
        stations = interface.get_station_list()

        names = []
        for s in stations:
            names.append(s.name)

        self.assertIn("34 - PATINOIRE", names)

    def test_can_get_station_list_for_contract(self):
        interface = JCDecauxInterface()

        contract = interface.get_contract_list()[2]
        self.assertEqual(contract.name, "Toulouse")

        stations = interface.get_station_list(contract=contract)

        names = []
        for s in stations:
            names.append(s.name)

        self.assertIn("00069 - FEUGA", names)

    def test_can_get_station_detail_for_contract_by_number(self):
        interface = JCDecauxInterface()

        contract = interface.get_contract("Toulouse")
        self.assertEqual(contract.name, "Toulouse")

        station = contract.get_station_detail(69)
        
        self.assertEqual("00069 - FEUGA", station.name)

    def test_can_get_station_list_as_json(self):
        interface = JCDecauxInterface()
        stations = interface.get_station_list(data_type='json')

        self.assertIn("34 - PATINOIRE", stations)