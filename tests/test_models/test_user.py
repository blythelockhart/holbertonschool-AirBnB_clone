#!usr/bin/python3
""" Unit test for User class. """
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Test the User class. """
    def setUp(self):
        user = User()

    def test_inheritance(self):
        """ Test if User inherits from BaseModel. """
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """ Test the attributes of the User class. """
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_email(self):
        """ Test the 'email' attribute. """
        self.assertTrue(isinstance(user.email, str))

    def test_password(self):
        """ Test the 'password' attribute. """
        self.assertTrue(isinstance(user.password, str))

    def test_first_name(self):
        """ Test the 'first_name' attribute. """
        self.assertTrue(isinstance(user.first_name, str))

    def test_last_name(self):
        """ Test the 'last_name' attribute. """
        self.assertTrue(isinstance(user.last_name, str))

    def test_str(self):
        """ Test the string representation of User. """
        self.assertEqual(str(user), "[User] ({}) {}".format(user.id, user.__dict__))


if __name__ == '__main__':
    unittest.main()
