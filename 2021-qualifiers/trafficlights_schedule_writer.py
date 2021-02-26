class ScheduleWriter:
    def write(self, output_file_name, intersections):
        f = open(output_file_name, "w")
        f.write(str(len(intersections)) + '\n')
        for i, a in enumerate(intersections):
            f.write(str(i) + '\n')
            f.write(str(len(a.incoming)) + '\n')
            for x in a.incoming:
                f.write(x + ' ' + str(a.lightLengths[x]) + '\n')

        '''
        print len(intersections)
        for Intersection in intersections:
            print id
            print len(incomingStreets)
            for street in incomingStreets:
            print streetName, 1 '''