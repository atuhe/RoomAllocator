class Room(object):

    def __init__(self, room_name, room_type, max_occupants):
        self.room_type = room_type
        self.room_name = room_name
        self.max_occupants = max_occupants

class Office(Room):
    def __init__(self, room_name):
        self.room_name = room_name
        self.room_type = "office"
        self.max_occupants = 6

class LivingSpace(Room):
    def __init__(self, room_name):
        self.room_name = room_name
        self.room_type = "livingspace"
        self.max_occupants = 4






