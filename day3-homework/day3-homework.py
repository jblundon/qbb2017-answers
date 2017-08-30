#!/usr/bin/env python

import sys
import fasta

database = open( sys.argv[1] )
target = open( sys.argv [2] )

k = int( sys.argv[3] )

count = 0

database_index = {}

for ident, sequence in fasta.FASTAReader(database):
    sequence = sequence.upper()
    for i in range( 0, len(sequence) - k ):
        kmer = sequence[i:i+k]
        if kmer not in database_index:
            database_index[kmer] = [(ident ,i)] 
        else:
            database_index[kmer] += [(ident,i)]
            

ident, sequence = fasta.FASTAReader(target).next()
sequence = sequence.upper()
for i in range( 0, len(sequence) - k ):
    kmer = sequence[i:i+k]
    if kmer in database_index:
        value = database_index[kmer]
        for something in value:
            count +=1 
            if count > 1000:
                break
            print something[0], "\t", something[1], "\t", i, "\t", kmer