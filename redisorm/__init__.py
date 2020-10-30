# -*- coding: utf-8 -*-
import sys

if sys.version_info < (3, 8):  # pragma: no cover
    from importlib_metadata import version as get_version
else:  # pragma: no cover
    from importlib.metadata import version as get_version

appname = "redis-light"
version = get_version(appname)
