#!/usr/bin/env python

import sys
import pandas as pd

df = pd.read_csv( sys.argv[1], sep="\t")

roi_fwd = df["strand"] == "+"
roi_rev = df["strand"] == "-"
coi1 = ["chr", "start", "end", "t_name"]

df_fwd = df[roi_fwd][coi1]
df_fwd["newstart"] = df_fwd["start"] - 500
df_fwd["newstart"][df_fwd["newstart"]<0] = 1
df_fwd["newend"] = df_fwd["start"] + 500

coi2 =["chr", "newstart" , "newend", "t_name"]

df_rev = df[roi_rev][coi1]
df_rev["newstart"] = df_rev["start"] - 500
df_rev["newstart"][df_rev["newstart"]<0] = 1
df_rev["newend"] = df_rev["start"] + 500



coi3 =["chr", "newstart" , "newend", "t_name"]
df1 = df_fwd[coi2]
df2 = df_rev[coi3]



bothdf = [df1, df2]
final = pd.concat(bothdf)
final.to_csv("final.bed", sep="\t", header=None, index=False)

    
    
