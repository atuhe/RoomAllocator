from app.person import *
from app.rooms import *
from app.rooms import Office, LivingSpace
from app.person import Fellow, Staff
from random import randint


class Dojo(object):
        def __init__(self):
            self.office_rooms = []
            self.ls_rooms = []
            self.all_rooms = []
            self.staffs = []
            self.fellows = []
            self.all_people = []
            self.unallocated_person = []
            self.occupant = []

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

            if person_type == 'fellow':
                    new_fellow = Fellow(person_name)
                    print("Fellow {0} has been created succesfully".format(person_name))
                    new_fellow.allocate_office(self.all_rooms)
                    self.all_people.append(new_fellow)
            elif person_type == 'staff':
                    new_staff = Staff(person_name)
                    print("Staff {0} has been created succesfully".format(person_name))
                    new_staff.allocate_office(self.all_rooms)
                    self.all_people.append(new_staff)

        def print_room(self, room_name):

            # prints a room and all the people allocated to that room
            new_room = [x for x in self.all_rooms if x.room_name == room_name]
            print(room_name)

            if len(new_room) > 0:
                print("All people in room %s" % room_name)
                for y in [person for person in new_room]:
                    print(y.person_name)
            else:
                print ("Rooom has no new added persons ")

         #checkout allocations
        def print_allocations(self):
           pass

