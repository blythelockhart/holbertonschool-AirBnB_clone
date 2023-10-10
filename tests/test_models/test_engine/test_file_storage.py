#!usr/bin/python3
""" Unit test for File Storage. """
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """ Test the FileStorage class. """
    def setUp(self):
        """ Set up each test. """
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """ Clean up after each test. """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_attributes(self):
        """ Test the attributes of the FileStorage class. """
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """ Test the 'all' method. """
        all_objects = self.storage.all()
        self.assertEqual(type(all_objects), dict)
        self.assertEqual(all_objects, {})

    def test_new(self):
        """ Test the 'new' method. """
        obj = BaseModel()
        self.storage.new(obj)
        self.assertTrue(isinstance(self.storage._FileStorage__objects, dict))
        self.assertIn(
            "BaseModel." + obj.id,
            self.storage._FileStorage__objects
        )

    def test_save(self):
        """ Test the 'save' method. """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r") as file:
            saved_data = json.load(file)
        self.assertIn("BaseModel." + obj.id, saved_data)

    def test_reload(self):
        """ Test the 'reload' method. """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertTrue(isinstance(all_objects, dict))
        self.assertIn("BaseModel." + obj.id, all_objects)

    def test_reload_no_file(self):
        """ Test the 'reload' method with nonexistent file. """
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertTrue(isinstance(all_objects, dict))
        self.assertEqual(all_objects, {})

    def test_reload_invalid_json(self):
        """ Test the 'reload' method with invalid JSON in file. """
        with open(self.file_path, "w") as file:
            file.write("invalid json data")
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertTrue(isinstance(all_objects, dict))
        self.assertEqual(all_objects, {})

    def test_reload_empty_json(self):
        """ Test the 'reload' method with empty JSON file. """
        with open(self.file_path, "w") as file:
            file.write("{}")
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertTrue(isinstance(all_objects, dict))
        self.assertEqual(all_objects, {})

    def test_reload_user(self):
        """ Test the 'reload' method with User. """
        user = User()
        self.storage.new(user)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertTrue(isinstance(all_objects, dict))
        self.assertIn("User." + user.id, all_objects)


if __name__ == '__main__':
    unittest.main()
