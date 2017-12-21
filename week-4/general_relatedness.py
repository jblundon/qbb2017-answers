#!/usr/bin/env python

"""
./general_relatedness.py "vcf_plink_output" "output.png"
"""

import sys
import matplotlib.pyplot as plt

x, y = [], []
for line in open( sys.argv[1] ):
    hi_peter = line.rstrip("\n").split(' ')
    x.append( float( hi_peter[2] ))
    y.append( float( hi_peter[3] ))
    
plt.figure()
plt.scatter( x,y )
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCAs')
plt.savefig( sys.argv [2] )
plt.close()    