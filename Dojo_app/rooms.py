import Dojo_app
class Room(object):

    def __init__(self, room_name, room_type, max_occupants):
        self.room_type = room_type
        self.room_name = room_name
        self.max_occupants = max_occupants

class Office(Room):
    def __init__(self, *args):
        super(Office, self).__init__(*args, room_type='O', max_occupants=6)

class LivingSpace(Room):
    def __init__(self, *args):
        super(LivingSpace, self).__init__(*args, room_type='L', max_occupants=4)


