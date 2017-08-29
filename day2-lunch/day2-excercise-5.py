#!/usr/bin/env python

import sys

align=open( sys.argv[1] )

time=align.readlines()

result=[]

for line in time:
    if "AS:" not in line:
        continue
    else:    
        result.append(line.split("\t")[4])
        
align.close()  

sum(result)/float(len(result))

