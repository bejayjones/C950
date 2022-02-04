#Brandon Jones 002390118
import Truck
import Package
import csv
import DirectHashTable


#create an instance of myHash class, which will be used to store and handle our package information
myHash = DirectHashTable.DirectHashTable()
packageTable = open("WGUPS Package File.csv")
packageData = csv.reader(packageTable)
next(packageData)
#create an array that will our package data reader will store information from our csv in
packages = []
#for each row in our package info csv, we will read in each column and pass that information
#to our package constructor to instantiate each package
for package in packageData:
    id = int(package[0])
    address = package[1]
    city = package[2]
    state = package[3]
    zip = package[4]
    delivery = package[5]
    mass = package[6]
    notes = package[7]
    package = Package.Package(id, address, city, state, zip, delivery, mass, notes)
    myHash.insert(package.id, package)
#follow a similar process as above, creating a distance array where we will store info from our distance csv
#we only store raw distance in this array, we will store the address separately in a different array
distanceTable = open("WGUPS Distance Table.csv")
distanceData = csv.reader(distanceTable)
distance = []
for row in distanceData:
    distance.append(row[2:])
#store the address information from our distance table
addressTable = open("WGUPS Distance Table.csv")
address = []
addressData = csv.reader(addressTable)
for row in addressData:
    #this line normalizes the read in data so that it easier to compare with our package information
    address.append((row[1:2][0]).strip().replace("\n", " ").replace("(", "").replace(")", ""))


#the following 9 variables are created to keep track of truck mileage at various times
truck1TotalNine = 0
truck1TotalTen = 0
truck1TotalTwelve = 0

truck2TotalNine = 0
truck2TotalTen = 0
truck2TotalTwelve = 0

truck1TotalDistance = 0
truck2TotalDistance = 0

#this runRoute function is the main algorithm of this program
#it takes a list of package numbers from each truck and a starting place is defined
#after the starting location is defined, the function cycles through the array comparing each package destination
#with the starting location to determine the next closest location
#once the next closest location is found, the function calculates the total mileage now including the distance to
#that location, calculates the time taken to reach that destination, then sets the new starting location equal to the destination
#of said package, marks the package as delivered
#then removes said package from the array of packages so that it is not eligible to be the next location

def runRoute(truck):
    firstLocation = 0
    totalDistance = 0
    global truck1TotalNine
    global truck1TotalTen
    global truck1TotalTwelve
    global truck2TotalNine
    global truck2TotalTen
    global truck2TotalTwelve
    global truck1TotalDistance
    global truck2TotalDistance
    while len(truck.packages) > 0:
        minDistance = 200
        for p2 in truck.packages:
            if(p2 == 9 and truck.time > 10.33):
                myHash.search(9).address = "410 S State St"
                myHash.search(9).zip = "84111"
            if firstLocation == 0 or len(truck.packages) == 1:
                nextDistance = distance[address.index(myHash.search(p2).address + " " + myHash.search(p2).zip)][0]
                #print("Hub Distance: ", nextDistance)
            else:
                nextDistance = distance[address.index(myHash.search(p2).address + " " + myHash.search(p2).zip)][address.index(myHash.search(firstLocation).address + " " + myHash.search(firstLocation).zip)]
            if nextDistance == '':
                nextDistance = distance[address.index(myHash.search(firstLocation).address + " " + myHash.search(firstLocation).zip)][address.index(myHash.search(p2).address + " " + myHash.search(p2).zip)]
            if float(nextDistance) < float(minDistance):
                minDistance = round(float(nextDistance), 2)
                nextLocation = p2
        firstLocation = nextLocation
        totalDistance += round(float(minDistance), 2)
        if(truck.time < 9.166666):
            if(truck.id == 1):
                truck1TotalNine += float(minDistance)
            if(truck.id == 2):
                truck2TotalNine += float(minDistance)
        if(truck.time < 10):
            if(truck.id == 1):
                truck1TotalTen += float(minDistance)
            if(truck.id == 2):
                truck2TotalTen += float(minDistance)
        if(truck.time < 12.28):
            if(truck.id == 1):
                truck1TotalTwelve += float(minDistance)
            if(truck.id == 2):
                truck2TotalTwelve += float(minDistance)
        if(truck.id == 1):
            truck1TotalDistance += float(minDistance)
        if(truck.id == 2):
            truck2TotalDistance += float(minDistance)
        truck.addTime(round((float(minDistance) / 18), 2))
        myHash.search(nextLocation).deliveryStatus = ["delivered", round(truck.time, 2)]
        #print(nextLocation, "Delievered at:", round(truck.time,2), round(minDistance, 2), "Miles Driven:", round(totalDistance, 2))
        truck.removePackage(nextLocation)

