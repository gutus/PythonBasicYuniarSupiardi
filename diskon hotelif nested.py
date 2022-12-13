lama=int(input("Lama Menginap:"))
harga=int(input("Harga Kamar:"))
jumlah=lama*harga
if jumlah > 300000:
    diskon=jumlah*0.35
    bayar=jumlah-diskon
    if harga > 50000:
        keterangan="Dapat Diskon Harga > 50000"
    else:
        keterangan="Tidak Dapat Diskon Harga > 50000"
else:
    keterangan="Tidak Dapat Diskon Total > 300000"
    diskon=0
if lama >= 3:
    diskon=jumlah*0.3
    bayar=jumlah-diskon
    keterangan2="Dapat Diskon Lama >3"
else:
    diskon<0
    bayar=jumlah-diskon
    keterangan2=""

print("Keterangan: ", keterangan)
print("Diskon Tambahan:",keterangan2)
print ("Jumlah= Rp.", jumlah)
print("Total Diskon= Rp.", diskon)
print("Bayar Akhir= Rp.",bayar)

