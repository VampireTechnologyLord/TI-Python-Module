import setuptools as st
import os
import io


###

VERSION = "0.10.12"


SUMMARY = "Texas Instruments python debugging"

###

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = SUMMARY



st.setup(
    name="ti-python-module",
    version=VERSION,
    author="VampireTechnologyLord",
    author_email="<elias.freund@ewe.net>",
    description=SUMMARY,
    long_descripion=long_description,
    long_description_content_type='text/markdown',
    packages=st.find_packages(),
    install_requires=[],
    setup_requires=[
    'setuptools>=41.0.1',
    'wheel>=0.33.4'],
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
