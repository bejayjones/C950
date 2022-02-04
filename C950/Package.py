class Package:
    def __init__(self, id, address, city, state, zip, deliveryTime, mass, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryTime = deliveryTime
        self.mass = mass
        self.notes = notes
        self.deliveryStatus = ["at the hub", 8]