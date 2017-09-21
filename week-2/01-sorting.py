#!/usr/bin/env python 

import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

contig_file = open(sys.argv[1])

nseq = []
for ident, sequences in fasta.FASTAReader( contig_file ):
    nseq.append(sequences)
    
print "Statistics for Velvet"

nlength = []
for i in range(len(nseq)):
    nlength.append(len(nseq[i]))

nlength.sort()

print "Max = " + str(max(nlength))
print "Min = " + str(min(nlength))

clength = 0
for i in nlength:
    clength += i

print contig_length/2
count = 0
pos = 0
for i in nlength:
    if count < clength/2:
        count += i
        pos += 1
    else:
        print "N50 = " + str(nlength[pos - 1]) 
        break
        
print "Mean = " + str(np.mean(nlength))