#!/usr/bin/env python
from setuptools import setup, find_packages

__version__ = 1.0


setup(
    name="courier",
    author="Greg Rehm",
    version=__version__,
    packages=find_packages(exclude=["scripts"]),
    install_requires=[
        "google-api-python-client"
    ],
    entry_points={
        "console_scripts": [
            "courier=courier.main:main"
        ]
    }
)
