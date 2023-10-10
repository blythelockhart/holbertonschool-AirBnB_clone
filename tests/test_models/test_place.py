#!usr/bin/python3
""" Unit test for Place class. """
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Test the Place class. """
    def setUp(self):
        """ Set up each test. """
        place = Place()

    def test_inheritance(self):
        """ Test if Place inherits from BaseModel. """
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """ Test the attributes of the Place class. """
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])

    def test_city_id(self):
        """ Test the 'city_id'. """
        self.assertTrue(isinstance(place.city_id, str))

    def test_user_id(self):
        """ Test the 'user_id'. """
        self.assertTrue(isinstance(place.user_id, str))

    def test_name(self):
        """ Test the 'name'. """
        self.assertTrue(isinstance(place.name, str))

    def test_description(self):
        """ Test the 'description'. """
        self.assertTrue(isinstance(place.description, str))

    def test_number_rooms(self):
        """ Test the 'number_rooms'. """
        self.assertTrue(isinstance(place.number_rooms, int))

    def test_number_bathrooms(self):
        """ Test the 'number_bathrooms'. """
        self.assertTrue(isinstance(place.number_bathrooms, int))

    def test_max_guest(self):
        """ Test the 'max_guest'. """
        self.assertTrue(isinstance(place.max_guest, int))

    def test_price_by_night(self):
        """ Test the 'price_by_night'. """
        self.assertTrue(isinstance(place.price_by_night, int))

    def test_latitude(self):
        """ Test the 'latitude'. """
        self.assertTrue(isinstance(place.latitude, float))

    def test_longitude(self):
        """ Test the 'longitude'. """
        self.assertTrue(isinstance(place.longitude, float))

    def test_amenity_ids(self):
        """ Test the 'amenity_ids'. """
        self.assertTrue(isinstance(place.amenity_ids, list))

    def test_str(self):
        """ Test the string representation of Place. """
        self.assertEqual(
            str(place),
            "[Place] ({}) {}".format(place.id, place.__dict__)
        )


if __name__ == '__main__':
    unittest.main()
