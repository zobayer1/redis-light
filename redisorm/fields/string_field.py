# -*- coding: utf-8 -*-
from redisorm.fields.field import Field


class StringField(Field):
    """String type field"""

    def __init__(
        self, default_value: str = None, minimum_length: int = None, maximum_length: int = None, required: bool = False
    ):
        """Creates a string field

        :param default_value: default value
        :param minimum_length: minimum string length
        :param maximum_length: maximum string length
        :param required: required flag
        """
        super().__init__(default_value, required)
        self.minimum_length = minimum_length
        self.maximum_length = maximum_length

    def validate(self, value: str) -> bool:
        """Validation method

        :param value: value for validation
        :return: True if validated, False otherwise
        """
        return super().validate(value) and (value is None or (isinstance(value, str) and self._validate_length(value)))

    def _validate_length(self, value: str) -> bool:
        """Length validation method

        :param value: value for validation
        :return: True if validated, False otherwise
        """
        return (self.minimum_length is None or len(value) >= self.minimum_length) and (
            self.maximum_length is None or len(value) <= self.maximum_length
        )
