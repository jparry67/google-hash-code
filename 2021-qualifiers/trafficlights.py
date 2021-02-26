from trafficlights_models import Car, Street, Schedule, Intersection
from trafficlights_parser import Parser
from trafficlights_slightly_less_lazy_solution import SlightlyLessLazySolution
from trafficlights_schedule_writer import ScheduleWriter

input_files = ['a','b','c','d','e','f']
# input_files = ['a']

p = Parser()
writer = ScheduleWriter()
solution = SlightlyLessLazySolution()

for input_file in input_files:
    schedule = p.parse(input_file + '.txt')
    intersections = solution.schedule(schedule)
    writer.write(input_file + '_output.txt', intersections)
