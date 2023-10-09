#!usr/bin/python3
""" Unit test for City class. """
import unittest
from datetime import datetime
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    """ Test the City class. """

    def setUp(self):
        self.state = State()
        self.city = City()

    def test_state_id(self):
        """ Check if 'state_id' is initialized empty. """
        self.assertEqual(self.city.state_id, "")

    def test_name(self):
        """ Check if 'name' is initialized empty. """
        self.assertEqual(self.city.name, "")

    def test_state_id_new(self):
        """ Check if 'state_id' can be assigned. """
        self.city.state_id = self.state.id
        self.assertEqual(self.city.state_id, self.state.id)

    def test_name_new(self):
        """ Check 'name' can be assigned. """
        self.city.name = "Los Angeles"
        self.assertEqual(self.city.name, "Los Angeles")

    def test_created_at(self):
        """ Check if 'created_at' is a datetime. """
        self.assertTrue(isinstance(self.city.created_at, datetime))

    def test_updated_at(self):
        """ Check if 'updated_at' is a datetime. """
        self.assertTrue(isinstance(self.city.updated_at, datetime))

    def test_str(self):
        """ Check the string representation of City. """
        city_str = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), city_str)

    def test_save(self):
        """ Check if 'save' updates. """
        initial_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(initial_updated_at, self.city.updated_at)

    def test_to_dict(self):
        """ Check the 'to_dict' method. """
        obj = self.city.to_dict()
        self.assertTrue(isinstance(obj, dict))
        self.assertEqual(obj['__class__'], 'City')
        self.assertTrue('id' in obj)
        self.assertTrue('created_at' in obj)
        self.assertTrue('updated_at' in obj)
        self.assertTrue('state_id' in obj)
        self.assertTrue('name' in obj)

        created_at_str = self.city.created_at.isoformat()
        updated_at_str = self.city.updated_at.isoformat()
        self.assertEqual(obj['created_at'], created_at_str)
        self.assertEqual(obj['updated_at'], updated_at_str)

if __name__ == '__main__':
    unittest.main()
