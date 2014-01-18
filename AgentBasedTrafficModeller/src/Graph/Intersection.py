
__author__="stuart"
__date__ ="$08 Jan 2014 9:06:16 PM$"

class Intersection:
    neighbours = []
    name = "not set"
    trafficCount = 0
    
    def __init__(self, intersectionName):
        self.neighbours = []
        self.name = intersectionName
        self.trafficCount = 0
        return
    
    def travelIntersection(self):
        trafficCount = trafficCount + 1
    
    def getTrafficCount(self):
        return trafficCount
    
    def printNeighbours(self):
        print "\nNeighbours of ", self.name, ": "
        for neighbour in self.neighbours:
            print neighbour.name, ","
        return
            
    def addNeighbour(self, newNode):
        self.neighbours.append(newNode)
        return

if __name__ == "__main__":
    print "Hello World"
