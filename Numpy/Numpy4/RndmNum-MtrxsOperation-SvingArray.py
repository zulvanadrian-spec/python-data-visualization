# === RANDOM NUMBERS, MATRIX OPERARION & SAVING ARRAY ===
import numpy as np

number = np.random.randint(1,101)
print("\n--- RANDOM NUMBER ---")
print(number)

# --- GENERATE MULTIPLE RANDOM NUMBERS ---
numbers = np.random.randint(1, 11, size=5)
print("\n--- MULTIPLE RANDOM NUMBERS ---")
print(numbers)

# --- CREATE A MATRIX ---
matrix1 = np.array([
    [12,24,15],
    [23,6,78]
])
print("\n--- MATRIX ---")
print(matrix1)

# --- TRANSPOSE A MATRIX --- 
matrix2 = np.array([
    [4,6,1],
    [8,5,7]
])
print("\n--- TRANSPOSE MATRIX ---")
print(matrix2)

# --- MATRIX MULTIPLICATION ---
matrix3 = np.array([
    [1,3],
    [3,2]
])
matrix4 = np.array([
    [5,8],
    [1,6]
])
print("\n--- MATRIX MULTIPLICATION ---")
print(matrix3 @ matrix4)

# --- SAVE AN ARRAY ---
numbers2 = np.array([10,20,30,40])
np.save("numbers2.npy",numbers2)

# --- LOAD AN ARRAY ---
display = np.load("numbers2.npy") # for npy
print(display)

# np.savetxt("numbers2.txt", numbers2, fmt="%d") # for txt