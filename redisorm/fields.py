# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Callable


class _Field(object):
    """Base class for all field types"""

    def __init__(self, default_value=None, required: bool = False):
        """Creates a _Field object with a default value

        :param default_value: default value for this field
        :param required: required flag
        """
        self.default_value = default_value
        self.required = required

    def validate(self, value) -> bool:
        """Validation method stub

        :param value: value for validation
        :return: True if validated, False otherwise
        """
        return not self.required or value is not None


class BoolField(_Field):
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


class DateField(_Field):
    """Date type field"""

    def __init__(self, default_value: datetime = None, required: bool = False, fmt: Callable = lambda x: x.isoformat()):
        """Creates a date field of python datetime type

        :param default_value: default value
        :param required: required flag
        """
        super().__init__(default_value, required)
        self.fmt = fmt

    def validate(self, value: datetime) -> bool:
        """Validation method

        :param value: value for validation
        :return: True if validated, False otherwise
        """
        return super().validate(value) and (value is None or isinstance(value, datetime))


class FloatField(_Field):
    """Float type field"""

    def __init__(
        self,
        default_value: float = 0.0,
        minimum_value: float = None,
        maximum_value: float = None,
        required: bool = False,
    ):
        """Creates a float field

        :param default_value: default value
        :param minimum_value: minimum value
        :param maximum_value: maximum value
        :param required: required flag
        """
        super().__init__(default_value, required)
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value

    def validate(self, value: float) -> bool:
        """Validation method

        :param value: value for validation
        :return: True if validated, False otherwise
        """
        return super().validate(value) and (value is None or (isinstance(value, float) and self._validate_range(value)))

    def _validate_range(self, value: float) -> bool:
        """Range validation method

        :param value: value for validation
        :return: True if validated, False otherwise
        """
        return (self.minimum_value is None or value >= self.minimum_value) and (
            self.maximum_value is None or value <= self.maximum_value
        )


class IntField(_Field):
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


class StringField(_Field):
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


def is_valid_field(typ):
    return isinstance(typ, _Field)


__all__ = ["IntField", "FloatField", "BoolField", "StringField", "DateField", "is_valid_field"]
