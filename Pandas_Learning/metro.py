# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:48:03 2021

@author: Nigor
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = ('http://archive.ics.uci.edu/ml/machine-learning-databases/00492/'
       'Metro_Interstate_Traffic_Volume.csv.gz')

# %% Loading dataset

metro = pd.read_csv(url,compression='gzip', index_col='date_time', parse_dates=True) 
metro = metro.loc['2016-01-01':]
# %% plotting traffic

traffic = metro.iloc[:,-1:]
traffic.plot()
tr = traffic.resample('M').sum()
tr.plot()
# %% pivot tables

pd.pivot_table(data=metro, values = 'traffic_volume',index='weather_main').plot(kind='bar')
