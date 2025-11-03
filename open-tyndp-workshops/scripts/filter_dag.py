# -*- coding: utf-8 -*-
import sys
import re

content = sys.stdin.read()
match = re.search(r"(digraph.*)", content, re.DOTALL)
if match:
    print(match.group(1))
