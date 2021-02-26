from trafficlights_models import Car, Street, Schedule, Intersection
import math
import re

class SlightlyLessLazySolution:
    def schedule(self, schedule):
        # schedule.intersections[0].lightLengths['streetName'] = lightTime

        totalStreetUsageCount = {}

        for car in schedule.cars:
            for street in car.streets:
                if street not in totalStreetUsageCount:
                    totalStreetUsageCount[street] = 1
                else:
                    totalStreetUsageCount[street] = 1 + totalStreetUsageCount[street]

                # setattr(totalStreetUsageCount, street, 1 + getattr(totalStreetUsageCount, street, 0))


        for intersection in schedule.intersections:
            maxCount = 1
            sumCount = 0
            for incomingStreetName in intersection.incoming: 
                if (incomingStreetName in totalStreetUsageCount):
                    sumCount = sumCount + totalStreetUsageCount[incomingStreetName]
                if (incomingStreetName in totalStreetUsageCount and totalStreetUsageCount[incomingStreetName] > maxCount): 
                    maxCount = totalStreetUsageCount[incomingStreetName]


            for incomingStreetName in intersection.incoming: 
                if incomingStreetName not in totalStreetUsageCount:
                    intersection.lightLengths[incomingStreetName] = 1
                else:
                    # intersection.lightLengths[incomingStreetName] = math.ceil(totalStreetUsageCount[incomingStreetName] * 10 / maxCount)
                    intersection.lightLengths[incomingStreetName] = math.ceil(totalStreetUsageCount[incomingStreetName] * 10 / sumCount)

        return schedule.intersections
