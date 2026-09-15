import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May"]
sales_a = [100,120,140,160,175]
sales_b = [90,132,110,150,95]

plt.plot(months,sales_a, label="Product A")
plt.plot(months,sales_b, label="Product B")

plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()
plt.show()