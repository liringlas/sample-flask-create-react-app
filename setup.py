# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample Python app',
    long_description=readme,
    author='Konstantin Ryzhov',
    author_email='theaklair@gmail.com',
    url='https://github.com/catbug-developer/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

