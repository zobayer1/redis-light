# -*- coding: utf-8 -*-
import json

import pytest

from redisorm.bases import HashBase
from redisorm.fields import IntField, StringField


@pytest.fixture(scope="module")
def user_orm():
    """Pytest fixture for user orm class"""

    class UserOrm(HashBase):
        user_id = IntField(default_value=0, minimum_value=-128, maximum_value=127)
        user_name = StringField()

    return UserOrm


@pytest.fixture(scope="module")
def user(user_orm):
    """Pytest fixture for user orm object"""
    return user_orm()


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


def test_orm_object_populated_with_dict(user_orm):
    """Test fails if orm object could not be populated from a dictionary object"""
    user_dict = {"user_id": 0, "user_name": "test"}
    user = user_orm(user_dict)
    assert user_dict == json.loads(repr(user))


def test_orm_object_fails_from_non_dict_object(user_orm):
    """Test fails if orm object instantiated from a non dictionary object"""
    with pytest.raises(RuntimeError):
        user_orm("string")


def test_orm_object_fails_from_dict_with_invalid_fields(user_orm):
    """Test fails if orm object populated from a dictionary containing invalid field"""
    user_dict = {"user_id": 0, "age": 30}
    with pytest.raises(AttributeError):
        user_orm(user_dict)
