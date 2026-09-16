# === SET AXIS LIMITS ===
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,15,40]

plt.plot(x,y)

plt.xlim(1, 5) # -> sumbu x hanya menampilkan range 1 - 5
plt.ylim(0, 60) # -> sumbu y hanya menampilkan range 0 - 60

plt.show()