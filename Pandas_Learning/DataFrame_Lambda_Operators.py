# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:34:41 2021

@author: Nigor
"""

import pandas as pd
import numpy as np

df_raw = pd.read_clipboard()

#%%

columns = [col for col in df_raw.columns]
# %% 
df = df_raw.drop(['Czas','1r 3m'], axis = 1)

# %%
df['Wolumen'] = df['Wolumen'].apply(lambda s: s.replace(' ','')).apply(lambda s: int(s))
df['Obrót'] = df['Obrót'].apply(lambda s: s.replace(' ','')).apply(lambda s: int(s))
df['Udział'] = df['Udział'].apply(lambda s: s.replace('%','')).apply(lambda s: float(s))

