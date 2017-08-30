#!/usr/bin/env python

import sys

yes = 0.0
no = 0.0

for line in sys.stdin:
    line = line.rstrip()
    mylen = int(line)
    yes += mylen
    no += 1
    
print "There are %d genes, with a total span of %d, average gene len is %f" % (no, yes, float(yes)/no)