
import random

class LightVehicle():
    name = "not set"
    availableRoutes = []

    def __init__(self):
        self.name = "Light Vehicle"
        self.availableRoutes = []
        return
    
    def travel(self):
        for route in self.availableRoutes:
            travel = random.random()
            if travel <= road.lightProbability:
                route.travelRoute()
        return
    
    def addRoute(self, route):
        availableRoutes.append(route)
        return

if __name__ == "__main__":
    print "Hello World"
