import matplotlib.pyplot as plt

scores = [45,50,52,55,60,62,65,68,7072,75,80,85,90]

plt.hist(scores, bins=5)

plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.show()