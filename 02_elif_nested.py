lama = int(input(" Lama menginap : \t"))
harga = int(input(" Harga Kamar : \t"))
jumlah = harga * lama

if jumlah > 300000:
    if harga > 50000:
        keterangan = "Dapat Kartu Diskon dari Harga"
    else:
        keterangan = "Tidak Dapat Kartu Diskon dari Harga"
else:
    keterangan = "Tidak Dapat Kartu Diskon"
if lama > 3 :
    diskon = jumlah * 0.3
    bayar = jumlah - diskon
else:
    bayar = jumlah

print("Jumlah = Rp. ", harga, "*", lama, jumlah)
print("Diskon = Rp. ", diskon)
print("Keterangan = ", keterangan)
print("Bayar Akhir =", bayar)