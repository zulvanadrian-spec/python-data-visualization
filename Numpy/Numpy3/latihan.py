import numpy as np

# 1.Array Indexing 2D
np.random.seed(42)

nilai = np.random.randint(40, 100, size=(5, 4))
nama_siswa = np.array(['Andi', 'Budi', 'Citra', 'Dewi', 'Eka'])
mapel = np.array(['Math', 'Physics', 'Chemistry', 'Biology'])

# Ambil nilai 'Physics' milik 'Citra'
print(f"\n\t-->Nilai Fisika Citra<--\n")
print(f"Nilai {mapel[1]} -> {nama_siswa[2]}: {nilai[2, 1]}") # -> row 2 (citra), col 1 (physics)

# Nilai Kimia all Siswa
print("\n\t-->Nilai Chemitry all siswa<--\n")
print(f"Nilai {mapel[2]} : ")
print(f"{nama_siswa[0]} --> {nilai[0, 2]}") # row 0 -> andi, col 2 -> chemistry
print(f"{nama_siswa[1]} --> {nilai[1, 2]}") # row 1 -> budi, col 2 -> chemistry
print(f"{nama_siswa[2]} --> {nilai[2, 2]}") # row 2 -> citra, col 2 -> chemistry
print(f"{nama_siswa[3]} --> {nilai[3, 2]}") # row 3 -> dewi, col 2 -> chemistry
print(f"{nama_siswa[4]} --> {nilai[4, 2]}") # row 4 -> eka, col 2 -> chemistry


# Ambil  Semua Nilai Milik Siswa (Satu Baris full)
print(f"\n\t-->Nilai all Mapel<--\n")

# Nilai all Mapel Budi
print(f"Nilai {mapel} : ")
print(f"{nama_siswa[0]} : {nilai[0, :]}\n") # Matrix Row Index 0 full

# Nilai all Mapel Andi
print(f"Nilai {mapel} : ")
print(f"{nama_siswa[1]} : {nilai[1, :]}\n") # Matrix Row Index 1 full

# Nilai all Mapel Citra
print(f"Nilai {mapel} : ")
print(f"{nama_siswa[2]} : {nilai[2, :]}\n") # Matrix Row Index 2 full

# Nilai all Mapel Dewi
print(f"Nilai {mapel} : ")
print(f"{nama_siswa[3]} : {nilai[3, :]}\n") # Matrix Row Index 3 full

# Nilai all Mapel Eka
print(f"Nilai {mapel} : ")
print(f"{nama_siswa[4]} : {nilai[4, :]}\n") # Matrix Row Index 4 full