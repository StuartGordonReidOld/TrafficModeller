
from Road import Road

class RoadNetwork:
    roads = []
    
    def __init__(self):
        self.roads = []
        return
        
    def addRoad(self, name):
        newRoad = Road(name)
        roads.append(newRoad)

if __name__ == "__main__":
    print "Hello World"
