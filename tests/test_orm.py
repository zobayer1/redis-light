# -*- coding: utf-8 -*-
import json

import pytest

from redisorm import ORMBase
from redisorm.fields import IntField, StringField


@pytest.fixture(scope="module")
def user():
    """Pytest fixture for user orm object"""
    _dict = {"user_id": 0, "user_name": "test"}

    class UserOrm(ORMBase):
        user_id = IntField(default_value=0, minimum_value=-128, maximum_value=127)
        user_name = StringField()

    return UserOrm(_dict)


def test_object_creation_succeeds(user):
    """Test fails if object cannot be created from orm class"""
    assert user.user_id == 0


def test_orm_fails_with_attribute_error_for_validation_error(user):
    """Test fails if attribute error was not raised when validation fails"""
    with pytest.raises(AttributeError):
        user.user_id = 130


def test_orm_fails_with_attribute_error_for_unknown_field(user):
    """Test fails if attribute error was not raised when unknown field was accessed"""
    with pytest.raises(AttributeError):
        user.age = 100


def test_orm_object_populated_with_dict(user):
    """Test fails if orm object could not be populated from a dictionary object"""
    _dict = json.loads(repr(user))
    assert _dict == {"user_id": 0, "user_name": "test"}
