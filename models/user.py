#!usr/bin/python3
""" User class. """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from BaseModel. """
    def __init__(self, *args, **kwargs):
        """ Initializes a new User instance. """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
