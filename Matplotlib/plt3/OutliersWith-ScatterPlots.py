# === IDENTIFY OUTLIERS WITH SCATTER PLOTS ===
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [10,12,15,18,20,50]

plt.scatter(x,y)

plt.title("Data Distributions")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)
plt.show()