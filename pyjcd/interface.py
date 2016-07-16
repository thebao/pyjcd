import json

from pyjcd import parsers
from pyjcd.client import JCDHTTPClient
from pyjcd.configuration import API_CONTRACT_LIST_URL, API_STATION_LIST_URL, \
    API_STATION_DETAIL_URL, API_CONTRACT_LIST_URLS

class JCDecauxInterface(object):

    def __init__(self, api_key=None):
        try:
            from key import DEFAULT_API_KEY
            self.API_key = DEFAULT_API_KEY
        except ImportError:
            self.API_key = api_key
        self.client = JCDHTTPClient(self.API_key)

    def set_API_key(self, api_key):
        self.client.API_key = api_key
        self.API_key = api_key

    def get_API_key(self):
        return self.API_key

    def is_API_online(self):
        response = self.client.call_API(API_CONTRACT_LIST_URL, {})
        if response is not None:
            return True
        return False

    def get_contract_list(self, data_type='object'):
        response = self.client.call_API(API_CONTRACT_LIST_URL, {})

        if data_type == 'json':
            return response

        d = json.loads(response)
        parser = parsers.ContractParser()
        contracts = [parser.parse_JSON(json.dumps(item), self) for item in d]
        return contracts

    def get_station_list(self, contract=None, data_type='object'):
        if contract is None:
            response = self.client.call_API(API_STATION_LIST_URL, {})
        else:
            response = self.client.call_API(API_STATION_LIST_URL, 
                {'contract': contract.name})

        if data_type == 'json':
            return response

        d = json.loads(response)
        parser = parsers.StationParser()
        return [parser.parse_JSON(json.dumps(item)) for item in d]

    def get_station_details(self, station, contract, data_type='object'):
        response = self.client.call_API(API_STATION_DETAIL_URL \
            % station.number, {'contract': contract.name})

        if data_type == 'json':
            return response

        parser = parsers.StationParser()
        return parser.parse_JSON(response)
