# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Callable, Any


class _FieldBase(object):
    """Base class for all field types"""

    def __init__(self, default_value: Any = None, required: bool = False):
        """Creates a `_FieldBase` object with a default value

        :param default_value: initial value for this field, default `None`
        :param required: required flag, default `False`
        """
        self.default_value = default_value
        self.required = required

    def validate(self, value: Any) -> bool:
        """Validation method stub

        :param value: value for validation
        :returns: `True` if validated, `False` otherwise
        """
        return not self.required or value is not None


class BoolField(_FieldBase):
    """Boolean type field"""

    def __init__(self, default_value: bool = False, required: bool = False):
        """Creates a boolean field

        :param default_value: initial value, default `False`
        :param required: required flag, default `False`
        """
        super().__init__(default_value, required)

    def validate(self, value: bool) -> bool:
        """Validation method

        :param value: value for validation
        :returns: `True` if validated, `False` otherwise
        """
        return super().validate(value) and (value is None or isinstance(value, bool))


class DateField(_FieldBase):
    """Date type field"""

    def __init__(
        self, default_value: datetime = None, required: bool = False, formatter: Callable = lambda x: x.isoformat()
    ):
        """Creates a date field of python datetime type

        :param default_value: initial value, default `None`
        :param required: required flag, default `False`
        :param formatter: function to convert `datetime` object to `string`, default `datetime.isoformat`
        """
        super().__init__(default_value, required)
        self.formatter = formatter

    def validate(self, value: datetime) -> bool:
        """Validation method

        :param value: value for validation
        :returns: `True` if validated, `False` otherwise
        """
        return super().validate(value) and (value is None or isinstance(value, datetime))


class FloatField(_FieldBase):
    """Float type field"""

    def __init__(
        self,
        default_value: float = 0.0,
        minimum_value: float = None,
        maximum_value: float = None,
        required: bool = False,
    ):
        """Creates a float field

        :param default_value: initial value, default `0.0`
        :param minimum_value: minimum value, default `None`
        :param maximum_value: maximum value, default `None`
        :param required: required flag, default `False`
        """
        super().__init__(default_value, required)
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value

    def validate(self, value: float) -> bool:
        """Validation method

        :param value: value for validation
        :returns: `True` if validated, `False` otherwise
        """
        return super().validate(value) and (value is None or (isinstance(value, float) and self._validate_range(value)))

    def _validate_range(self, value: float) -> bool:
        """Range validation method

        :param value: value for validation
        :returns: `True` if validated, `False` otherwise
        """
        return (self.minimum_value is None or value >= self.minimum_value) and (
            self.maximum_value is None or value <= self.maximum_value
        )


class IntField(_FieldBase):
    """Integer type field"""

    def __init__(
        self, default_value: int = 0, minimum_value: int = None, maximum_value: int = None, required: bool = False
    ):
        """Creates an integer field

        :param default_value: initial value, default `0`
        :param minimum_value: minimum value, default `None`
        :param maximum_value: maximum value, default `None`
        :param required: required flag, default `False`
        """
        super().__init__(default_value, required)
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value

    def validate(self, value: int) -> bool:
        """Validation method

        :param value: value for validation
        :returns: `True` if validated, `False` otherwise
        """
        return super().validate(value) and (value is None or (isinstance(value, int) and self._validate_range(value)))

    def _validate_range(self, value: int) -> bool:
        """Range validation method

        :param value: value for validation
        :returns: `True` if validated, `False` otherwise
        """
        return (self.minimum_value is None or value >= self.minimum_value) and (
            self.maximum_value is None or value <= self.maximum_value
        )


class StringField(_FieldBase):
    """String type field"""

    def __init__(
        self, default_value: str = None, minimum_length: int = None, maximum_length: int = None, required: bool = False
    ):
        """Creates a string field

        :param default_value: initial value, default `None`
        :param minimum_length: minimum string length, default `None`
        :param maximum_length: maximum string length, default `None`
        :param required: required flag, default `False`
        """
        super().__init__(default_value, required)
        self.minimum_length = minimum_length
        self.maximum_length = maximum_length

    def validate(self, value: str) -> bool:
        """Validation method

        :param value: value for validation
        :returns: `True` if validated, `False` otherwise
        """
        return super().validate(value) and (value is None or (isinstance(value, str) and self._validate_length(value)))

    def _validate_length(self, value: str) -> bool:
        """Length validation method

        :param value: value for validation
        :returns: `True` if validated, `False` otherwise
        """
        return (self.minimum_length is None or len(value) >= self.minimum_length) and (
            self.maximum_length is None or len(value) <= self.maximum_length
        )


def isormfield(obj: _FieldBase) -> bool:
    """Tests if an object is an instance of `_FieldBase`

    :param obj: object for instance validation
    :returns: `True` if an instance of `_FieldBase`, `False` otherwise
    """
    return isinstance(obj, _FieldBase)


__all__ = ["IntField", "FloatField", "BoolField", "StringField", "DateField", "isormfield"]
