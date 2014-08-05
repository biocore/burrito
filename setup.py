#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2014--, burrito development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

__version__ = "0.9.0"

from setuptools import find_packages, setup

classes = """
    Development Status :: 5 - Production/Stable
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Topic :: Software Development :: Libraries
    Topic :: Software Development :: Libraries :: Python Modules
    Topic :: Utilities
    Programming Language :: Python
    Programming Language :: Python :: 2
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.3
    Programming Language :: Python :: 3.4
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

description = ('Framework for wrapping and controlling command-line '
               'applications.')

with open('README.rst') as f:
    long_description = f.read()

setup(name='burrito',
      version=__version__,
      license='BSD',
      description=description,
      long_description=long_description,
      author="burrito development team",
      author_email="gregcaporaso@gmail.com",
      maintainer="burrito development team",
      maintainer_email="gregcaporaso@gmail.com",
      url='https://github.com/biocore/burrito',
      test_suite='nose.collector',
      packages=find_packages(),
      install_requires=['future'],
      extras_require={'test': ["nose >= 0.10.1", "pep8", "flake8",
                               "coveralls"]},
      classifiers=classifiers)
