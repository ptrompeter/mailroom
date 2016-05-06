# _*_ coding: utf-8 _*_
from setuptools import setup

setup(
    name="mailroom",
    desc="mailroom homework for python 401 week 1",
    version=0.1,
    author="Patrick Trompeter and Mike Harrison",
    email="patrick@trompeter.io",
    py_modules=['mailroom'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']}
)
