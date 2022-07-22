# -*- coding: utf-8 -*-
"""Data Representation .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UQhqUNiKyaYCJM7TvarN_6UJgpASBeWZ

# ***Bangladeshi Students Survey***
*Online Survey Data of Bangladeshi Students*

### *Importing Libraries*
"""

# Commented out IPython magic to ensure Python compatibility.
# importing libraries
import pandas as pd # data processing
import numpy as np # linear algebra
import matplotlib.pyplot as plt # visualization
# %matplotlib inline

import seaborn as sns
# increases the size of sns plots
sns.set(rc={'figure.figsize':(8,6)})

"""### *Read Data*"""

# raw data in panda dataframe
df = pd.read_csv('/content/Online Survey Data on Education Bd.csv')
print('Data Frame Shape: \n{}'.format(df.shape))
# shows five instances of the dataframe
df.head()

"""### *Data Pre-processing*"""

df.columns

# investigating all the elements whithin each Feature
for column in df:
  unique_vals = df[column].unique()
  nr_values = len(unique_vals)
  
  if nr_values < 10:
    print('The number of values for feature {} :{} -- {}'.format(column, nr_values,unique_vals))
  else:
    print('The number of values for feature {} :{}'.format(column, nr_values))

# checking for the null values
df.isnull().sum()