# create a bar chart for products sales
import matplotlib.pyplot as plt

products = ["Laptop","Mobile","Tablet"]
sales = [120,321,243]

plt.bar(products,sales)

plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()