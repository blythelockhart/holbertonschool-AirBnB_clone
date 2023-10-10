#!usr/bin/python3
""" Unit test for State class. """
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ Test the State class. """
    def setUp(self):
        """ Set up each test. """
        state = State()

    def test_inheritance(self):
        """ Test if State inherits from BaseModel. """
        self.assertIsInstance(state, BaseModel)

    def test_name(self):
        """ Test the attributes of State class. """
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_name_type(self):
        """ Test the data type of 'name'. """
        self.assertTrue(isinstance(state.name, str))

    def test_str(self):
        """ Test the string representation of State. """
        self.assertEqual(
            str(state),
            "[State] ({}) {}".format(state.id, state.__dict__)
        )


if __name__ == '__main__':
    unittest.main()