#instantiate two trucks for delivering packages
truck1 = Truck.Truck(1)
truck2 = Truck.Truck(2)
#set the start time of each truck
truck1.addTime(8)
truck2.addTime(8)
#load truck 1 with appropriate packages
truck1.addPackage(1)
truck1.addPackage(34)
truck1.addPackage(13)
truck1.addPackage(14)
truck1.addPackage(15)
truck1.addPackage(16)
truck1.addPackage(20)
truck1.addPackage(29)
truck1.addPackage(30)
truck1.addPackage(31)
truck1.addPackage(40)
truck1.addPackage(21)
truck1.addPackage(23)
truck1.addPackage(24)
#once packages are loaded on a truck, set the delivery status to "en route"
for each in truck1.packages:
    myHash.search(each).deliveryStatus = "en route"
#run the route for truck1
route1 = runRoute(truck1)

#load truck 1 again with a new set of packages
truck1.addPackage(2)
truck1.addPackage(4)
truck1.addPackage(5)
truck1.addPackage(7)
truck1.addPackage(8)
truck1.addPackage(9)
truck1.addPackage(10)
truck1.addPackage(11)
truck1.addPackage(12)
truck1.addPackage(17)
truck1.addPackage(19)
truck1.addPackage(22)
truck1.addPackage(39)
truck1.addPackage(33)
truck1.addPackage(35)
truck1.addPackage(27)
#set the delivery status of packages to en route
for each in truck1.packages:
    myHash.search(each).deliveryStatus = "en route"
#run the second route of truck 1
route2 = runRoute(truck1)

#load truck 2 with first load of packages
truck2.addPackage(3)
truck2.addPackage(36)
truck2.addPackage(37)
truck2.addPackage(38)
#set delivery status of packages to en route
for each in truck2.packages:
    myHash.search(each).deliveryStatus = "en route"
#run the first route of truck 2
route3 = runRoute(truck2)
#add time to truck 2 because the truck returned to the hub before the 9:05 so the truck must wait for the late packages
truck2.addTime(.16)
#load the next packages on the truck
truck2.addPackage(18)
truck2.addPackage(6)
truck2.addPackage(25)
truck2.addPackage(26)
truck2.addPackage(28)
truck2.addPackage(32)
#set delivery status accordingly
for each in truck2.packages:
    myHash.search(each).deliveryStatus = "en route"
#run the final route for truck 2
route4 = runRoute(truck2)

#the following code generates three status reports at distinct intervals.
#if the package is delivered before the status report, it will display the package information
#and the time of which it was delivered
#if the package has not been delivered by the time of the status report, it will display the package information
#and say the package is en route at the time of the status check
print("STATUS REPORT - 9:10AM")
print("Truck 1 Total Mileage:", round(truck1TotalNine, 2), "Truck 2 Total Mileage:", round(truck2TotalNine, 2))
for x in range(1, 41):
    if(myHash.search(x).deliveryStatus[1] < 9.166666):
        print(myHash.search(x).id, myHash.search(x).address, myHash.search(x).deliveryTime,
              myHash.search(x).city, myHash.search(x).zip, myHash.search(x).mass, myHash.search(x).deliveryStatus[0], myHash.search(x).deliveryStatus[1])
    else:
        print(myHash.search(x).id, myHash.search(x).address, myHash.search(x).deliveryTime,
              myHash.search(x).city, myHash.search(x).zip, myHash.search(x).mass, "en route", 9.17)
print("")
print("")

print("STATUS REPORT - 10AM")
print("Truck 1 Total Mileage:", round(truck1TotalTen, 2), "Truck 2 Total Mileage:", round(truck2TotalTen, 2))
for x in range(1, 41):
    if(myHash.search(x).deliveryStatus[1] < 10):
        print(myHash.search(x).id, myHash.search(x).address, myHash.search(x).deliveryTime,
              myHash.search(x).city, myHash.search(x).zip, myHash.search(x).mass, myHash.search(x).deliveryStatus[0], myHash.search(x).deliveryStatus[1])
    else:
        print(myHash.search(x).id, myHash.search(x).address, myHash.search(x).deliveryTime,
              myHash.search(x).city, myHash.search(x).zip, myHash.search(x).mass, "en route", 10.00)
print("")
print("")

print("STATUS REPORT - 12:17PM")
print("Truck 1 Total Mileage:", round(truck1TotalTwelve, 2), "Truck 2 Total Mileage:", round(truck2TotalTwelve, 2))
for x in range(1, 41):
    if(myHash.search(x).deliveryStatus[1] < 12.28):
        print(myHash.search(x).id, myHash.search(x).address, myHash.search(x).deliveryTime,
              myHash.search(x).city, myHash.search(x).zip, myHash.search(x).mass, myHash.search(x).deliveryStatus[0], myHash.search(x).deliveryStatus[1])
    else:
        print(myHash.search(x).id, myHash.search(x).address, myHash.search(x).deliveryTime,
              myHash.search(x).city, myHash.search(x).zip, myHash.search(x).mass, "en route", 12.28)

