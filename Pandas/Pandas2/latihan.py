# 1.Display only the price column

import pandas as pd

data = {
    "Product":["Laptop","HandPhone","Keyboard"],
    "Price":[30000000,12000000,100000],
    "Stok":[20,8,100]
}

df = pd.DataFrame(data)
print("---ONLY PRICE COLUMN---\n",df["Price"])

# 2.Display Product and Stok
print("---PRODUCT & STOK---\n",df[["Product","Stok"]])

# 3.Display third row
print("---THIRD ROW---\n",df.iloc[2])

# 4.Show product with stok greater than 10
print("---PRODUCT STOCK > 10---\n",df [df["Stok"]>10])

# 5.Sort data by Stok
print("---SORT DATA BY STOCK---\n",df.sort_values("Stok", ascending=False))