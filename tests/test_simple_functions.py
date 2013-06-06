#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

from eyeball import code_blocks


CODE = """

def function_one():
    pass

def function_two():
    pass
"""


def test_function1():
    blocks = code_blocks(CODE, line=4)
    assert blocks[0].name == "function_one"


def test_function2():
    blocks = code_blocks(CODE, line=6)
    assert blocks[0].name == "function_two"
