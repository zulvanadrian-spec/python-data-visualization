import matplotlib.pyplot as plt

months = ['jan','feb','mar', 'apr']
sales = [120, 150, 180, 200]

plt.plot(months, sales, label='Sales')

plt.title('Monthly Sales') # Judul 
plt.xlabel('Month') # Label Bawah
plt.ylabel('Sales') # Label Kiri


plt.grid(True) # Garis Jalur
plt.legend() # Tampilkan Penjualan Terlaku

plt.show()