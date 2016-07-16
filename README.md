#  PyJCD
A Python wrapper around the JCDecaux/Cyclocity API

##  What is it?
PyJCD is a client Python wrapper library for the JCDecaux/Cyclocity (JCD) web API.

It allows quick and easy access to JCD contract and station data from Python applications via a simple object model and in a human-friendly fashion.

No additional libraries are requested: only the Python standard library modules.

##  Support

PyJCD currently supports _version 1.0_ of the JCD API (which is the latest one)

##  Usage

### API key

As the JCDecaux/Cyclocity API needs a valid API key to allow responses, 
*PyJCD won't work if you don't provide one*.

You can signup for a free API key [on the JCDecaux developer's website](https://developer.jcdecaux.com/)

### Examples

```python

from pyjcd.interface import JCDecauxInterface

jcd = JCDecauxInterface('your-API-key')  # You MUST provide a valid API key

# Get a list of all contracts (ie: cities in which the JCDecaux/Cyclocity services are available):
contracts = jcd.get_contract_list()

# Get a list of all stations (world-wide)

stations = jcd.get_station_list()

print(stations)             # [<Contract - Rouen>,
                            # <Contract - Paris>,
                            # <Contract - Toulouse>,
                            # ...

# Get a specific contract:  

dublin_contract = jcd.get_contract('Dublin')

print(dublin_contract)      # <Contract - Dublin>


# Get a list of all stations (for a specific contract):

dublin_contract = jcd.get_contract('Dublin')
stations = dublin_contract.get_station_list()

print(stations)             # [<Station (Dublin) - SMITHFIELD NORTH>,
                            # <Station (Dublin) - PARNELL SQUARE NORTH>,
                            # <Station (Dublin) - PEARSE STREET>,
                            # ...

# Get a specific station for a specific contract:

dublin_contract = jcd.get_contract('Dublin')
station = dublin_contract.get_station_detail(29)

print(station)              # <Station (Dublin) - ORMOND QUAY UPPER>

```

