nama = str(input("Nama Mahasiswa : "))
nim = int(input("NIM :"))
python = int(input("Nilai Python :"))
nilaipy = ""
if python <= 30:
    nilaipy = "E"
elif 40 <= python < 55:
    nilaipy = "D"
elif 55 <= python < 70:
    nilaipy = "C"
elif 70 <= python < 80:
    nilaipy = "B"
else:
    nilaipy = "A"

print("Nama \t:", nama)
print("NIM \t:", nim)
print("Nilai Python \t:", python)
print("Mutu Huruf \t:", nilaipy)