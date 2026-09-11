import pandas as pd

data = {
    "OrderDate":["2026-08-23","2026-08-30","2026-08-15"]
}

df = pd.DataFrame(data)
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
print(df)

# 1.convert to uppercase
data2 = {
    "Product":["Laptop","Mobile","TABLET"]
}

df2 = pd.DataFrame(data2)

print("\n+-+-+ CONVERT TO UPPERCASE +-+-+")
print(df2["Product"].str.upper())

# 2.extract to month from a date column
print("\n+-+-+ CONVERT TO MONTHLY +-+-+")
print(df["OrderDate"].dt.month)

# 3.create new column using apply()
data3 = {
    "Price":[2000000,3200000,1000000]
}

df3 = pd.DataFrame(data3)

df3["Tax"] = df3["Price"].apply(lambda price: price * 0.18)
print("\n+-+-+ NEW COLUMN USING APPLY +-+-+")
print(df3)

# 4.replace text name
data4 = {
    "Name":["andi", "budi", "cici", "budi"]
}

df4 = pd.DataFrame(data4)

df4["Name"] = df4["Name"].str.replace("budi", "ambatukam")
print("\n+-+-+ REPLACE TEXT +-+-+")
print(df4)

# 5.export dataframe to csv
df3.to_csv("output_latihan.csv", index=False)