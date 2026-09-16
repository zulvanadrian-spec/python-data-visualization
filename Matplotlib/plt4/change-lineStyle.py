# === CHANGE LINE STYLE ===
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x,y, linestyle="-.")
# "-" -> Solid
# "--" -> Dashed
# ":" -> Doted
# "-." -> Dash-dot

plt.show()