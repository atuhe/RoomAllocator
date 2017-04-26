from Dojo_app.person import *
from Dojo_app.rooms import *


class Dojo(object):


    @staticmethod
    def create_room(room_name, room_type):
            '''
            Loop through the Dojo, determine if room does not exist and what type of room it is
            '''
            if room_name in Dojo.all_rooms:
                print('Room already exists')
            elif room_type.upper() == 'O':
                current_room = Office(room_name)
                Dojo.all_rooms[current_room.room_name.upper()] = current_room.room_type
                Dojo.office_rooms[current_room.room_name.upper()]
                print('%s created succesfully' % room_name)

            elif room_type.upper() == 'L':
                current_room = LivingSpace(room_name)
                Dojo.all_rooms[current_room.room_name.upper()] = current_room.room_type
                Dojo.ls_rooms[current_room.room_name.upper()]
                print('%s created succesfully' % room_name)
            else:
                print('%s is an invalid room type' % room_type)

    @staticmethod
    def add_person(person_id, person_name, person_type, wants_accomodation='N'):
            '''
            create details of a person in the Dojo
            '''
            person_id = len(list(Dojo.all_people)) + 1

            if person_name.upper() in Dojo.all_people:
                print ('Person with %s id already exist.' % person_name)

            elif person_type.upper() == 'F' and wants_accomodation.upper() == 'Y':
                new_fellow = Fellow(person_id, person_name)
                Dojo.all_people[new_fellow.person_name.upper()] = person_type
                Dojo.fellows.append(new_fellow.person_name.upper())
                '''
                    generate a random room i.e. office or living_space in the Dojo
                '''
                random_office = Dojo.generate_random_office()
                random_space = Dojo.generate_random_living_space()
                '''
                    persons not assigned rooms
                '''
                if not random_office and not random_space:
                    Dojo.unallocated_person[new_fellow.person_name.upper()] = person_type
                    print('Added %s to the unallocated list' % new_fellow.person_name)

                elif not random_office and random_space:
                    Dojo.unallocated_person[new_fellow.person_name.upper()] = person_type
                    print('Added %s to the unallocated list' % new_fellow.person_name)
                    Dojo.living_space_rooms[random_space].append(new_fellow.person_name.upper())
                    print("Added: %s and allocated them to a living space %s: " % (new_fellow.person_name, random_space))

                elif not random_space and random_office:
                    Dojo.unallocated_person[new_fellow.person_name.upper()] = person_type
                    print('Added %s to the unallocated list' % new_fellow.person_name)
                    Dojo.office_rooms[random_office].append(new_fellow.person_name.upper())
                    print("Added: %s and allocated them to an office %s: " % (new_fellow.person_name, random_office))

                else:
                    Dojo.office_rooms[random_office].append(new_fellow.person_name.upper())
                    print("Added: %s and allocated them to %s: " % (new_fellow.person_name, random_office))
                    Dojo.ls_rooms[random_space].append(new_fellow.person_name.upper())
                    print("Added: %s and allocated them to %s: " % (new_fellow.person_name, random_space))

            elif person_type.upper() == 'F':
                new_fellow = Fellow(person_id, person_name)
                Dojo.all_people[new_fellow.person_name.upper()] = person_type
                Dojo.fellows.append(new_fellow.person_name.upper())
                random_office = Dojo.generate_random_office()
                if not random_office:
                    Dojo.unallocated_person[new_fellow.person_name.upper()] = person_type
                    print('Added %s to the unallocated list' % new_fellow.person_name)
                else:
                    Dojo.office_rooms[random_office].append(new_fellow.person_name.upper())
                    print("Added: %s and allocated them to %s: " % (new_fellow.person_name, random_office))

            elif person_type.upper() == 'S' and wants_accomodation.upper() == 'Y':
                new_staff = Staff(person_id, person_name)
                Dojo.all_people[new_staff.person_name.upper()] = person_type
                Dojo.staffs.append(new_staff.person_name)
                random_office = Dojo.generate_random_office()
                if not random_office:
                    Dojo.unallocated_person[new_staff .person_name.upper()] = person_type
                    print('Added %s to the unallocated list' % new_staff.person_name)
                    print('Staff cannot be llocated a living space')
                else:
                    Dojo.office_rooms[random_office].append(new_staff.person_name.upper())
                    print("Added: %s and allocated them to %s: " % (new_staff.full_name, random_office))
                    print('Staff cannot be llocated a living space')

            elif person_type.upper() == 'S':
                new_staff = Staff(person_id, person_name)
                Dojo.all_people[new_staff.person_name.upper()] = person_type
                Dojo.staffs.append(new_staff.person_name.upper())
                random_office = Dojo.generate_random_office()
                if not random_office:
                    Dojo.unallocated_person[new_staff.full_name.upper()] = person_type
                    print('Added %s to the unallocated list' % new_staff.full_name)
                else:
                    Dojo.office_rooms[random_office].append(new_staff.person_name.upper())
                    print("Added: %s and allocated them to %s: " % (new_staff.person_name, random_office))

            else:
                print('%s is not a valid position.' % person_type)
