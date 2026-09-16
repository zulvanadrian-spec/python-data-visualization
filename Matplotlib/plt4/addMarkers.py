# === ADD MARKERS ===
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]
sales = [100,120,150,180]

plt.plot(months,sales, marker="s")
# "s" -> Square
# "o" -> Circle
# "^" -> Triangle
# "." -> Star

plt.title("Monthly Sales")

plt.show()