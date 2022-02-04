class Truck:
    def __init__(self, id):
        self.id = id
        self.speed = 18
        self.packages = []
        self.time = 0

    def addPackage(self, packageID):
        self.packages.append(packageID)
    def removePackage(self, packageID):
        self.packages.remove(packageID)
    def addTime(self, time):
        self.time += time

