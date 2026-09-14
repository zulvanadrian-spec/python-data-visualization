import matplotlib.pyplot as plt

produts = ["Laptop","Phone","Tab"]
sales = [120,231,180]

plt.bar(produts,sales)

plt.title("product sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()