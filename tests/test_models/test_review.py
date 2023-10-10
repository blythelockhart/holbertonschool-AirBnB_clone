#!usr/bin/python3
""" Unit test for Review class. """
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Test the Review class. """
    def setUp(self):
        """ Set up each test. """
        review = Review()

    def test_inheritance(self):
        """ Test if Review inherits from BaseModel. """
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """ Test the attributes of the Review class. """
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

    def test_place_id(self):
        """ Test the 'place_id' attribute. """
        self.assertTrue(isinstance(review.place_id, str))

    def test_user(self):
        """ Test the 'user_id' attribute. """
        self.assertTrue(isinstance(review.user_id, str))

    def test_text(self):
        """ Test the 'text' attribute. """
        self.assertTrue(isinstance(review.text, str))

    def test_str(self):
        """ Test the string representation of Review. """
        self.assertEqual(
            str(review),
            "[Review] ({}) {}".format(review.id, review.__dict__)
        )


if __name__ == '__main__':
    unittest.main()
