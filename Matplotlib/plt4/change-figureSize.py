# ==== CHANGE FIGURE SIZE ====
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]
sales = [100,120,150,180]

plt.figure(figsize=(8,5)) # --> figure is 8 inches wide, and 5 inches tall 

plt.plot(months,sales)

plt.title("Monhtly Sales")
plt.xlabel("Month")
plt.ylabel("sales")

plt.show()