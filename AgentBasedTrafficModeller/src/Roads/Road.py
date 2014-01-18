
class Road:
    intersections = []
    count = 0
    name = ""
    
    def __init__(self, roadName):
        self.intersections = []
        self.count = 0
        self.name = roadName
        return
        
    def travelRoad(self):
        self.count = self.count + 1