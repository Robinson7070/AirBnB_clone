#!/usr/bin/python
"""
Module for BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
            if not hasattr(self, 'id'):
                self.id = str(uuid.uuid4())
            if not hasattr(self, 'created_at'):
                self.created_at = datetime.now()
            if not hasattr(self, 'updated_at'):
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance.
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
