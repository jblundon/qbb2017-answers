#!/usr/bin/env python

"""
Usage ./01-timecourse <samples.csv> <ctab_dir> <replicates.csv>

- Plot timecourse of FBtr0331261 for females
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt

transcript = "FBtr0331261"

df_samples1 = pd.read_csv( sys.argv[1] )
df_samples2 = pd.read_csv( sys.argv[1] )
df_samples3 = pd.read_csv( sys.argv[3] )
df_samples4 = pd.read_csv( sys.argv[3] )

soi1 = df_samples1["sex"] == "female"
soi2 = df_samples2["sex"] == "male"
soi3 = df_samples3["sex"] == "female"
soi4 = df_samples4["sex"] == "male"

fpkms1 = []
fpkms2 = []
fpkms3 = []
fpkms4 = []


for sample in df_samples1["sample"][soi1]:
    # Build a complete path
    fname = os.path.join( sys.argv[2], sample, "t_data.ctab" )
    # Read current sample
    df = pd.read_csv( fname, sep="\t" )
    # Subset just Sxl rows
    roi1 = df["t_name"] == transcript
    # Save FPKM values to list
    fpkms1.append( df[roi1]["FPKM"].values )
    
for sample in df_samples2["sample"][soi2]:
    fname = os.path.join( sys.argv[2], sample, "t_data.ctab" )
    df = pd.read_csv(fname, sep="\t")
    roi2 = df["t_name"] == transcript
    fpkms2.append( df[roi2]["FPKM"].values )
    
for sample in df_samples3["sample"][soi3]:
    fname = os.path.join( sys.argv[2], sample, "t_data.ctab" )
    df = pd.read_csv(fname, sep="\t")
    roi3 = df["t_name"] == transcript
    fpkms3.append( df[roi3]["FPKM"].values )
     
for sample in df_samples4["sample"][soi4]:
    fname = os.path.join( sys.argv[2], sample, "t_data.ctab" )
    df = pd.read_csv(fname, sep="\t")
    roi4 = df["t_name"] == transcript
    fpkms4.append( df[roi4]["FPKM"].values )   
    
plt.figure()
plt.plot( fpkms1, color = 'red', label = 'Female')
plt.plot( fpkms2, color = 'blue', label = 'Male' )
plt.plot( [4,5,6,7], fpkms3, "o", color = 'red', label = 'Female Replicate')
plt.plot( [4,5,6,7],fpkms4, "o", color = 'blue', label = 'Male Replicate' )
plt.xlabel("Developmental Stage", fontsize = 20)
plt.ylabel("mRNA Abundance (RPKM)", fontsize = 20)
plt.suptitle("$\it{Sxl}$", fontsize = 30)
plt.xticks([0,1,2,3,4,5,6,7],("10", "11", "12", "13", "14A", "14B", "14C", "14D"), rotation = "vertical")
plt.legend(loc = "best")
plt.savefig( "day4-homework.png", bbox_inches = "tight")
plt.close()