# 5.identify a potensian outlier usinf=g scater plot
import matplotlib.pyplot as plt

umur = [22, 23, 24, 22, 25, 23, 24, 22, 60, 23]
gaji = [4, 4.2, 4.5, 4.1, 4.8, 4.3, 4.6, 4.2, 4.4, 4.3]  # dalam juta

plt.scatter(umur, gaji)
plt.title("Umur vs Gaji Karyawan")
plt.xlabel("Umur")
plt.ylabel("Gaji (juta)")
plt.show()