# === PARACTICE EXERCISE === #

import pandas as pd
data = {
    "Product":["Laptop","Mobile",None,"Tablet"],
    "Price":[5000000,None,18000000,15000000]
}

df = pd.DataFrame(data)
print("\n=== DATA AWAL ===\n",df)

# --- count missing values --- 
print("\n+-+-+-+ COUNT MISSING VALUES +-+-+-+\n",df.isnull().sum())

# --- replace missing values with 0 ---
df ["Price"] = df["Price"].fillna(0)
print("\n+-+-+-+ REPLACE MISSING VALUES = 0 +-+-+-+\n",df)

# --- remove rows containing missing values ---
clean_df = df.dropna()
print("\n+-+-+-+ REOVE ROWS MISSING VALUES +-+-+-+\n",df)

# --- find duplicate records ---
print("\n+-+-+-+ FIND DUPLICATES +-+-+-+\n",df.duplicated())

# --- remove duplicates rows ---
df = df.drop_duplicates()
print("\n+-+-+-+ REMOVE DUPLICATE ROWS +-+-+-+\n",df)

# --- display dataset information ---
print("\n+-+-+-+ DATASET INFORMATION +-+-+-+\n")
print(df.info())