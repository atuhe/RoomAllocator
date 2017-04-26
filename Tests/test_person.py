import unittest
from unittest import TestCase
from Dojo_app.dojo import *
from Dojo_app.rooms import *

class TestPerson(TestCase):

    def test_person_type_is_fellow(self):
        fellow1 = Fellow(2, 'ray atuhe')
        self.assertEqual(fellow1.person_type, 'F')

    def test_person_type_is_staff(self):
        staff1 = Staff(3, 'Lydia Ashaba')
        self.assertEqual(staff1.person_type, 'S')

