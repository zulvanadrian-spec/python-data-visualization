import matplotlib.pyplot as plt

categories = ["Electronics","Clothing","Acssecories"]
sales = [50,40,35]

plt.pie(sales, labels=categories, autopct="%1.1f%%")
plt.title("Sales Distribution")

plt.show()