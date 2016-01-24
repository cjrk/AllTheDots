#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name="allthedots",
      version="0.1.3",
      author="Christian Jurke",
      description="Make a list of important stuff.",

      py_modules = ['allthedots'],
      entry_points={
          'console_scripts':
            ['atd = allthedots:main']
      },
      install_requires=['setuptools']
)
