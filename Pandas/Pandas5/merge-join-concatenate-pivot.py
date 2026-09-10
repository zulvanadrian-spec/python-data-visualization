# === MERGE, JOIN, CONCATENATE AND PIVOT TABLES ===

import pandas as pd

products = pd.DataFrame({
    "ProductID":[101, 102, 103],
    "Product":["Laptop","Mobile","Tablet"]
})

sales = pd.DataFrame({
    "ProductID":[101, 102, 203],
    "Sales":[120,250,180]
})

# --- MERGE DATA FRAME ---
result = pd.merge(products,sales, on="ProductID") # menggabungkan berdasarkan nilai kolom yg sama ("ProductID")
print("\n+-+-+-+ MERGE DATA FRAME +-+-+-+\n")
print(result)

print("HANYA YG COCOK DRI KEDUANYA :\n",pd.merge(products, sales, on="ProductID", how="inner"))   # default: cuma yg cocok di 2-2nya
print("SEMUA DARI KIRI 'product' :\n",pd.merge(products, sales, on="ProductID", how="left"))     # semua dari kiri (products), walau gak ada pasangannya
print("SEMUA DARI KANAN 'sales' : \n",pd.merge(products, sales, on="ProductID", how="right"))    # semua dari kanan (sales)
print("SEMUA DATA DARI KIRI MAUPUN KANAN : \n",pd.merge(products, sales, on="ProductID", how="outer"))    # semua data, dari kiri MAUPUN kanan

# --- JOIN DATA FRAME ---
print("\n+-+-+-+ JOIN DATA FRAME +-+-+-+\n")
print(products.join(sales["Sales"])) # menggabungkan  berdasarkan index

# --- CONCATENATE DATA FRAME ---
first = pd.DataFrame({
    "Value":[10,20]
})

second = pd.DataFrame({
    "Value":[30,40]
})

print("\n+-+-+-+ CONCATENATE DATA FRAME +-+-+-+\n")
print(pd.concat([first, second])) # menggabungkan data secara vertikal

# --- CRETAE A PIVOT TABLE ---
data = pd.DataFrame({
    "Departement":["Sales","Sales","IT","IT"],
    "Salary":[5000000,5500000,7000000,7500000],
    "Gender":["Female","Male","Female","Male"]
})
pivot = data.pivot_table(
    values="Salary", # kolom yg mau di hubungkan
    index="Departement", # kolom yg jadi 'pengelompokan' (baris hasil)
    aggfunc="mean" # cara ngitung ny (mean, sum, max, min, dll)
)
pivot2 = data.pivot_table(
    values="Salary",
    index="Departement",
    columns="Gender", # jadikan kolom "Gender" jadi sebuah KOLOM di hasil pivot
    aggfunc="mean"
)
# kelompokan data berdasarkan Departement, lalu hitung rata-rata Salary nya
print("\n+-+-+-+ PIVOT TABLE SUMMARIZE DATA QUICKLY +-+-+-+")
print(pivot)

print("\n+-+-+-+ PIVOT TABLE WITH GENDER +-+-+-+")
print(pivot2)

# --- CREATE A CROSSTAB ---
data = pd.DataFrame({
    "Departement":["Sales","Sales","IT","HR"],
    "Shift":["Morning","Evening","Morning","Evening"]
})
# membuat tabel, tiap kombinasi Departement x shift, itung ada berapa data yang cocok
print("\n+-+-+-+ CREATE CROSSTAB +-+-+-+\n")
print(pd.crosstab(data["Departement"],data["Shift"])) 
'''
HR - Evening → ada 1 data (Evening shift di HR)
HR - Morning → ada 0 data (gak ada yang Morning di HR)
Sales - Evening → ada 1 data
Sales - Morning → ada 1 data
IT - Evening  → ada 0 data
IT - Morning  → ada 1 data
'''