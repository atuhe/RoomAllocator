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
            self.all_people = {}
            self.unallocated_person = {}

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


        def add_person(self, person_id, person_name, person_type, wants_accomodation='N'):
            """Usage: add_person <person_name> <FELLOW|STAFF> [wants_accommodation]"""
            #Add person to the system
            if person_name in self.all_people:
                print('person{}already exists')

                # Check if person is staff and wants accommodation.
            elif person_type == 'F' and wants_accomodation == 'Y':
                new_fellow = Fellow(person_name, person_type)
                self.all_people[new_fellow.person_name] = person_type
                self.append(new_fellow.person_name)

                random_office = self.generate_random_office()
                random_ls = self.generate_random_living_space()

                if not random_office and not random_ls:
                    self.unnalocated_person[new_fellow.person_name] = person_type
                    print('Added%s to unnallocated list')

                elif not random_office and random_ls:
                    self.unnalocated_person[new_fellow.person_name] = person_type
                    print('Added%s to unnallocated list')
                    self.ls_rooms[random_ls].append(new_fellow.person_name)
                    print("Added: %s and allocated them to a living space %s: " % (new_fellow.person_name, random_ls))

                elif not random_ls and random_office:
                    self.unallocated_person[new_fellow.person_name] = person_type
                    print('Added %s to the unallocated list' % new_fellow.person_name)
                    self.office_rooms[random_office].append(new_fellow.person_name)
                    print("Added: %s and allocated them to an office %s: " % (new_fellow.person_name, random_office))

                else:
                    self.office_rooms[random_office].append(new_fellow.person_name)
                    print("Added: %s and allocated them to %s: " % (new_fellow.person_name, random_office))
                    self.ls_rooms[random_ls].append(new_fellow.person_name)
                    print("Added: %s and allocated them to %s: " % (new_fellow.person_name, random_ls))

                #when person type is a Fellow"""
            elif person_type == 'F':
                new_fellow = Fellow(person_id, person_name)
                self.all_people[new_fellow.person_name] = person_type
                self.fellows.append(new_fellow.person_name)
                random_office = self.generate_random_office()

                if not random_office:
                    self.unallocated_person[new_fellow.person_name] = person_type
                    print('Added %s to the unallocated list' % new_fellow.person_name)
                else:
                    self.office_rooms[random_office].append(new_fellow.person_name)
                    print("Added: %s and allocated them to %s: " % (new_fellow.person_name, random_office))

            elif person_type == 'S' and wants_accomodation == 'Y':
                new_staff = Staff(person_id, person_name)
                self.all_people[new_staff.person_name] = person_type
                self.staffs.append(new_staff.person_name)
                random_office = self.generate_random_office()

                if not random_office:
                    self.unallocated_person[new_staff.person_name] = person_type
                    print('Staff cannot be located a living space')
                else:
                    self.office_rooms[random_office].append(new_staff.person_name)
                    print('Staff cannot be located a living space')

                #When the person is a Staff
            elif person_type == 'S':
                new_staff = Staff(person_id, person_name)
                self.all_people[new_staff.person_name] = person_type
                self.staffs.append(new_staff.person_name)
                random_office = self.generate_random_office()
                if not random_office:
                    self.unallocated_person[new_staff.person_name] = person_type
                    print('Added %s to the unallocated list' % new_staff.person_name)
                else:
                    self.office_rooms[random_office].append(new_staff.person_name)
                    print("Added: %s and allocated them to %s: " % (new_staff.person_name, random_office))

            else:
                print('%s is not a valid position.' % person_type)

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



