lama=int(input("Lama Menginap: "))
harga=int(input("Harga Kamar :"))
diskon3=diskon1+diskon2
jumlah = lama * harga
if jumlah > 300000:
    if harga > 50000:
        keterangan="Dapat Kartu Diskon"
        diskon1=jumlah-(jumlah*0.25)
    else :
        keterangan="Tidak Dapat kartu Diskon Harga > 50000"
        diskon1=jumlah
else :
    keterangan="Tidak Dapat Kartu Diskon Jumlah > 300000"
if lama > 3 :
        bayar=jumlah-(jumlah * 0.3)
        keterangan2="Dapat Diskon Lama Menginap > 3"
        diskon2=jumlah*0.3
else :
        bayar=jumlah
        keterangan2=""
        diskon2=0
print ("Jumlah=Rp. ", jumlah)
print ("Keterangan: ", keterangan)
print ("            ", keterangan2)
print ("Bayar Akhir :", bayar)
print ("Diskon:", diskon3)
