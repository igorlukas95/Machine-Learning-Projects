# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:15:55 2021

@author: Nigor
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# %% Loading dataset

tips = sns.load_dataset('tips')

# %% 
tips.pivot_table(values='tip',index='sex',columns='day',aggfunc='mean')

pv = tips.pivot_table(values=['tip','total_bill'],index='sex',columns='day'
                      ,aggfunc='mean')

tips.pivot_table(values='tip',index='sex',columns='day',aggfunc='min')

tips.pivot_table(values='tip',index='sex',columns=['smoker','day'],
                 aggfunc='min')

# %% Plots

tips.pivot_table(values='tip',index='sex',columns='day'
                 ,aggfunc='mean').plot(kind='bar',cmap='viridis',alpha=0.5)

tips.pivot_table(values='total_bill',index='sex',columns='day'
                 ,aggfunc='mean').plot(kind='bar',cmap='viridis',alpha=0.5)
# %%
tips.pivot_table(values='tip',index='day',columns='size'
                 ,aggfunc='mean').plot(kind='bar',cmap='viridis',alpha=0.5)

# %%
tips.pivot_table(values='total_bill',index='time',columns='size'
                 ,aggfunc='mean').plot(kind='bar',cmap='viridis',alpha=0.5)

# %% 

vals = tips[['total_bill','tip']]
vals.corr()
