#!/usr/bin/env python

"""
Usage ./01-timecourse <samples.csv> <ctab_dir>

- Plot timecourse of FBtr0331261 for females
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt

transcript = "FBtr0331261"

df_samples = pd.read_csv( sys.argv[1] )
soi = df_samples["sex"] == "female"

fpkms = []
for sample in df_samples["sample"][soi]:
    # Build a complete path
    fname = os.path.join( sys.argv[2], sample, "t_data.ctab" )
    # Read current sample
    df = pd.read_csv( fname, sep="\t" )
    # Subset just Sxl rows
    roi = df["t_name"] == transcript
    # Save FPKM values to list
    fpkms.append( df[roi]["FPKM"].values )
    

plt.figure()
plt.plot( fpkms , color = 'red')
plt.savefig( "timecourse.png")
plt.close()