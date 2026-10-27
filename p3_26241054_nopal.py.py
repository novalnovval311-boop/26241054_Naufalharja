nama = input("Masukkan nama mahasiswa       : ")
nim = int(input("Masukkan NIM                  : "))
prodi = input("Masukkan program studi        : ")
dua_digit = int(input("Masukkan 2 digit terakhir NIM : "))

# 2. Tampilkan hasil
print()
print("=" * 32)
print("     IDENTITAS MAHASISWA")
print("=" * 32)
print("Nama        :", nama)
print("NIM         :", nim)
print("Prodi       :", prodi)
print("2 Digit NIM :", dua_digit)
print()

# 3. Tampilkan tipe data
print("Tipe Data Nama        :", type(nama).__name__)
print("Tipe Data NIM         :", type(nim).__name__)
print("Tipe Data Prodi       :", type(prodi).__name__)
print("Tipe Data 2 Digit NIM :", type(dua_digit).__name__)
print("=" * 32)