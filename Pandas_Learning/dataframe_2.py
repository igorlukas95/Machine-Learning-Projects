# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:51:29 2021

@author: Nigor
"""

import pandas as pd
import numpy as np

df = pd.read_csv('./data/aapl_us_d.csv', index_col = 0)
df.columns = ['Open','High','Low','Close','Volume']

# %%
open_price = df['Open']
open_price = df.iloc[:,0]
# %%
close_price = df.Close

# %%
volume = df.Volume
# %%
last_column = df.iloc[:,-1]

# %%
two = df[['Open','Close']]
three = df.iloc[:, [0,1,-1]]

# 55
from_open_to_close = df.iloc[:,:-1]