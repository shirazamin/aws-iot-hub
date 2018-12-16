# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='hub',
    version='0.1.0',
    description='AWS IoT Hub for Raspberry Pi',
    long_description=readme,
    author='Shiraz Amin',
    author_email='shiraz@shirazamin.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

