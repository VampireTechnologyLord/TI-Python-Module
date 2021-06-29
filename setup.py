from sys import version
from setuptools import setup, find_packages
import codecs
import os


###

VERSION = "0.9.1"

###



current_directory = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_desc = f.read()
except Exception:
    long_desc = "A module for debugging with the TexasInstruments CX II Cas, Rover and Innovator Hub."



setup(
    name="ti-python-module",
    version=VERSION,
    author="VampireTechnologyLord",
    author_email="<elias.freund@ewe.net>",
    description="TI-Python Debugging",
    long_description_content_type="text/markdown",
    long_descripion=long_desc,
    packages=find_packages(),
    install_requires=['multimethod'],
    keywords=["python", "ti", "texas instruments"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operation System :: Unix",
        "Operation System :: MacOS, MacOS X",
        "Operation System :: Microsoft :: Windows",
        "Topic :: Utilities"
    ]
)