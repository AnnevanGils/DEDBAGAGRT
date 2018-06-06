from Edges import *
import os.path

class DistanceEdge:
    def __init__(self,ID,traffic1ID,traffic2ID):
        self.edgeID = ID
        self.traffic1ID = traffic1ID
        self.traffic2ID = traffic2ID

    def __str__(self):
        return str(self.edgeID) + ', ' + str(self.traffic1ID) + ', ' + str(self.traffic2ID)

    def format(self) -> str:
        return 'id,' + str(self.edgeID) + ',traffic1id,' + str(self.traffic1ID) + ',traffic2id,' + str(self.traffic2ID)

def saveDistanceEdges(nodes):
    #   list all header names
    header = ['id', 'traffic1id', 'traffic2id']
    #   open (or create) the file to save the nodes to
    #   the file is located in the script directory
    file = open(os.path.dirname(os.path.abspath(__file__)) + '\\output\\DistanceEdges.csv', 'w')

    #   write the elements of the header list to file
    #   separated by ', '
    file.write(','.join(header))

    #   write the attributes of each node to a different row
    for node in nodes:
        file.write('\n' + str(node))

    file.close()

# function that returns a list of
# q is the maximum distance between two traffic nodes
def create_distance_edges(trafficNodes: list, q):
    DistanceEdgesList = []

    distanceEdgeID = 0

    length = trafficNodes.__len__() -2

    for i in range(0, length):
        traffic1 = trafficNodes[i]

        for j in range(i+1,length+1):
            traffic2 = trafficNodes[j]

            if traffic1.id != traffic2.id and distance(traffic1,traffic2) < q:

                DistanceEdgesList.append(DistanceEdge(distanceEdgeID,traffic1.id,traffic2.id))

                distanceEdgeID += 1

    return DistanceEdgesList