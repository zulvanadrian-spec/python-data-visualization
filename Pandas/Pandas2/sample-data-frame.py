# create sample data frame

import pandas as pd

data = {
    "Product":["Laptop","HandPhone","Keyboard"],
    "Price":[30000000,12000000,100000],
    "Stok":[20,15,100]
}

df = pd.DataFrame(data)
print(df)

# select a single column
print("-- SINGLE COLUMN ---\n",df["Product"])

# select a mutiple column
print("---MUTIPLE COLUMN ---\n",df[["Product","Price"]])

# select rows 'loc[]'
print("loc[]\n",df.loc[2]) # --> select rows 2 in data

# filtering data
print("---BARANG HARGA DIATAS 2jt---\n",df[df["Price"]>2000000])

# sorting data 
print("---URUTAN BARANG DRI YG TERMURAH---\n",df.sort_values("Price"))
print("---URUTAN BARANG DRI YG TERMAHAL---\n",df.sort_values("Price",ascending=False))