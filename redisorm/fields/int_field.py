# -*- coding: utf-8 -*-
from redisorm.fields.field import Field


class IntField(Field):
    """Integer type field"""

    def __init__(
        self, default_value: int = 0, minimum_value: int = None, maximum_value: int = None, required: bool = False
    ):
        """Creates an integer field

        :param default_value: default value
        :param minimum_value: minimum value
        :param maximum_value: maximum value
        :param required: required flag
        """
        super().__init__(default_value, required)
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value

    def validate(self, value: int) -> bool:
        """Validation method

        :param value: value for validation
        :return: True if validated, False otherwise
        """
        return super().validate(value) and (value is None or (isinstance(value, int) and self._validate_range(value)))

    def _validate_range(self, value: int) -> bool:
        """Range validation method

        :param value: value for validation
        :return: True if validated, False otherwise
        """
        return (self.minimum_value is None or value >= self.minimum_value) and (
            self.maximum_value is None or value <= self.maximum_value
        )
