#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import statsmodels.api as sm

df = pd.read_csv(sys.argv[1], sep="\t")
df = df.sort_values("t_name")
fpkm = df["FPKM"]

for arg in sys.argv[2:]:
    df_ad = pd.read_csv(arg, sep='\t', header=None, names = ["name", "size", "covered", "sum", "mean0", "mean"])
    df_ad = df_ad.sort_values("name")
    ad  = df_ad["mean"]
    model = sm.OLS(ad,fpkm)
    results = model.fit()
    print results.summary()

