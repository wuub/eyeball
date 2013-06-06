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
    version='0.0.1',
    description='Simple Python source inspection with AST',
    author='Wojciech Bederski',
    license='MIT',
    author_email='github@wuub.net',
    packages=find_packages(),
    tests_require=['tox'],
    zip_safe=False,
    cmdclass={'test': Tox}
)
