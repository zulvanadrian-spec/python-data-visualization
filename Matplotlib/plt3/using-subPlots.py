import matplotlib.pyplot as plt

fig, axes = plt.subplots(1,2)

# axes[0] => kotak pertama
axes[0].plot([1, 2, 3], [20, 35, 40])
axes[0].set_title("Sales")

# axes[1] => kotak kedua
axes[1].bar(["Electronics","Gadgeats","Accesories"], [20, 35, 25])
axes[1].set_title("products")

plt.tight_layout()
plt.show()