# -*- coding: utf-8 -*-
from datetime import datetime

from redisorm.fields import IntField, BoolField, FloatField, StringField, DateField
from redisorm.fields.field import Field


def test_required_field_cannot_validate_none():
    """Test fails if a required field can validate None"""
    field = Field(required=True)
    assert not field.validate(None)


def test_non_required_field_can_validate_none():
    """Test fails if a non-required field cannot validate None"""
    field = Field()
    assert field.validate(None)


def test_int_field_default_value():
    """Test fails if IntField instance doesn't have default value"""
    int_field = IntField()
    assert int_field.default_value == 0


def test_int_field_default_value_overwritten():
    """Test fails if IntField instance default value cannot be overwritten"""
    int_field = IntField(100)
    assert int_field.default_value == 100


def test_int_field_validation():
    """Test fails if IntField validation isn't successful"""
    int_field = IntField(minimum_value=-100, maximum_value=100)
    assert int_field.validate(50)
    assert not int_field.validate(-200)
    assert not int_field.validate(200)


def test_bool_field_default_value():
    """Test fails if BoolField instance doesn't have default value"""
    bool_field = BoolField()
    assert not bool_field.default_value


def test_bool_field_default_value_overwritten():
    """Test fails if BoolField instance default value cannot be overwritten"""
    bool_field = BoolField(True)
    assert bool_field.default_value


def test_bool_field_validation():
    """Test fails if BoolField validation isn't successful"""
    bool_field = BoolField()
    assert bool_field.validate(True)


def test_float_field_default_value():
    """Test fails if FloatField instance doesn't have default value"""
    float_field = FloatField()
    assert float_field.default_value == 0


def test_float_field_default_value_overwritten():
    """Test fails if FloatField instance default value cannot be overwritten"""
    float_field = FloatField(100.0)
    assert float_field.default_value == 100.0


def test_float_field_validation():
    """Test fails if FloatField validation isn't successful"""
    float_field = FloatField(minimum_value=-100.0, maximum_value=100.0)
    assert float_field.validate(50.0)
    assert not float_field.validate(-200.0)
    assert not float_field.validate(200.0)


def test_string_field_default_value():
    """Test fails if StringField instance doesn't have default value"""
    str_field = StringField()
    assert str_field.default_value is None


def test_string_field_default_value_overwritten():
    """Test fails if StringField instance default value cannot be overwritten"""
    str_field = StringField("Hello World")
    assert str_field.default_value == "Hello World"


def test_string_field_validation():
    """Test fails if StringField validation isn't successful"""
    str_field = StringField(minimum_length=5, maximum_length=20)
    assert str_field.validate("Hello World")
    assert not str_field.validate("A")
    assert not str_field.validate("A" * 200)


def test_date_field_default_value():
    """Test fails if DateField instance doesn't have default value"""
    date_field = DateField()
    assert date_field.default_value is None


def test_date_field_default_value_overwritten():
    """Test fails if DateField instance default value cannot be overwritten"""
    dt = datetime.now()
    date_field = DateField(dt)
    assert date_field.default_value == dt


def test_date_field_validation():
    """Test fails if DateField validation isn't successful"""
    date_field = DateField()
    assert date_field.validate(datetime.now())
