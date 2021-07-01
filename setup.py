from sys import version
from setuptools import setup, find_packages
import codecs
import os


###

VERSION = "0.9.4"


SUMMARY = "Texas Instruments python debugging"

###
with open("README.md", "r") as fh:
    long_decription = fh.read()



setup(
    name="ti-python-module",
    version=VERSION,
    author="VampireTechnologyLord",
    author_email="<elias.freund@ewe.net>",
    description=SUMMARY,
    long_descripion=long_decription,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['multimethod'],
    keywords=["python", "ti", "texas instruments"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Utilities"
    ]
)
