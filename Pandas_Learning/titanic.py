# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:12:23 2021

@author: Nigor
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# %% zbiór danych
tit = sns.load_dataset('titanic')

# %% grouping by sex and plotting

tit.groupby('sex').size().plot(kind='bar', alpha = 0.5)
tit.groupby(['sex','survived']).size()
# %% grouping by classes
tit.groupby('class').size().plot(kind='bar')
tit.groupby('class').mean()['survived'].plot(kind='bar')

r = pd.pivot_table(data=tit, values='survived',index='sex',columns='class'
               , aggfunc='count')
# %% marking variable age cathegorical and grouping by age

tit['age_bin'] = pd.cut(x=tit['age'], bins=[0,18,80])
pv = pd.pivot_table(data=tit, values = 'survived',index = 'age_bin',columns='class'
               ,aggfunc='count')

# %% marking subplots
fig,ax = plt.subplots(1,2,sharey=True)
tit.groupby(['sex','survived']).size()['male'].plot(ax=ax[0],kind='bar')
tit.groupby(['sex','survived']).size()['female'].plot(ax=ax[1],kind='bar')
ax[0].legend('male')
ax[1].legend('female')

# %% pivoting table

r = pd.pivot_table(data=tit, values='age',index='survived',columns='sex'
               , aggfunc='count')
r.plot(subplots = True, kind='bar',sharey=True,layout=(1,2))

# %% aggregatino

agg =  pd.pivot_table(data=tit,index='sex',columns='class',
               aggfunc={'survived': sum, 'fare': 'mean','age':'mean'})
