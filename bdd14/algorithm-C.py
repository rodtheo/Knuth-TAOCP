import sys
import os
import collections as c


d = c.defaultdict()
with open(sys.argv[1], 'r') as opened:
    for instruction in opened.readlines():
        print instruction.split()
