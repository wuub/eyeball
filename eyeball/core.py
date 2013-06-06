#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import ast


class CodeMap(object):
    def __init__(self):
        self._blocks = set()

    def add(self, block):
        self._blocks.add(block)

    def for_line(self, lineno):
        for b in self._blocks:
            if b.covers(lineno):
                yield b

class CodeBlock(object):
    def __init__(self, name, node, parent):
        self.name = name
        self.node = node
        self.parent = parent

        self._start = None
        self._end = None
        self._full_path = None

    def update_line(self, lineno):
        self._start = min(lineno, self._start) if self._start is not None else lineno
        self._end = max(lineno, self._end) if self._end is not None else lineno

    def covers(self, lineno):
        return self._start <= lineno <= self._end

    @property
    def is_class_def(self):
        return isinstance(self.node, ast.ClassDef)

    @property
    def full_path(self):
        if not self._full_path:
            cur = self
            path = []
            while cur is not None:
                path.append(cur.name)
                cur = cur.parent
            self._full_path = '.'.join(reversed(path))
        return self._full_path

    @property
    def span(self):
        """Returns number of lines"""
        return self._end - self._start + 1

    def code(self, full_text):
        """Return code of this block with extra whitespace removed"""
        block_lines = full_text.splitlines()[self._start - 1:self._end]
        first_line = block_lines[0]
        white_count = len(first_line) - len(first_line.lstrip())
        return "\n".join(line[white_count:] for line in block_lines)

    def __cmp__(self, other):
        return cmp(self.span, other.span)

    def __repr__(self):
        return "{}({}:{})".format(self.full_path, self._start, self._end)


class ClassVisitor(ast.NodeVisitor):
    def __init__(self, code_map):
        self.path = []
        self.line_map = {}
        self.code_map = code_map
        self.current_block = []

    def visit_ClassDef(self, node):
        block = CodeBlock(node.name, node, self.path[-1] if self.path else None)
        self.code_map.add(block)
        self.path.append(block)
        self.generic_visit(node)
        self.path.pop()

    visit_FunctionDef = visit_ClassDef

    def generic_visit(self, node):
        if hasattr(node, 'lineno'):
            for elem in self.path:
                elem.update_line(node.lineno)
        return super(ClassVisitor, self).generic_visit(node)



def code_blocks(code, line=None):
    module = ast.parse(code)
    code_map = CodeMap()
    cv = ClassVisitor(code_map)
    cv.visit(module)
    return sorted(list(code_map.for_line(line)))
