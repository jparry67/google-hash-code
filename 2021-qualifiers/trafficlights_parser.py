from trafficlights_models import Street, Car, Schedule, Intersection

class Parser:
    def parse(self, input_file):
        f = open(input_file, "r")
        lines = f.readlines()
        num_seconds, num_intersections, num_streets, num_cars, points = map(int, lines[0].split())

        line_index = 1
        intersections = []
        for i in range(num_intersections):
            intersections.append(Intersection(i))

        streets = []
        for _ in range(num_streets):
            start_intersection, end_intersection, name, length = lines[line_index].split()
            streets.append(Street(start_intersection, end_intersection, name, length))
            intersections[int(start_intersection)].addOutgoingStreet(name)
            intersections[int(end_intersection)].addIncomingStreet(name)
            line_index += 1

        cars = []
        for _ in range(num_cars):
            car = lines[line_index].split()
            cars.append(Car(car[0], car[1:]))
            line_index += 1

        return Schedule(intersections, streets, cars)