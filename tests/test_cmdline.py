#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import json
from eyeball.__main__ import main

CODE = '''
def function_test():
    """zażółć_gęślą_jaźń"""
    pass

'''

def test_simple_sdtio(monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, 'read', lambda: CODE)
    monkeypatch.setattr(sys, 'argv', ["__main__", "--line", "2"])
    main()
    out, err = capsys.readouterr()
    assert not err
    blocks = json.loads(out)
    assert len(blocks) == 1
    assert blocks[0]['name'] == 'function_test'
