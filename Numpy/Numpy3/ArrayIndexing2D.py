import numpy as np

matrix = np.array([
    [10,20,30], # index 0
    [40,50,60], # index 1 -> index 2 in index 1 = 60
    [70,80,90]  # index 2
])

# Indexing 2D
print("\n\t-->Indexing 2D Array<--")
print(matrix[1,2]) # [1]-> index 1 = [40,50,60], # [2]-> take a colloumns index 2 in index 1 = 60

# Indexing Collumns & Rows
print('\n\t-->Access an entire Column<--\n')
print('Rows 1 Collumns 2 : ',matrix[:,1]) # Access a collumns index 1 & Rows Index 0 to all index