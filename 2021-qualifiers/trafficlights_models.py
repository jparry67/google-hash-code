class Street:
    def __init__(self, start_intersection, end_intersection, name, length):
        self.start_intersection = int(start_intersection)
        self.end_intersection = int(end_intersection)
        self.name = name 
        self.length = int(length)

    def __repr__(self):
        return self.name + ": " + str(self.start_intersection) + " -> " + str(self.end_intersection) + ", length: " + str(self.length)

class Car:
    def __init__(self, num_streets, streets):
        self.num_streets = int(num_streets)
        self.streets = streets

    def __repr__(self):
        return str(self.num_streets) + ": " + str(self.streets)

class Schedule:
    def __init__(self, intersections, streets, cars):
        self.intersections = intersections
        self.streets = streets
        self.cars = cars

class Intersection:
    def __init__(self, id):
        self.id = id
        self.incoming = []
        self.outgoing = []
        self.lightLengths = {}

    def addIncomingStreet(self, street_name):
        self.incoming.append(street_name)

    def addOutgoingStreet(self, street_name):
        self.outgoing.append(street_name)

    def __repr__(self):
        return str(self.id) + ", incoming: " + str(self.incoming) + ", outgoing: " + str(self.outgoing)


'''
class street_importance:
    def __init__(self, cars):
        self.streets = {}
        for car in cars:
            for street in car.streets:
                if 
            '''