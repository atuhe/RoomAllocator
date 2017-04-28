from random import randint
from app.rooms  import *

#A super class person that takes in parameters
# person_id, person_name, person_type
class Person(object):
    def __init__(self, person_id, person_name, person_type):
        self.person_id = person_id
        self.person_name = person_name
        self.person_type = person_type


    #A function to determine allocation of ofices to people
    def allocate_office(self, all_rooms):
        office_rooms = []
        for office in all_rooms:
            max_occupants = 6
            if office.room_type == "office" and len(office.occupants) < max_occupants:
                office_rooms.append(office)
                got_rooms = len(office_rooms)
        if got_rooms > 0:
            random_room = randint(0, got_rooms)
            random_room -= 1
            office_rooms[random_room].occupants.append(self)
            room_name = office_rooms[random_room].room_name
            print("{0} has been allocated an office {1}".format(self.person_name, room_name))
        else:
            print("No offices to assign")
            return


#class Fellow that inherits from Person
class Fellow(Person):
    def __init__(self, person_name):
        self.person_name = person_name
        self.person_type = "fellow"


#class Fellow that inherits from Person
class Staff(Person):
    def __init__(self, person_name):
        self.person_name = person_name
        self.person_type = "staff"

