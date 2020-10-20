# -*- coding: utf-8 -*-


class Field(object):
    """Base class for all field types"""

    def __init__(self, default_value=None, required: bool = False):
        """Creates a Field object with a default value

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
