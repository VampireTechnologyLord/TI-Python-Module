from sys import version
from setuptools import setup, find_packages
import codecs
import os


VERSION = "0.8.2"

setup(
    name="ti-python-module",
    version=VERSION,
    author="VampireTechnologyLord",
    author_email="<elias.freund@ewe.net>",
    description="TI-Python Debugging",
    long_description_content_type="text/markdown",
    packages=find_packages(),
#    install_requires=[],
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