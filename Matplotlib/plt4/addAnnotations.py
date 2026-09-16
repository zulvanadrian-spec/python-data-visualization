# === ADD ANNOTATIONS ===
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]
sales = [100,120,150,130]

plt.plot(months, sales, marker="s")

plt.annotate(
    "Highest Sales",
    xy=("Mar", 150),
    xytext=("Feb", 145) # posisi text berdasarkan letak x y figure
)

plt.show()