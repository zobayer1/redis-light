# -*- coding: utf-8 -*-
import redisorm


def test_redisorm_version_is_readable():
    """Test fails if version string is empty"""
    assert redisorm.version


def test_redisorm_appname_is_readable():
    """Test fails if appname string is empty"""
    assert redisorm.appname == "redis-light"
