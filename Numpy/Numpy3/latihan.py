import numpy as np

# ===== 1. Array Indexing 2D =====

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


# ===== 2. Array Slicing =======

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


# ===== 3. Boolean Indexing =====

# Ganti Semua Nilai yg di Bawah 50 jdi 50

n_math = nilai[:, 0] # take a math collumns all rows nilai
r_math = n_math.mean() # count avarage 

state = n_math > r_math # Array True/False
siswa_abv_avrg = nama_siswa[state] # filter nama pake state yg sama

print('\n\t-->Nilai Rata-rata Matematika<--\n')
print(f"Rata-rata nilai Matematika : {r_math}\n")

print(f"Siswa yang diatas Rata-rata : \n")
for nama in siswa_abv_avrg :
    print(nama)

# ===== 4. Multiple Condition =====

# Cari Siswa dengan nilai matematika & fisika di atas 70

nilai_mtk = nilai[:, 0] # take all rows nilai, and take a math collumns
nilai_fisika = nilai[:, 1] # take all rows nilai, and take a physics collumns

state2 = (nilai_mtk > 70) & (nilai_fisika > 70)
s_diatas_70 = nama_siswa[state2]

print(f"\n\t-->Siswa IPA Unggulan<--\n")
for nama in s_diatas_70:
    print(nama)

# Cari Nilai Teratas dan Terbawah

batas_atas = 90
batas_bawah = 45

s_teratas = nilai > batas_atas
s_terbawah = nilai < batas_bawah

print('\n\t-->Nilai Teratas<--\n')
print(nilai[s_teratas])

print('\n\t-->Nilai Terbawah<--\n')
print(nilai[s_terbawah])