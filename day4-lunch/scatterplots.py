#!/usr/bin/env python

"""

"""
import sys
import numpy
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv( sys.argv[1], sep="\t")
df2 = pd.read_csv( sys.argv[2], sep="\t")


x = numpy.log1p(df1["FPKM"])
y = numpy.log1p(df2["FPKM"])
m = numpy.polyfit(x, y, 1)





plt.figure()
plt.scatter( df1["FPKM"], df2["FPKM"], alpha=0.2, color='blue')#, edgecolors="none")

plt.plot(numpy.unique(x), numpy.poly1d(numpy.polyfit(x, y, deg = 1)) (numpy.unique(x)))

plt.xscale()
plt.yscale()
plt.suptitle('Scatterplot', fontsize=28)
plt.xlabel('SRR072893', fontsize=20)
plt.ylabel('SRR072915', fontsize=20)
plt.savefig( sys.argv[3] + ".png")
plt.close()