#!/usr/bin/python3
"""module for Base Model class"""

import uuid
from datetime import datetime


class BaseModel():
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        """initilization with id, created_at and updated_at"""
        self.id = str(uuid.uuid4()) #uses uuid4 to create unique id and converts to string
        self.created_at = datetime.now()
        self.updated_at = datetime.now() #created_at and updated_at are set to current time

    def __str__(self):
        """returns string rep of BaseModle instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dictionary of all keys/values of __dict__"""
        obj_dict = self.__dict__.copy() #creats a copy of __dict__
        obj_dict['__class__'] = self.__class__.__name__ #adds the class name to obj_dict

        obj_dict['created_at'] = self.created_at.isoformat() #formats created_at and updated_at,
        obj_dict['updated_at'] = self.updated_at.isoformat() #then adds them to obj_dict

        return obj_dict
