NIM=int(input("NIM:"))
NAMAMHS=str(input("Nama Mahasiswa:"))
NILAIPY=int(input("Nilai Python:"))
if NILAIPY >= 80:
    INDEK="A"
elif NILAIPY < 80 and NILAIPY >= 70:
    INDEK="B"
elif NILAIPY < 70 and NILAIPY >= 55:
    INDEK="C"
elif NILAIPY < 55 and NILAIPY >= 40:
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
