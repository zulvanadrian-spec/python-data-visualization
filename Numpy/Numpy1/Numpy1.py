import numpy as np

np.random.seed(42) # Angka Random Output nya akan Konsisiten walaupun Angka Random
# kalo gapake .seed hasilnya tidak akan Konsisten

numbers = np.random.randint(1,101) # Generate angka Random integer 1-100

print(numbers)