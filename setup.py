#!/usr/bin/env python

from setuptools import setup

version = '1.0.0'

required = open('requirements.txt').read().split('\n')

setup(
    name='fakearray',
    version=version,
    description='simulated n-dimensional array data',
    author='jasminetstone',
    author_email='jasminetstone@gmail.com',
    url='https://github.com/jasminetstone/fakearray',
    packages=['fakearray'],
    install_requires=required,
    long_description='See ' + 'https://github.com/jasminetstone/fakearray',
    license='MIT'
)