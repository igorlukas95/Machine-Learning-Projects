# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:33:35 2021

@author: Nigor
"""

import pandas as pd
import numpy as np

# %%
df =pd.DataFrame(data = [12, 15, 17])

df = pd.DataFrame(data = [[12,16,23], 
                          [16,34,255]], index = ['first','second'], 
                  columns = ['col1','col2','col3'])

# %% 3x3
df = pd.DataFrame(data = [[12,16,23], 
                          [16,34,255],
                          [3112, 5534,291]], index = ['first','second','third'], 
                  columns = ['col1','col2','col3'])

# %%
d = {'one': pd.Series([1,2,3]),
     'two': pd.Series([4,5,6]),
     'flag': ['yes','no','no']}
df = pd.DataFrame(d)

# %%
d = {'one': pd.Series([1,2,3,4,5]),
     'two': pd.Series([4,5,6])}
df = pd.DataFrame(d)

# %%
d = {'one' : pd.Series(np.random.randn(100)),
    'two' : pd.Series(np.random.randn(100))}

df = pd.DataFrame(d)

# %%
df.index
df.columns
# %%
list_of_dicts = [{'apple': 1, 'orange': 4}, 
                {'apple': 3,'mango': 2, 'melon':3}]
df =pd.DataFrame(list_of_dicts)

for col in df.columns:
    print(col)
    
big_letters = [col.upper() for col in df.columns]
df.columns = big_letters

# %%

d = {'wig20': ['PKN Orlen','PKO BP','LPP'],
     'mWig40':['Amica','Playway','Benefit']}
df = pd.DataFrame(d)