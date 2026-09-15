# 2.compare two products using a line chart
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May"]
electronics = [110,134,125,240,220]
accescories = [90,132,135,125,155]
clothing = [100,120,125,143,155]
toys = [150,235,255,180,190]

plt.plot(months,electronics, label="Electronics")
plt.plot(months,accescories, label="Accescories")
plt.plot(months,clothing, label="Clothing")
plt.plot(months,toys, label="Toys")

plt.title("Products Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend()
plt.show()
