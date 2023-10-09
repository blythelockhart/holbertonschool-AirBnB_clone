#!usr/bin/python3
""" Unit test for Amenity class. """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Test the Amenity class. """
    def setUp(self):
        amenity = Amenity()

    def test_inheritance(self):
        """ Test if Amenity inherits from BaseModel. """
        self.assertIsInstance(amenity, BaseModel)

    def test_name(self):
        """ Test the attributes of the Amenity class. """
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_name_type(self):
        """ Test the data type of the 'name' attribute. """
        self.assertTrue(isinstance(amenity.name, str))

    def test_str(self):
        """ Test the string representation of Amenity. """
        self.assertEqual(str(amenity), "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__))


if __name__ == '__main__':
    unittest.main()
