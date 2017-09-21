#!/usr/bin/env python

import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

d = open(sys.argv[1])

count = 1
plt.figure()
for i in d:
    if "zstart1" in i:
        continue
    else:
        fields = i.split("\t")
        plt.plot([count,count+float(fields[3])],[float(fields[0]),float(fields[1])])
        count += float(fields[3])

plt.xlabel("Contig Names")
plt.ylabel("Position")
plt.ylim((0,100000))
plt.xlim((0,100000))
plt.savefig( "velvet_high" + ".png")
plt.close()