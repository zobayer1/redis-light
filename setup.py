# -*- coding: utf-8 -*-
from os import path
from setuptools import find_packages, setup

setup_dependencies = [
    "wheel",
    "setuptools-scm",
]

install_dependencies = [
    "importlib-metadata;python_version<'3.8'",
    "redis",
]

try:
    docs_file = path.join(path.abspath(path.dirname(__file__)), "README.md")
    with open(docs_file, encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = __doc__

setup(
    name="redis-light",
    url="https://github.com/zobayer1/redis-light",
    license="MIT",
    author="Zobayer Hasan",
    author_email="zobayer1@gmail.com",
    description="Lightweight Redis ORM",
    keywords="python redis orm",
    long_description=long_description,
    use_scm_version=True,
    setup_requires=setup_dependencies,
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=False,
    zip_safe=True,
    platforms="any",
    install_requires=install_dependencies,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
