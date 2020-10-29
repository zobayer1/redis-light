# -*- coding: utf-8 -*-
from redisorm.fields.field import Field


class ORMMeta(type):
    """Metaclass for redis-orm"""

    def __new__(mcs, name, bases, namespace):
        """Metaclass magic method

        Gathers all instances of Field into a new class variable called _fields. All field instances are also removed
        from the class dictionary.

        :param name: name of the class
        :param bases: tuple of base classes
        :param namespace: dictionary of all fields
        """
        fields = {_name: _field for _name, _field in namespace.items() if isinstance(_field, Field)}
        c_namespace = namespace.copy()
        for _name in fields.keys():
            del c_namespace[_name]
        c_namespace["fields"] = fields
        return super().__new__(mcs, name, bases, c_namespace)
