#!/usr/bin/env python

import sys

align =open( sys.argv[1] )

count = 0

for line in align:
    # NM is 18
    if "NH:i:1" in line:
        count = count + 1
    else:
        continue
        
print count
  
