import unittest
from app.dojo import *
from app.person import *
from app.rooms import *

class Test_Dojo(unittest.TestCase):

    def setUp(self):
        self.office_rooms = []
        self.lspace_rooms = []
        self.all_rooms = {}
        self.staffs = []
        self.fellows = []
        self.all_people = {}
        self.unallocated_person = []
        self.office = Office('D100', 'O', 6)
        self.living_space = LivingSpace(...)

    def test_room_does_not_exist(self):
        self.office.create_room('blue', 'O')
        self.assertTrue('blue' in self.all_rooms)
        response = self.create_room('blue', 'O')
        self.assertEqual(response, "The Room already exists")
