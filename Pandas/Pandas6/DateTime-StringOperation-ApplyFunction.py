# === DATE TIME, STRING OPERATION, & APPLY FUNCTION ===

import pandas as pd

data = {
    "OrderDate":["2026-08-23","2026-08-30","2026-08-15"]
}

df = pd.DataFrame(data)
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
print(df)

# --- EXTRACT DATE COMPONENTS ---
print("\n+-+-+-+ EXTRACT YEAR +-+-+-+")
print(df["OrderDate"].dt.year)
print("\n+-+-+-+ EXTRACT MONTH +-+-+-+")
print(df["OrderDate"].dt.month)
print("\n+-+-+-+ EXTRACT DAY +-+-+-+")
print(df["OrderDate"].dt.day)

# --- STRING OPERATIONS ---
data2 = {
    "Product":["Laptop","Mobile","TABLET"]
}

df = pd.DataFrame(data2)

print("\n+-+-+-+ EXTRACT TO UPPERCASE +-+-+-+")
print(df["Product"].str.upper())

print("\n+-+-+-+ EXTRACT TO LOWERCASE +-+-+-+")
print(df["Product"].str.lower())

# --- REPLACE TEXT ---
data3 = {
    "Category":["Old","New","Old"]
}

df = pd.DataFrame(data3)
print("\n+-+-+-+ DATASET +-+-+-+")
print(df)

df["Category"] = df["Category"].str.replace("Old","Update") # mengganti semua 'Old' menjadi 'Update'
print("\n+-+-+-+ DATA REPLACE +-+-+-+")
print(df)

# --- APPLY CUSTOM FUNCTIONS ---
data4 = {
    "Price":[12000,20000,40000]
}

# lambda --> fungsi sekali pake / fungsi yg singkat
df4 = pd.DataFrame(data4)
df4["Tax"] = df4["Price"].apply(lambda price: price * 0.18) # '(lambda price: price * 0.18)' --> di apply pada  kolom "Price"

print("\n+-+-+-+ APPLY CUSTOM FUNCTIONS +-+-+-+")
print(df4)

# --- MAP VALUES ---

data5 = {
    "Status":[1,0,1,1,0]
}

df = pd.DataFrame(data5)

status_map = {
    1:"Active",
    0:"Inactive"
}

df["Status"] = df["Status"].map(status_map) # -> mengubah nilai menggunakan dictionary

print("\n+-+-+-+ APPLY CUSTOM FUNCTIONS +-+-+-+")
print(df)

# --- REPLACE VALUES ---
data6 = {
    "Priority":["Low","Medium","Low","High"]
}

df = pd.DataFrame(data6)
print("\n+-+-+-+ FIRST DATA +-+-+-+")
print(df)
df["Priority"] = df["Priority"].replace("Low","Normal") # mengubah 'Low' menjadi 'Normal'

print("----- REPLACE VALUES -----")
print(df)

# --- EXPORT DATA ---

# save dataframe to CSV file
df.to_csv("output_csv.csv",index=False)

# save dataframe to excel file
df4.to_excel("output_xlsx.xlsx",index=False)