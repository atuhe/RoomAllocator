import unittest
from unittest import TestCase
from app.person import *
from app.rooms import *


class Tests(unittest.TestCase):
   def setup(self):
        self.create_room = Tests()

   def test_room_is_office(self):
        office1 = Office('blue')
        self.assertEqual(office1.room_type, 'office')

    #Test for maximum living_space occupants
   def test_max_living_space_occupants(self):
        ls1 = LivingSpace('green')
        self.assertEqual(ls1.max_occupants, 4)

    #Test for if room is living_space
   def test_room_is_lspace(self):
        Space = LivingSpace('green')
        self.assertEqual(Space.room_type, 'livingspace')



