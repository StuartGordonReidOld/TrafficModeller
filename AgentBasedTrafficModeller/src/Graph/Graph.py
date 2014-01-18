
from Intersection import Intersection

__author__="stuart"
__date__ ="$08 Jan 2014 9:06:32 PM$"

class Graph:
    Intersections = []
    
    def __init__(self):
        self.Intersections = []
        return
    
    def addLink(self, intersectionA, intersectionB):
        intersectionA.addNeighbour(intersectionB)
        return
    
    def addTwoWay(self, A, B):
        intersectionA = self.get(A)
        intersectionB = self.get(B)
        self.addLink(intersectionA, intersectionB)
        self.addLink(intersectionB, intersectionA)
        return
    
    def addOneWay(self, A, B):
        intersectionA = self.get(A)
        intersectionB = self.get(B)
        self.addLink(intersectionA, intersectionB)
        return
    
    def get(self, name):
        #Check if any nodes exist
        if(len(self.Intersections) == 0):
            self.Intersections.append(Intersection(name))
        else:
            fetched = self.Intersections[0]
        #Check if node already exists
        found = 0
        for intersection in self.Intersections:
            if intersection.name == name:
                fetched = intersection
                found = 1
                break
        #If not found append new node and return
        if found == 0:
            fetched = Intersection(name)
            self.Intersections.append(fetched)
        #Return the found / new node
        return fetched
    
    def printNodes(self):
        print "\nList of all Nodes: "
        for intersection in self.Intersections:
            print intersection.name, ","
        return

if __name__ == "__main__":
    g = Graph()
    g.addTwoWay("Jan Smuts", "Empire")
    g.addTwoWay("Empire", "Barry Hertzog")
    g.printNodes()
    janSmuts = g.get("Jan Smuts")
    janSmuts.printNeighbours()
    empire = g.get("Empire")
    empire.printNeighbours()
    barry = g.get("Barry Hertzog")
    barry.printNeighbours()
