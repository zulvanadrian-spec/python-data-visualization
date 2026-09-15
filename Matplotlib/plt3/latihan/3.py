# 3.create two charts using subplots
import matplotlib.pyplot as plt

years = [2022,2023,2024,2025,2026]
intern = [80,100,140,225,180]
employee = [200,250,210,300,450]

plt.subplot(2,1,1)
plt.plot(years,intern)
plt.title("internship position")
plt.xlabel("Years")
plt.ylabel("intern")

plt.subplot(2,1,2)
plt.plot(years,employee)
plt.title("permanent employees")
plt.xlabel("Years")
plt.ylabel("employeee")

plt.tight_layout()
plt.show()