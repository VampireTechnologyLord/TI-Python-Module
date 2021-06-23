from sys import version
from setuptools import setup, find_packages
import codecs
import os

def readme():
    with open('README.md') as f:
        return f.read()

VERSION = "0.8.9"

setup(
    name="ti-python-module",
    version=VERSION,
    author="VampireTechnologyLord",
    author_email="<elias.freund@ewe.net>",
    description="TI-Python Debugging",
    long_description_content_type="text/markdown",
    long_descripion=readme(),
    packages=find_packages(),
    install_requires=['multimethod'],
    keywords=["python", "ti", "texas instruments"],
    # classifiers=[
    #     "Developement Status :: 1 - Planning",
    #     "Intended Audience :: Developers",
    #     "Programming Language :: Python :: 3",
    #     "Operation System :: Unix",
    #     "Operation System :: MacOS, MacOS X",
    #     "Operation System :: Microsoft :: Windows",
    # ]
)