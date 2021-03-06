#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = ['numpy', 'xarray', 'netcdf4']
tests_require = ['pytest', 'nose', 'coveralls', 'flake8', 'mypy']

setup(name='pyrinex',
      packages=find_packages(),
      description='Python RINEX 2/3 NAV/OBS reader that is very fast',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      author='Michael Hirsch, Ph.D.',
      version='1.4.1',
      url='https://github.com/scivision/pyrinex',
      install_requires=install_requires,
      tests_require=tests_require,
      python_requires='>=3.6',
      extras_require={'plot': ['matplotlib', 'seaborn', 'pymap3d'],
                      'tests': tests_require, },
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Atmospheric Science',
      ],
      scripts=['ReadRinex.py', 'PlotExample.py'],
      include_package_data=True,
      )
