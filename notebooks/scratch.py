##########################################################
##########################################################
##########################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# System Confirmation
print("Environment is working.")
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)


# Testing Pandas

print(pd.options.display.max_rows)

# Test Example of a DataFrames

test_data_set = {
    'time': ['1', '2', '3'],
    'price': ['15', '20', '25']
}

price_test = pd.DataFrame(test_data_set)
print(price_test)

"""
   time price
0    1    15
1    2    20
2    3    25
"""

print(price_test.loc[0])
print(price_test.loc[[0, 1]])

"""
time      1
price    15
Name: 0, dtype: str

   time price
0    1    15
1    2    20
"""

price_test = pd.DataFrame(test_data_set, index = ['hour1', 'hour2', 'hour3'])
print(price_test)

"""
      time price
hour1    1    15
hour2    2    20
hour3    3    25
"""

# Test example of .Series function

alpha = ['2', '9', '81']
beta = {'day': 120, 'week': 4, 'hour': 9}

series_test = pd.Series(alpha)
series_test2 = pd.Series(beta, index = ['day', 'hour'])

print(series_test)
print(series_test2)

"""
0     2
1     9
2    81
dtype = str

day     120
hour      9
dtype: int64
"""

# Regular Indexing
print(series_test[0])

"""
2
"""

# Labels function
labels_test = pd.Series(alpha, index = ['x', 'y', 'z'])
print(labels_test)

"""
x     2
y     9
z    81
dtype = str
"""

# Can now access each variable through the labels
print(labels_test['y'])
"""
9
"""


# Loading files into a DataFrame

csv = r'C:\Users\olive\OneDrive\Desktop\filler.csv'

df = pd.read_csv(csv)

# print(df)

##########################################################
##########################################################
##########################################################