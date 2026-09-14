# Create a histogram using numerical data 
import matplotlib.pyplot as plt

nilai = [45, 67, 78, 88, 92, 55, 60, 73, 81, 95, 50, 68, 77, 85, 90, 62, 71, 79, 83, 88]

plt.hist(nilai, bins=5)
plt.title("Distribusi Nilai Ujian")
plt.xlabel("Rentang Nilai")
plt.ylabel("Jumlah Mahasiswa")
plt.show()