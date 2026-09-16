# === ADD MULTIPLE ELEMENTS TOGETHER ===
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]
sales = [110,120,150,130]
cash = [50,40,20,80]
qris = [60,80,130,50]

plt.figure(figsize=(8, 5))

plt.plot(
    months,
    sales,
    marker="^",
    linestyle="-.",
    label="Sales",
)
plt.plot(
    cash,
    marker="o",
    linestyle="--",
    label="Cash Payment",
)
plt.plot(
    qris,
    marker="s",
    linestyle=":",
    label="Qris Payment",
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)
plt.legend()

plt.show()