# -*- coding: utf-8 -*-
from datetime import datetime

from redisorm.fields.field import Field


class DateField(Field):
    """Date type field"""

    def __init__(self, default_value: datetime = None, required: bool = False):
        """Creates a date field of python datetime type

        :param default_value: default value
        :param required: required flag
        """
        super().__init__(default_value, required)

    def validate(self, value: datetime) -> bool:
        """Validation method

        :param value: value for validation
        :return: True if validated, False otherwise
        """
        return super().validate(value) and (value is None or isinstance(value, datetime))
