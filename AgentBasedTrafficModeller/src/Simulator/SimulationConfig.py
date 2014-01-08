# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="stuart"
__date__ ="$08 Jan 2014 9:05:50 PM$"

class SimulationConfig:
    totalVehicles = 0
    lightVehicles = 0
    heavyVehicles = 0
    # TODO: Add any additional variables light vehicle weight? etc.
    
    def __init__(self):
        self.totalVehicles = 0
        self.lightVehicles = 0
        self.heavyVehicles = 0
        return
    
    def run(self,fileName):
        self.readData(fileName)
        self.printData()
    
    def readData(self, fileName):
        # TODO: Open up the Config text file
        # TODO: Read values into the 
        # 1. total Vehicles,
        # 2. light Vehicles, and
        # 3. heavy Vehicles variables
        # TODO: Add additional variables and lines in the Config text file for
        # additional required information e.g. weights of vehicles? etc.
        return
    
    def printData(self):
        print "Total vehicles is ", self.totalVehicles
        print "Heavy vehicles is ", self.heavyVehicles
        print "Light vehicles is ", self.lightVehicles
        # TODO: Print any additional variables
        return

if __name__ == "__main__":
    config = SimulationConfig()
    config.run("Config")
