#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

CODE = """ #1
class Test(object):
    def __init__(self): #3
        pass

    @property #6
    def simple_property():
        pass  #8

"""

from eyeball import code_blocks

def test_class():
    blocks = code_blocks(CODE, line=2)
    assert len(blocks) == 1
    assert blocks[0].name == "Test"


def test_method():
    blocks = code_blocks(CODE, line=3)
    assert len(blocks) == 2
    assert blocks[0].name == "__init__"


def test_property():
    blocks = code_blocks(CODE, line=6)
    assert blocks[0].name == "simple_property"
    assert blocks[0].covers(7)
