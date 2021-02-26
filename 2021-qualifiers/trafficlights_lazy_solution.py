from trafficlights_models import Car, Street, Schedule, Intersection

class LazySolution:
    def schedule(self, schedule):
        # schedule.intersections[0].lightLengths['streetName'] = lightTime
        
        for i in schedule.intersections:
            for a in i.incoming: 
                i.lightLengths[a] = 1 
        return schedule.intersections
