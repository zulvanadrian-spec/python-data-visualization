# ===== LATIHAN =====

import pandas as pd

products = pd.DataFrame({
    "ProductID":[101, 102, 103],
    "Product":["Laptop","Mobile","Tablet"]
})

sales = pd.DataFrame({
    "ProductID":[101, 102, 203],
    "Sales":[120,250,180]
})

# 1.merge two dataframe using a common column
print("\n+-+-+-+ MERGE DATA FRAME +-+-+-+\n")
print(pd.merge(products, sales, on="ProductID"))

# 2.Join two dataframe using index
print("\n+-+-+-+ JOIN TWO DATA USING INDEX +-+-+-+\n")
print(products.join(sales["Sales"]))

# 3.concatenate two dataframe
first = pd.DataFrame({
    "Value":[10,20]
})

second = pd.DataFrame({
    "Value":[30,40]
})

print("\n+-+-+-+ CONCATENATE TWO DATAFRAME +-+-+-+\n")
print(pd.concat([first, second]))

# 3.create a pivot table to calculate avarage values
data = pd.DataFrame({
    "Departement":["Sales","Sales","IT","IT"],
    "Salary":[5000000,5500000,7000000,75000000],
    "Gender":["Female","Male","Female","Male"]
})

pivot = data.pivot_table(
    values="Salary", # data yg akan di hutung di 'aggfunc'
    index=["Departement", "Gender"],
    aggfunc="mean"
)

print("\n+-+-+-+ PIVOT TABLE +-+-+-+")
print(pivot)

# 4.create crosstab for two categorical columns
data1 = pd.DataFrame({
    "Member":["Andi","Budi","Christ","Demian"],
    "Category":["Platinum","Gold","Silver",None] # jika pasangan 'None', maka "Member" tdk bisa crosstab
})

print("\n+-+-+-+ CROSSTAB +-+-+-+")
print(pd.crosstab(data1["Member"],data1["Category"]))