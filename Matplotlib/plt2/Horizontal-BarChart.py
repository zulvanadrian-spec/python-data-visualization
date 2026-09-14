import matplotlib.pyplot as plt

fruit = ["Aple","Manggo","Strawberry","Banana"]
sales = [120,342,213,164]

plt.barh(fruit,sales)

plt.title("Fruit Sales")
plt.xlabel("Sales")
plt.ylabel("Fruit")

plt.show()