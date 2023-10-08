#!/usr/bin/python3
"""module for Base Model class"""

import uuid
from datetime import datetime


class BaseModel():
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initilization with id, created_at and updated_at"""
        if kwargs:  # kwargs is not empty
            for key, value in kwargs.items():
                # uses the key, value pairs to assign attributes
                if key != '__class__':
                    # __class__ is not made into an attribute
                    if key == 'created_at' or key == 'updated_at':
                        # convertes created_at and updated_at from a string
                        format = "%Y-%m-%dT%H:%M:%S.%f"
                        setattr(self, key, datetime.strptime(value, format))
                    else:
                        setattr(self, key, value)
        else:
            # uses uuid4 to create unique id and converts to string
            self.id = str(uuid.uuid4())
            # created_at and updated_at are set to current time
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """returns string rep of BaseModle instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dictionary of all keys/values of __dict__"""
        # creats a copy of __dict__
        obj_dict = self.__dict__.copy()
        # adds the class name to obj_dict
        obj_dict['__class__'] = self.__class__.__name__
        # formats created_at and updated_at, then adds them to obj_dict
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
