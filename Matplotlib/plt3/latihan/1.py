# 1.create a scatter plot with two numerical variabel
import matplotlib.pyplot as plt

hours = [1,2,3,4,5]
scores = [40,50,55,60,70]

plt.scatter(hours,scores)

plt.title("Study Hours VS Scores")
plt.xlabel("Hours")
plt.ylabel("Scores")

plt.show()