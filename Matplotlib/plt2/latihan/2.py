# create a horizontal bar chart
import matplotlib.pyplot as plt

fruits = ["Aple","Avocado","Manggo","Strawberry"]
sales = [60,100,98,88,]

plt.barh(fruits,sales)

plt.title("Fruits Sales")
plt.xlabel("Fruits")
plt.ylabel("Sales")

plt.show()