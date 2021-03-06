# -*- coding: utf-8 -*-
import json
from typing import Any

from redisorm.fields import isormfield


class _ORMMeta(type):
    """Metaclass for redis-orm"""

    def __new__(mcs, name: str, bases: tuple, namespace: dict):
        """Metaclass magic method

        Gathers all instances of `_FieldBase` into a new class variable called `fields`. All field instances are also
        removed from the class dictionary.

        :param name: name of the class
        :param bases: tuple of base classes
        :param namespace: dictionary of all fields
        """
        fields = {_name: _field for _name, _field in namespace.items() if isormfield(_field)}
        c_namespace = namespace.copy()
        for _name in fields.keys():
            del c_namespace[_name]
        c_namespace["fields"] = fields
        return super().__new__(mcs, name, bases, c_namespace)


class _ORMBase(metaclass=_ORMMeta):
    """User interface for the base class"""

    def __init__(self, from_dict: dict = None):
        """Base method for crating an orm object

        :param from_dict: dictionary object containing field values, default `None`
        :raises:
            :RuntimeError: when `from_dict` parameter is not an instance of `dict`
            :AttributeError: for unexpected field or value in `from_dict`
        """
        for name, field in self.fields.items():
            setattr(self, name, field.default_value)

        if from_dict:
            if not isinstance(from_dict, dict):
                raise RuntimeError("Param from_dict must be a dictionary object")
            for field, value in from_dict.items():
                setattr(self, field, value)

    def __setattr__(self, key: str, value: Any):
        """Magic method setter

        :param key: attribute name
        :param value: attribute value
        :returns: nothing
        :raises: :AttributeError: for unexpected field or value
        """
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


class AtomicBase(_ORMBase):
    """Wrapper class for atomic string value"""

    pass


class StringBase(_ORMBase):
    """Wrapper class for string value"""

    pass


class HashBase(_ORMBase):
    """Wrapper class for hash mapped value"""

    pass


class SetBase(_ORMBase):
    """Wrapper class for set element"""

    pass


class SortedSetBase(_ORMBase):
    """Wrapper class for sorted set element"""

    pass


class ListBase(_ORMBase):
    """Wrapper class for list element"""

    pass


__all__ = [
    "AtomicBase",
    "StringBase",
    "HashBase",
    "SetBase",
    "SortedSetBase",
    "ListBase",
]
