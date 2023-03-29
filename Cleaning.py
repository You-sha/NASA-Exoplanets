# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 00:36:17 2023

@author: Yousha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To see all the columns
pd.set_option('display.max_rows',None)
pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)

# Loading information about every column
with open(r"PS_2023.03.18_06.37.51.csv",'r') as f:
     
     # 292 is where the information ends and dataset begins
     line_num = np.arange(292)
     instructions = []
     for i, line in enumerate(f):
         if i in line_num:
             instructions.append(line.strip())
         elif i > 292:
             break

# To cleanly read the information
for i in instructions:
    print(i)

# Taking a look at the dataset
df = pd.read_csv('PS_2023.03.18_06.37.511.csv')
df.shape # (34084, 287)
df.dtypes
df.columns

df.describe()

# There are too many columns. I'm going to remove some for the sake of
# convenience

df = df[['pl_name','sy_snum','sy_pnum','sy_mnum','discoverymethod','disc_year',
        'disc_telescope','disc_instrument','pul_flag','ptv_flag','tran_flag',
        'ast_flag','obm_flag','micro_flag','etv_flag','ima_flag','dkin_flag',
        'pl_controv_flag','pl_orbper','pl_rade','pl_masse','pl_orbeccen',
        'pl_eqt','st_teff','st_age','sy_kepmag']]
df.shape # (34084, 26)

# Reduced the colums from the original 287 to the 26 I find most interesting

# I'm going to rename the columns to something more inituitive
df = df.set_axis(['name','stars','planets','moon','discoverymethod',
                'disc_year','disc_telescope','disc_instrument','pul_flag','ptv_flag',
                'tran_flag','ast_flag','obm_flag','micro_flag','etv_flag','ima_flag',
                'dkin_flag','pl_controv_flag','orbital_period','radius(earth)',
                'mass(earth)','eccentricity','eq_temp','st_efftemp','st_age',
                'sy_keplermag'],axis = 'columns')

df.dtypes
df.describe()
df.info

# Looking at percentage of nulls
df.isnull().sum()*100/df.shape[0]

df.orbital_period.mean()
df.orbital_period.median()
plt.hist(df.orbital_period)
df.orbital_period.plot.box()

df.st_efftemp.mean()
df.st_efftemp.median()
plt.hist(df.st_efftemp)
df.st_efftemp.plot.box()



