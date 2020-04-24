def airlinId():
    return "airlinId"

def name():
    return "name"

def alias():
    return "alias"

def iata():
    return "iata"

def icao():
    return "icao"

def callsign():
    return "callsign"

def country():
    return "country"

def active():
    return "active"


switcher = {
    0: airlinId,
    1: name,
    2: alias,
    3: iata,
    4: icao,
    5: callsign,
    6: country,
    7: active
}

class RequestMap:
    def __self__(self):
        return self

    def numbers_to_strings(argument):
    # Get the function from switcher dictionary
        func = switcher.get(argument, "nothing")
    # Execute the function
        return func()