
class Route:
    count = 0
    name = "not set"
    intersections = []
    heavyProbability = 100
    lightProbability = 100
    
    def __init__(self, routeName):
        self.intersections = []
        self.count = 0
        self.name = routeName
        self.heavyProbability = 100
        self.lightProbability = 100
        return
        
    def travelRoute(self):
        self.count = self.count + 1
        for intersection in intersections:
            intersection.travelIntersection()
        return
    
    def getCount(self):
        return count