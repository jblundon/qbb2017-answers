#!/usr/bin/env python

import sys
#open the three files you need
#one being the dictionary
#two being the ctab file 
#three being the gene you are looking for

one = open( sys.argv[1] )
two = open( sys.argv[2] )
three = ( sys.argv[3] )

count = 0

gene_matching = {}

for line in one:
    cut = line.rstrip("\r\n").split()
    fly_gene = cut[0]
    ac_name = cut[1]
    gene_matching[fly_gene] = ac_name
    
for line in two:
    fields = line.rstrip("\r\n").split("\t")
    tank = fields [8]
    if count > 100:
        break
    if tank in gene_matching:
        count+=1
        name = gene_matching[tank]
        fields[8] = name
        #print fields[8]
        print "\t".join(fields)
    else: 
        continue
