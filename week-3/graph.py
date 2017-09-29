#!/usr/bin/env python

import sys
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

Hey_peter = open(sys.argv[1])

freqs = []

for i in Hey_peter:
    if i.startswith("#"):
        continue
    line = i.rstrip("\t\n").split()
    freq1 = line[7].split(";")
    freq2 = freq1[3][3:]
    if "," in freq2:
        freq3 = freq2.split(",")
        for i in freq3:
            freqs.append(float(i))
    else:
        freqs.append(float(freq2))
        
plt.figure()
plt.hist(freqs, bins=20)
plt.savefig(sys.argv[2] + ".png")
plt.close