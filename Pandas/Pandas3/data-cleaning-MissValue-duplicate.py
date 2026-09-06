# === DATA CLEANING, MISSING VALUES & DUPLICATE === #

import pandas as pd

data = {
    "Product":["Laptop","Mobile",None,"Tablet"],
    "Price":[5000000,None,18000000,15000000]
}

df = pd.DataFrame(data)
print("\n=== DATA AWAL ===\n",df)

# --- detecting missing values ---
print("\n=== IDENTIFIKASI DATA YG HILANG ===\n",df.isnull())
print("\n=== HITUNG JUMLAH DATA YG HILANG SETIAP KOLOM ===\n",df.isnull().sum())

# --- remove missing values ---
clean_df = df.dropna()
print("\n=== MENGHAPUS DATA YANG HILANG ===\n",clean_df)

# --- fill missing values ---
df["Price"] = df["Price"].fillna(11000000) # '.fillna' automatically fill in the empty data in those rows
print("\n=== DATA 'PRICE' 'MOBILE' TELAH DIISI ===\n",df)
# replace missing product names
df["Product"] = df["Product"].fillna("Monitor")
print("\n=== DATA 'PRODUCT' 'PRICE' -> 18000000  TELAH DIISI ===\n",df)

# --- remove duplicate rows ---
df = df.drop_duplicates()
print("\n=== MENGHAPUS DATA DUPLIKAT ===\n",df)

# --- check data information ---
print("\n=== DATA INFORMATION ==\n")
print(df.info())

# --- generate summary statistics ---
print("\n=== SUMMARY STATICS ===\n",df.describe())