import pandas as pd

data = {
    "Departement":["Sales","IT","Sales","HR","IT","HR"],
    "Salary":[5000000,7000000,5500000,4500000,7500000,4800000],
    "Experience":[2, 5, 3, 1, 6, 2]
}

# format rupiah, semua data di parse jdi string, ketika function di panggil
def format_rupiah(x):
    return f"Rp{x:,.0f}".replace(",", ".")

df = pd.DataFrame(data)
print(df)

# 1.temukan gajih rata-rata pada setiap departement
print("\n+-+-+-+ GAJIH RATA-RATA +-+-+-+")
print(df.groupby("Departement")["Salary"].mean().apply(format_rupiah))

# 2.temukan gajih tertinggi pada setiap departement
print("\n+-+-+ DEPARTEMEN & GAJIH TERTINGGINYA +-+-+")
print(df.groupby("Departement")["Salary"].max().apply(format_rupiah))

# 3.menghitung jumlah karyawan setiap departement
print("\n+-+-+ JUMLAH KARYAWAN SETIAP DEPARTEMENT +-+-+")
print(df["Departement"].value_counts())

# 4.tampilkan nama departement / berbeda satu sama lain
print("\n+-+-+ NAMA-NAMA DEPARTEMENT +-+-+")
print(df["Departement"].unique())

# 5.sorting gajih rata-rata departemen
print("\n+-+-+ GAJIH RATA-RATA +-+-+")
result = df.groupby("Departement")["Salary"].mean()
print(result.sort_values(ascending=False).apply(format_rupiah))