#   Code for loading traffic data CSV into designated data-structure

import csv
import os.path
from Location import *
from Interval import *

#   class to store all the important attributes associated to a TrafficNode

#   class to store all the important attributes associated to a TrafficNode object
class TrafficNode:
    def __init__(self, id, type, interval, location, locName):
    def __init__(self, id, type: str, interval: Interval, location: Location, locName: str):
        self.id = id
        self.type = type
        self.interval = interval
        self.location = location
        self.locName = locName

    def __str__(self):

    def lon(self):
        return self.location.longitude()

    def lat(self):
        return self.location.latitude()

    def interval(self):
        return self.interval

#   function to extract TrafficNodes from a .csv file and store them in a list
def loadTrafficNodes(fileName):
def loadTrafficNodes(fileName: str) -> list:
    reader = csv.reader(open(fileName))

    trafficNodes = []

    for row in reader:
        if (row[0] == "ongeval" or row[0] == 'blokkade') and row[14] == "TRUE" and row[40] != '':
            # Important indexes:
            #   situationRecordType         1
            #   situationId                 6
            #   validityOverallStartTime    11
            #   validityOverallEndTime      13
            #   lat lon                     40
            #   alertCLocationName          41

            #   Insert above values into TrafficNode Object

            #   Split the latitude and longitude into two separate variables
            if '|' in row[40]:
                loc = row[40].split('|')[0].split(' ')
            else:
                loc = row[40].split(' ')

            #   Split date and time into two separate variables
            start = row[11].split(' ')
            end = row[13].split(' ')

            #   Add a TrafficNode to the list of trafficNodes
            trafficNodes.append(
                TrafficNode(row[6], row[1], Interval(start[0], start[1], end[0], end[1]), Location(loc[0], loc[1]),
                            row[41]))

    return trafficNodes


def saveTrafficNodes(nodes):
#   function to save a list of TrafficNodes to .csv
def saveTrafficNodes(nodes: list):
    #   list all header names
    header = ['id', 'type', 'start date', 'start time', 'end date', 'end time', 'latitude', 'longitude',
              'location name']
    #   open (or create) the file to save the nodes to
    #   the file is located in the script directory
    file = open(os.path.dirname(os.path.abspath(__file__)) + '\\trafficNodes.csv', 'w')

    #   write the elements of the header list to file
    #   separated by ', '
    file.write(', '.join(header))

    #   write the attributes of each node to a different row
    for node in nodes:
        file.write('\n' + str(node))

    file.close()
