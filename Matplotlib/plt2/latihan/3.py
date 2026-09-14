# create a pie chart showing category distributions
import matplotlib.pyplot as plt

categories = ["Electronics","Clothing","Acsecories","Toys"]
sales = [80,76,100,150]

plt.pie(sales, labels=categories, autopct="%1.1f%%")

plt.title("Sales Distribution")
plt.show()