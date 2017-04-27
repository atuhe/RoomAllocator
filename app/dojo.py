from app.person import *
from app.rooms import *
from app.rooms import Office, LivingSpace
from app.person import Fellow, Staff

class Dojo(object):
        def __init__(self):
            self.office_rooms = []
            self.ls_rooms = []
            self.all_rooms = []
            self.staffs = []
            self.fellows = []
            self.all_people = []
            self.unallocated_person = []

        def create_room(self, room_type, room_list):
            """Usage: create_room <room_type> <room_name>..."""
            if room_type == 'office':
                for room_name in room_list:
                    new_office = Office(room_name)
                    self.all_rooms.append(new_office)
                    print("An {} {} has been successfully created!".format(room_type, room_name))
            else:
                room_type == 'livingspace'
                for room_name in room_list:
                    new_livingspace = LivingSpace(room_name)
                    self.all_rooms.append(new_livingspace)
                    print("{} {} has been successfully created!".format(room_type, room_name))

        def add_person(self, person_name, person_type, wants_accomodation):
            if not wants_accomodation:
                wants_accomodation = 'N'
            else:
                wants_accomodation = wants_accomodation.upper()
            print("Creating a person")

            #Add person to the system
            if person_name in [person for person in self.all_people if person.person_name == person_name]:
                print("person {0} already exists".format(person_name))
                return



        def print_room(self, room_name):
            # prints a room and all the people allocated to that room
            new_room = [x for x in self.all_rooms if x.room_name == room_name]
            print(room_name)
            new_added = new_room
            if len(new_added) < 1:
                print("Rooom has no new added persons ")
            elif len(new_added) > 6:
                print("Room has reached the maximum")
            else:
                print("All people in room %s" % room_name)
                for y in new_added:
                    print(y.person_name)

        #checkout allocations
        def print_allocations(self):
            if len(self.all_rooms) < 1:
                 print("Registered rooms none")
            else:
                for room in self.all_rooms:
                    print(room.room_name)
                    for x in room.occupants:
                        print(x.person_name)



