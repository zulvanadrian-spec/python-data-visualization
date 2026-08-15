import numpy as np

numbers = np.array([10,20,30,40,50,60])
print("\n\t-->Array slicing<--\n")
# from index 1 into a index 5
print("1:5 = ",numbers[1:5])
# into a index 3
print(":3 = ",numbers[:3])
#  from a index 3 into a index 5
print("3: = ",numbers[3:])
# index 2 from a last
print("-2: = ",numbers[-2:])