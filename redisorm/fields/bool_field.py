# -*- coding: utf-8 -*-
from redisorm.fields.field import Field


class BoolField(Field):
    """Boolean type field"""

    def __init__(self, default_value: bool = False, required: bool = False):
        """Creates a boolean field

        :param default_value: default value
        :param required: required flag
        """
        super().__init__(default_value, required)

    def validate(self, value: bool) -> bool:
        """Validation method

        :param value: value for validation
        :return: True if validated, False otherwise
        """
        return super().validate(value) and (value is None or isinstance(value, bool))
