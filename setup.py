#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


setup(
    name='eyeball',
    version='0.0.3',
    description='Python source inspection with AST',
    long_description=open('README.rst').read(),
    author='Wojciech Bederski',
    url="https://github.com/wuub/eyeball",
    license='MIT',
    author_email='github@wuub.net',
    packages=find_packages(),
    tests_require=['tox'],
    zip_safe=False,
    cmdclass={'test': Tox},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)
