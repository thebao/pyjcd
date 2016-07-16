import json

from pyjcd import models
from pyjcd.exceptions import ParseError

class ContractParser(object):
    def parse_JSON(self, JSON_string, interface):
        c = json.loads(JSON_string)
        try:
            contract = models.Contract(
                name=c['name'],
                commercial_name=c['commercial_name'],
                country_code=c['country_code'],
                cities=[city for city in c['cities']],
                interface=interface
            )
            return contract
        except KeyError as e:
            raise ParseError(e)

class StationParser(object):
    def parse_JSON(self, JSON_string):
        s = json.loads(JSON_string)
        station = models.Station(
            name=s['name'],
            number=s['number'],
            address=s['address'],
            lat=s['position']['lat'],
            lng=s['position']['lng'],
            banking=s['banking'],
            bonus=s['bonus'],
            status=s['status'],
            contract=s['contract_name'],
            bike_stands=s['bike_stands'],
            available_bike_stands=s['available_bike_stands'],
            available_bikes=s['available_bikes'],
            last_update=s['last_update']
        )
        return station