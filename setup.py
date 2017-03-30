#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


# get version nr
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    'pirc522')))
sys.path.pop(0)

setup(
    name='pi-rc522',
    packages=find_packages(),
    include_package_data=True,
    version="2.0.0",
    description='Raspberry Pi Python library for SPI RFID RC522 module.',
    long_description='Raspberry Pi Python library for SPI RFID RC522 module.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    author='ondryaso',
    url='https://github.com/ondryaso/pi-rc522',
    license='MIT',
)
