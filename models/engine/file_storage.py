#!/usr/bin/python3
"""Module for serializing / deseralizing instances to / from JSON files"""


import json


class FileStorage:
    """serialize instance to JSON file / deserialize JSON file to instance"""
    def __init__(self):
        """initilzation for file path and objects dictionary"""
        self.__file_path = "file.json"  # path to the JSON file
        self.__objects = {}  # will store all objects by <class name>.id

    def all(self):
        """returns __objects directory"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        # makes the key
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        # saves the key : obj pair to __objects dictionary
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serialized_objs = {}
        # converts objects in __objects to their dict rep
        # and adds them to serialized_objs
        for key, value in self.__objects.items():
            serialized_objs[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                      "City": City, "Place": Place,
                      "Review": Review, "Amenity": Amenity}
        try:
            with open(self.__file_path, "r") as file:
                # loads serialized objecs and sets them as data
                # data should be a dictionary of dict reps of objects
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name in class_dict:  # find class
                        instance_class = class_dict[class_name]
                    obj = instance_class(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
