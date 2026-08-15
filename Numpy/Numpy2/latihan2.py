'''
1.cretae a 3x3 array 
2.find its shape
3.reshape a 1D array into a 2x4 array
4.find the sum, mean, minimum and maximum values
5.calculate the median and std deviation
'''

import numpy as np

numbers = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print("sum = ",np.sum(numbers))
print("mean = ",np.mean(numbers))
print("minimum = ",np.min(numbers))
print("maximum =",np.max(numbers))
print("median =",np.median(numbers))
print("stndard deviation =",np.std(numbers))

# Reshape Array
array = np.array([10,20,30,40,50,60,70,80])
new_array = array.reshape(2,4)
print(f"array reshape : \n{new_array}")