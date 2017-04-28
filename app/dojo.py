import os
import sqlite3

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
                    print(" A {0} {0} has been successfully created!".format(room_type, room_name))

        def add_person(self, person_name, person_type, wants_accomodation):
            if not wants_accomodation:
                wants_accomodation = 'N'
            else:
                wants_accomodation = wants_accomodation.upper()
            print("Creating a person")

             #Add person to the dojo
            if person_name in [person for person in self.all_people if person.person_name == person_name]:
                print("person {0} already exists".format(person_name))
                return

            if person_type == 'fellow':
                    new_fellow = Fellow(person_name)
                    print("Fellow {0} has been created succesfully!".format(person_name))
                    new_fellow.allocate_office(self.all_rooms)
                    self.all_people.append(new_fellow)
            elif person_type == 'staff':
                    new_staff = Staff(person_name)
                    print("Staff {0} has been created succesfully".format(person_name))
                    new_staff.allocate_office(self.all_rooms)
                    self.all_people.append(new_staff)

        def print_room(self, room_name):

            # prints a room and all the people allocated to that room
            new_room = [x for x in self.all_rooms]
            # if x.room_name == room_name
            print(room_name)

            # if len(new_room) > 0:
            for room_name in new_room:
                print("The following people are in room %s" % room_name.room_name)
                for y in [person for person in room_name.occupants]:
                    print(y.person_name)
            # else:
            #     print("Rooom has no new added persons ")

         #checkout allocations
        def print_allocations(self, x):
            if len(self.all_rooms) < 1:
                print("No rooms registered")
                return
            else:
                for my_room in self.all_rooms:
                    print()
                    print(my_room.room_name.upper())
                    occupants = []
                    for occupant in my_room.occupants:
                        occupants.append(occupant.person_name)
                    print(', '.join(occupants))

                    # Create a txt file if the filename argument is passed
                    if x is not None:
                        filename = open (x + ".txt", "w")
                        for roomY in self.all_rooms:
                            filename.write ("\n")
                            filename.write (roomY.room_name.upper ())
                            filename.write ("\n------------------------------\n")
                            occupants = []
                            for occupant in roomY.occupants:
                                occupants.append (occupant.person_name)
                            filename.write (', '.join (occupants) + "\n")
                        filename.close ()
                        # Open the text_file with the default application
                        os.startfile(x + ".txt")

        def load_people(self):
            for line in open("text_file.txt"):
                line.strip()
                data_row = line.split()
                last_param = data_row[-1]
                person_name = ' '.join(data_row[0:2])
                if len(last_param) == 1:
                    wants_accommodation = data_row[-1]
                    person_type = data_row[-2]
                else:
                    wants_accommodation = "F"
                    person_type = data_row[-1]
                self.add_person(person_name, person_type, wants_accommodation)


        #defining a database
        def save_state(self, database_name):
            if database_name is not None:
                conn = sqlite3.connect(database_name + ".db")
            else:
                conn = sqlite3.connect('dojo.db')
            c = conn.cursor()

            # Creating a Person Table in dojo databse
            c.execute('''CREATE TABLE IF NOT EXISTS person
            (person_id TEXT PRIMARY KEY NOT NULL,
            person_name TEXT NOT NULL,
            person_type TEXT NOT NULL,
            opt_int INT     
            )''')

            # Creating rooms Table in dojo database
            c.execute('''create table if not exists room
                    (room_name text primary key not null,
                    room_type text not null,
                    max_occupants text not null
                    )''')
            #
            # # Create Table Occupant
            c.execute('''CREATE TABLE IF NOT EXISTS occupant
                    (person_id TEXT NOT NULL,
                    room_name TEXT NOT NULL
                    )''')

            # Save Room Data
            c.execute('DELETE FROM occupant')
            for room in self.all_rooms:
                if isinstance (room, Office):
                    room_type = "office"
                else:
                    room_type = "living_space"
                data_list = [room.room_name, room_type, room.max_occupants]
                c.execute ('INSERT OR REPLACE INTO room VALUES (?, ?, ?)', data_list)
                # Save Occupants Data
                for occupant in room.occupants:
                    data_list = [occupant.person_id, room.room_name]
                    c.execute ('INSERT INTO occupant VALUES (?, ?)', data_list)

            conn.commit()
            print ("Data saved successfully")
            conn.close ()

        def load_state(self, db_name):
            try:
                conn = sqlite3.connect (db_name + ".db")
                c = conn.cursor ()

                # Load People
                c.execute ('''SELECT * FROM person''')
                people = c.fetchall ()
                for person in people:
                    person_id = person[0]
                    person_name = person[1]
                    person_type = person[2]
                    opt_in = bool (person[3])
                    if person_type == "staff":
                        new_person = Staff (person_name)
                        self.all_people.append (new_person)
                    elif person_type == "fellow":
                        new_person = Fellow (person_name,)
                        self.all_people.append (new_person)
                    else:
                        print ("Invalid person type")
            except sqlite3.OperationalError:
                print ("Invalid database name!")

            print("Data loaded successfully")
            conn.close ()
