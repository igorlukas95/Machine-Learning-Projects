# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:10:04 2021

@author: Nigor
"""

import pandas as pd
import numpy as np

#%%
np.random.seed(0)
index = pd.date_range('01-01-2019', periods = 10000)
df = pd.DataFrame(np.random.randn(10000), index = index)

# %%
df_cumsum = df.cumsum()

df_cumsum.plot(kind='line')

# %% Generating some data
df_1 = pd.DataFrame(np.random.randn(10,3), columns= list('ABC'))
df_2 = pd.DataFrame(np.random.randn(10,3), columns= list('ABC'))

# %%
df_1 + df_2 
df_1 - df_2

df_1 * df_2

df_1 / df_2

df_1 ** 2

np.exp(df_1)


# %%
sample = df.sample(frac=0.5, replace = True)

# %%
df_unique  = df.drop_duplicates()
