# PyExifTool <http://github.com/smarnach/pyexiftool>
# Copyright 2012 Sven Marnach

# This file is part of PyExifTool.
#
# PyExifTool is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the licence, or
# (at your option) any later version, or the BSD licence.
#
# PyExifTool is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See COPYING.GPL or COPYING.BSD for more details.

from setuptools import setup
import os

MAJOR_VERSION = 1
MINOR_VERSION = 0
BUILD_NUMBER = os.environ.get('CIRCLE_BUILD_NUM', 'DEVSNAPSHOT')

setup(name="exiftool",
      version="{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, BUILD_NUMBER),
      description="Python wrapper for exiftool (Kairos-packaged)",
      license="GPLv3+",
      author="Sven Marnach",
      author_email="sven@marnach.net",
      url="https://github.com/KairosAerospace/pyexiftool",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Topic :: Multimedia"],
      py_modules=["exiftool"],
      setup_requires=["nose>=1.3.7"])

