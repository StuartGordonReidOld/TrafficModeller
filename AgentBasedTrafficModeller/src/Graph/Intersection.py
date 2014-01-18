
__author__="stuart"
__date__ ="$08 Jan 2014 9:06:16 PM$"

class Intersection:
    neighbours = []
    name = "not set"
    
    def __init__(self, intersectionName):
        self.neighbours = []
        self.name = intersectionName
        return
    
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
