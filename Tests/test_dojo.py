import unittest
from Dojo_app.dojo import *


class Test_Dojo(unittest.TestCase):

    def setUp(self):
        Dojo.office_rooms = []
        Dojo.lspace_rooms = []
        Dojo.all_rooms = {}
        Dojo.staffs = []
        Dojo.fellows = []
        Dojo.all_people = {}
        Dojo.unallocated_person = []

    def test_room_does_not_exist(self):
        Dojo.create_room('blue', 'O')
        self.assertTrue('blue' in Dojo.all_rooms)
        response = Dojo.create_room('blue', 'O')
        self.assertEqual(response, "The Room already exists")

    def test_create_office(self):
        previous_room_count = len(Dojo.all_rooms)
        self.assertFalse('blue' in Dojo.all_rooms)
        Dojo.create_room('blue', 'O')
        self.assertTrue('blue'.upper() in Dojo.all_rooms)
        new_room_count = len(Dojo.all_rooms)
        self.assertEqual(previous_room_count + 1, new_room_count)


    def test_reallocate_person(self):
        Dojo.create_room('violet', 'l')
        Dojo.create_room('orange', 'O')
        Dojo.add_person('ray atuhe', 'F'['green'])
        Dojo.create_room('GO', 'l')
        Dojo.reallocate_person_to_ls('ray atuhe', 'orange')
        self.assertIn('ray atuhe', Dojo.ls_rooms['GO'])
        self.assertNotIn('STEVE KANYI', Dojo.ls_rooms['PHP'])

