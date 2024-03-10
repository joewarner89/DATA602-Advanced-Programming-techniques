

import numpy as np
import pandas as pd

#1
# Creating a NumPy array
np_array = np.array([1, 2, 3, 4, 5])

# Creating a pandas Series
pd_series = pd.Series([1, 2, 3, 4, 5])

# Adding two elements of the array
np_array_sum = np_array[0] + np_array[1]

# Adding two elements of the series
pd_series_sum = pd_series[0] + pd_series[1]

print("NumPy Array:", np_array)
print("pandas Series:", pd_series)
print("Sum of two elements in NumPy Array:", np_array_sum)
print("Sum of two elements in pandas Series:", pd_series_sum)

#3


# Creating a 1D array of numbers from 0 to 9
array_1d = np.arange(10)

print("Desired Output:")
print(array_1d)

#4

# Given array
arr1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Extracting odd numbers using Boolean indexing
odd = arr1[arr1 % 2 != 0]

print("Odd numbers extracted from array1:")
print(odd)

#5

# Get the common items between a and b

#input
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

common_items = np.intersect1d(a, b)

print(common_items)

# 6
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

same = np.setdiff1d(a, b)

print(same)

import numpy as np

# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])

# Check for missing values
missing_values = np.isnan(iris).any()

if missing_values:
    print("The Iris dataset contains missing values.")
else:
    print("The Iris dataset does not contain any missing values.")


