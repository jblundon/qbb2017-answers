#!/usr/bin/env python

import sys

align=open( sys.argv[1] )


total = 0.0
count = 0.0

for line in align:
    if line.startswith( "@" ):
        continue
    id = line.split('\t')
    total = total + float(id[4])
    count += 1
        
print total / count

