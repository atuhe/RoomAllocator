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

    def test_dojo_object_is_a_dictionary(self):
        some_object = self
        self.assertTrue(isinstance(self.some_dojo, dict), msg='The Dojo class is not creating dictionary objects')

    def test_dojo_object_has_office_spaces_dictionary(self):
        self.assertEqual(type(self.some_dojo['office_spaces']), dict,
                         msg='The Dojo object has no office_spaces dictionary')

    def test_dojo_object_has_living_spaces_dictionary(self):
        self.assertEqual(type(self.some_dojo['living_spaces']), dict,
                         msg='The Dojo object has no living_spaces dictionary')

    def test_create_office(self):
        previous_room_count = len(self.all_rooms)
        self.assertFalse('blue' in self.all_rooms)
        self.create_room('blue', 'O')
        self.assertTrue('blue'.upper() in self.all_rooms)
        new_room_count = len(self.all_rooms)
        self.assertEqual(previous_room_count + 1, new_room_count)


    def test_reallocate_person(self):
        self.create_room('violet', 'l')
        self.create_room('orange', 'O')
        self.add_person('ray atuhe', 'F'['green'])
        self.create_room('GO', 'l')
        self.reallocate_person_to_ls('ray atuhe', 'orange')
        self.assertIn('ray atuhe', self.ls_rooms['GO'])
        self.assertNotIn('STEVE KANYI', self.ls_rooms['PHP'])

