# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:01:18 2021

@author: Nigor
"""

import numpy as np
import pandas as pd

# %% importing dataset

df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)
df.columns = ['Open',' High', 'Low','Close','Volume']
#%%  Tworzenie maski
df_bool = df > 150
df_ = df[df_bool]


# %%
df_ = df[df > 150]

# %%
df_2019 = df['2019-01-01':]

# %%
df_jan_2019 = df['2019-01-01':'2019-01-31']

# %%
df_jan_2019.query('Close > 160')
