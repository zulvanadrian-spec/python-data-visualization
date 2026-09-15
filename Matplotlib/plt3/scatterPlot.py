import matplotlib.pyplot as plt

hours = [1,2,3,4,5]
scores =[45,50,60,70,85]

plt.scatter(hours,scores)

plt.title("Study Hours VS Score")
plt.xlabel("Study Hours")
plt.ylabel("score")

plt.grid(True)
plt.show()