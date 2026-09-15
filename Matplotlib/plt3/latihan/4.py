# 4.create 2x2 subplot layout 
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,2)


axes[0][0].bar([1,2,3], [20,25,35])
axes[0][0].set_title("Sales")
axes[0][0].set_xlabel("Batch")
axes[0][0].set_ylabel("Total Sales")

axes[0][1].bar(["Electronics","Accescories","Toys"], [80,90,95])
axes[0][1].set_title("Product")
axes[0][1].set_xlabel("Category")
axes[0][1].set_ylabel("Jumlah")

plt.tight_layout()
plt.show()