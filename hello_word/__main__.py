#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

py2_command = """
print 'hello world!'
"""

py3_command = """
print('hello world!')
"""

def main():
    if sys.version_info[0] < 3:
        c = py2_command
    else:
        c = py3_command
    exec(c)

if __name__ == 'main':
    main()
