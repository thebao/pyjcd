
class City(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s - %s>' % (self.__class__.__name__, self.name)

class Contract(object):
    def __init__(self, name, commercial_name, country_code, cities, interface):
        self.name = name
        self.commercial_name = commercial_name
        self.cities = cities
        self.country_code = country_code
        self.interface = interface

    def get_station_list(self):
        return self.interface.get_station_list(self)

    def get_station_detail(self, station):
        return self.interface.get_station_details(self, station)

    def __repr__(self):
        return '<%s - %s>' % (self.__class__.__name__, self.name)

class Station(object):
    def __init__(self, name, number, address, lat, lng, banking, bonus, 
        status, contract, bike_stands, available_bike_stands, available_bikes, \
        last_update):

        self.name = name
        self.number = number 
        self.address = address
        self.lat = lat
        self.lng = lng
        self.banking = banking
        self.bonus = bonus
        self.status = status
        self.contract = contract
        self.bike_stands = bike_stands
        self.available_bike_stands = available_bike_stands
        self.available_bikes = available_bikes
        self.last_update = last_update

    def __repr__(self):
        return '<%s (%s) - %s>' % (self.__class__.__name__, \
            self.contract, self.name)
