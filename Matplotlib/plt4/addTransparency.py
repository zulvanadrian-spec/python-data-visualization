# === ADD TRANSPARENCY ===
import matplotlib.pyplot as plt

category = ["A","B","C"]
values = [20,35,25]

plt.bar(category, values, alpha=0.5) # atur transparansi bar chart, 0-1

plt.show()