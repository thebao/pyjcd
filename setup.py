#!/usr/bin/env python

from setuptools import setup
from pyjcd import configuration

setup(
    name='PyJCD',
    version=configuration.PYJCD_VERSION,
    description='A Python wrapper around the JCDecaux web API',
    author='Theo Hennessy (@thebao)',
    author_email='theo.hennessy@gmail.com',
    url='http://github.com/thebao/PyJCD',
    packages=['pyjcd',],
      long_description="""\
      PyJCD is a client Python wrapper library for the JCDecaux Cyclocity API.
      It allows quick and easy consumption of JCDecaux contract and station data
      from Python applications via a simple object model or JSON response.
      """,
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries",
    ],
    package_data = {
        '': ['*.txt', '*.xsd']
    },
    keywords='jcdecaux web api client wrapper data cyclocity vélib vélov',
    license='MIT',
    test_suite='tests'
)
