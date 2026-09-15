import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]
sales = [100,120,140,160]
expenses = [90,80,70,85]

plt.subplot(2,1,1) # -> 2 rows, 1 columns, first chart
plt.plot(months,sales)
plt.title("Sales")

plt.subplot(2,1,2) # -> 2 rows, 1 columns, second chart
plt.plot(months,expenses)
plt.title("Expenses")

plt.tight_layout()
plt.show()