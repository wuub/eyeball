#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

from eyeball import code_blocks


CODE = """

def function_one():
    pass  #4

def function_two():
    pass  #6

def function_three():
    def function_four():
        def function_five():
            pass  #11
    pass

"""


def test_function1():
    blocks = code_blocks(CODE, line=4)
    assert blocks[0].name == "function_one"


def test_function2():
    blocks = code_blocks(CODE, line=6)
    assert blocks[0].name == "function_two"

def test_internal():
    blocks = code_blocks(CODE, line=11)
    assert ["function_five", "function_four", "function_three"] == [block.name for block in blocks]

