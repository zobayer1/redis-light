# -*- coding: utf-8 -*-
import json

from redisorm.orm_meta import ORMMeta


class ORMBase(metaclass=ORMMeta):
    """User interface for the base class"""

    def __init__(self, from_dict: dict = None):
        """Base method for crating an orm object

        :param from_dict: dictionary object containing field values
        """
        for name, field in self.fields.items():
            setattr(self, name, field.default_value)

        if from_dict:
            if not isinstance(from_dict, dict):  # pragma: no cover
                raise RuntimeError("Param from_dict must be a dictionary object")
            for field, value in from_dict.items():
                setattr(self, field, value)

    def __setattr__(self, key, value):
        """Magic method setter"""
        if key in self.fields:
            if self.fields[key].validate(value):
                super().__setattr__(key, value)
            else:
                raise AttributeError('Invalid value "{}" for field "{}"'.format(value, key))
        else:
            raise AttributeError('Unknown field "{}"'.format(key))

    def __repr__(self):
        """Convert to JSON string"""
        _dict = dict()
        for name in self.fields.keys():
            _dict[name] = getattr(self, name)
        return json.dumps(_dict)
