#   class to store latitude and longitude values as floats

class Location:
    def __init__(self, lat, lon):
        self.lat = float(lat)
        self.lon = float(lon)

    def __str__(self):
        return '(' + str(self.lat) + ', ' + str(self.lon) + ')'
        return str(self.lat) + ', ' + str(self.lon)

    #   overload the '==' operator to work with the Location class
    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon

    def latitude(self):
        return self.lat

    def longitude(self):
        return self.lon
