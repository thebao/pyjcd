import unittest
import json

from pyjcd.exceptions import ParseError
from pyjcd.models import City, Contract, Station
from pyjcd.interface import JCDecauxInterface
from pyjcd import parsers 

class PyJCDTestModels(unittest.TestCase):
    def setUp(self):
        super().setUp();

    def test_can_raise_parser_error(self):
        interface = JCDecauxInterface()
        json_obj = {
            'name': 'foo', 
            'country_code': 'bar'
        }
        parser = parsers.ContractParser()
        with self.assertRaises(ParseError):
            contracts = parser.parse_JSON(json.dumps(json_obj), interface)