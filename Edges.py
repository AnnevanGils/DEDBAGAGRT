MAXDISTANCESQUARED = ... #choose parameter

class WeatherIncidentEdge:
    def __init__(self, weatherID, trafficID, location, interval):
        self.weatherID = weatherID
        self.trafficID = trafficID
        self.location = location
        self.interval = interval

    def __str__(self):
        return 'weatherID, ' + str(self.weatherID) + ', trafficID, ' + str(self.trafficID) + ', location, ' \
               + str(self.location) + ', interval, ' + str(self.interval)

def distance_squared(node1, node2):
        return (node1.lat() - node2.lat())**2 + (node1.lon() - node2.lon())**2

def time_overlap(node1, node2):
    return node1.interval().overlap(node2.interval())

def create_edges(TrafficNodesList, WeatherNodesList, stationNodesList):
    for traffic in TrafficNodesList:
        for weather in WeatherNodesList:
            if distance_squared(traffic, weather) < MAXDISTANCESQUARED and time_overlap(traffic, weather):
