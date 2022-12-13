NIM=int(input("NIM:"))
NAMAMHS=str(input("Nama Mahasiswa:"))
NILAIPY=int(input("Nilai Python:"))
if NILAIPY >= 80:
    INDEK="A"
elif  80 < NILAIPY >= 70:
    INDEK="B"
elif 70 < NILAIPY >= 55:
    INDEK="C"
elif 55 < NILAIPY >= 40:
    INDEK="D"
else :
    INDEK="E"
if INDEK=="E":
    keterangan="TIDAK LULUS"
else :
    keterangan="Lulus"

print ("Nama Mahasiswa:", NAMAMHS)
print ("Nilai Python:", NILAIPY)
print ("Mutu Huruf:", INDEK)
print ("Keterangan", keterangan)
