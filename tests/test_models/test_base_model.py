#!/usr/bin/python3
""" Unit test for Base class. """
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from unittest.mock import patch, Mock


class TestBaseModel(unittest.TestCase):
    """ Test the BaseModel class. """

    def setUp(self):
        """ Set up each test. """
        self.base = BaseModel()

    def test_id(self):
        """ Check if 'id' is a string. """
        self.assertTrue(isinstance(self.base.id, str))

    def test_ids(self):
        """ Check id creation. """
        i = BaseModel()
        j = BaseModel()
        self.assertTrue(i.id != j.id)

    def test_created_at(self):
        """ Check if 'created_at' is a datetime. """
        self.assertTrue(isinstance(self.base.created_at, datetime))

    def test_updated_at(self):
        """ Check if 'updated_at' is a datetime. """
        self.assertTrue(isinstance(self.base.updated_at, datetime))

    def test_str(self):
        """ Check the string representation of BaseModel. """
        base_str = f"[BaseModel] ({self.base.id}) {self.base.__dict__}"
        self.assertEqual(str(self.base), base_str)

    def test_save(self):
        """ Check the 'save' method. """
        initial_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(initial_updated_at, self.base.updated_at)

    def test_to_dict(self):
        """ Check the 'to_dict' method. """
        obj = self.base.to_dict()
        self.assertTrue(isinstance(obj, dict))
        self.assertEqual(obj['__class__'], 'BaseModel')
        self.assertTrue('id' in obj)
        self.assertTrue('created_at' in obj)
        self.assertTrue('updated_at' in obj)

        created_at_str = self.base.created_at.isoformat()
        updated_at_str = self.base.updated_at.isoformat()
        self.assertEqual(obj['created_at'], created_at_str)
        self.assertEqual(obj['updated_at'], updated_at_str)

    def test_init(self):
        """ Test initialization. """
        self.assertTrue(isinstance(self.base.id, str))
        self.assertTrue(isinstance(self.base.created_at, datetime))
        self.assertTrue(isinstance(self.base.updated_at, datetime))

    def test_init_with_kwargs(self):
        """ Test initialization with kwargs. """
        kwargs = {
            'id': 'test',
            'created_at': '1995-01-31T10:00:00',
            'updated_at': '1995-01-31T11:00:00',
            'name': 'Test'
        }
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, 'test')
        self.assertTrue(isinstance(obj.created_at, datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime))
        self.assertEqual(obj.name, 'Test')

    def test_save_calls_storage(self):
        """ Check if 'save' calls storage. """
        with patch.object(storage, 'save') as mock_save:
            self.base.save()
            mock_save.assert_called_once_with()

    def test_kwargs_calls_storage(self):
        """ Check if 'new' is called when initializing with kwargs. """
        kwargs = {
            'id': 'test',
            'created_at': '1995-01-31T10:00:00',
            'updated_at': '1995-01-31T11:00:00',
            'name': 'Test'
        }
        with patch.object(storage, 'new') as mock_new:
            obj = BaseModel(**kwargs)
            mock_new.assert_called_once_with(obj)


if __name__ == '__main__':
    unittest.main()
