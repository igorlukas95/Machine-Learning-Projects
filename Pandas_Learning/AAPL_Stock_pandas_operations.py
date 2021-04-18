# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:04:30 2021

@author: Nigor
"""

import numpy as np
import pandas as pd

# %% importing dataset

df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)
df.columns = ['Open',' High', 'Low','Close','Volume']
# %% select only first n rows
df.iloc[:5]
df.iloc[10:20]
df.iloc[10:]
# %% select only first n column

df.iloc[: , :2]
df.iloc[5:10,3:]
df.iloc[[1,4],[0,4]]
df.iloc[::5]
df.iloc[:,::2]

# %% 
df['Daily_Change'] = df['Close']/ df['Close'].shift(1) - 1

# %%
df = df.assign(avg= (df['Open'] + df['Close']) / 2.)

# %% 
max_daily_change = df['Daily_Change'].aggregate(max)
min_daily_change = df['Daily_Change'].aggregate(min)

avg_daily_change = df['Daily_Change'].aggregate(np.mean)

# %%
df['Daily_Change'].hist(bins=100)
# %%
df['Flag'] = df['Daily_Change'] > 0
df['Flag'].aggregate(sum)

# %% 
days_with_positive_return = df