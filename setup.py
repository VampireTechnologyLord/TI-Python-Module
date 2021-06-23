from sys import version
from setuptools import setup, find_packages
import codecs
import os

LONG_DESCRIPTION = "# TI-Python-Module\n\n## How to install this feature / module\nHow to use these modules properly:\n### Accessing the module\n\n1. Install the package using `pip install ti-python-module`\n2. Copy the other files into your workspace\n3. Create an additional python file\n4. Import the modules (examples: `from ti_python_module.ti_hub import *` or `from ti_python_module import ti_rover as rv`)\n\n### Putting the program on the calculator / rover\n\n1. Check, if you have used any of the returned values from the methods. Since these are NOT implemented on the TI-CAS itself, these won't work. Just comment them out, so you will be able to use them again, when editing the program later again\n2. Change the import so you don't habe the `ti_python_module` part\n3. Save the python file\n4. Copy ONLY your python file to the calculator\n\n## Known Problems / Issues\n\n- The functions `digital` and `bb_port` are registered each two times in the calculator. If you enter these via the calculators menu, the software is able to differentiate between both of them. If you enter these commands via the keyboard, the system won't know, whether you are choosing the one from category \"Add Output Device\" or the one from \"Add Input Device\". Due to pythons programming, I am unable to add these functions two times with different arguments, processing ... with the same name. Therefore, only the ones from \"Add Input Device\" are currently registered.\n\n- The module `cmath` dont exists. This is due to a module with the exact same name already exists build in to python. Since I am unable to change build-in classes, I can't add the proper functions. The same issue occurs for `time`. \n\n\n\n\nIf you know a way to solve one of these issues above, just open an issue tracker! Because clearly, I am not a computer, so i don't know everything ;-).\n"

VERSION = "0.8.9"

setup(
    name="ti-python-module",
    version=VERSION,
    author="VampireTechnologyLord",
    author_email="<elias.freund@ewe.net>",
    description="TI-Python Debugging",
    long_description_content_type="text/markdown",
    long_descripion=LONG_DESCRIPTION,
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