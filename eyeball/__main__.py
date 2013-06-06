#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import json
import argparse

from eyeball import code_blocks
from eyeball import CodeBlock


CODE_BLOCK_ATTRS = ['name', 'full_path', 'start', 'end', 'full_path']

def json_default(obj):
    if isinstance(obj, CodeBlock):
        return {attr:getattr(obj, attr) for attr in CODE_BLOCK_ATTRS}
    raise TypeError()


def main():
    parser = argparse.ArgumentParser(description='eyeball')
    parser.add_argument('--line', '-l', type=int)

    args = parser.parse_args()

    code = sys.stdin.read()
    blocks = code_blocks(code, line=args.line)
    json.dump(blocks, sys.stdout, indent=2, default=json_default)
    sys.stdout.write('\n')

if __name__ == '__main__':
    main()