
import random

class HeavyVehicle():
    name = "not set"
    availableRoutes = []

    def __init__(self):
        self.name = "Heavy Vehicle"
        self.availableRoutes = []
        return
    
    def travel(self):
        for route in self.availableRoutes:
            travel = random.random()
            if travel <= road.heavyProbability:
                route.travelRoute()
        return
    
    def addRoute(self, route):
        availableRoutes.append(route)
        return

if __name__ == "__main__":
    print "Hello World"
