import lama as lama

banyaknya = int(input(" Banyaknya barang : \t"))
harga_satuan = int(input(" Harga Satuan : \t"))
jumlah = harga_satuan * banyaknya

if jumlah > 300000:
    if harga_satuan > 100000:
        keterangan = "Dapat Kartu Diskon dari Harga"
    else:
        keterangan = "Tidak Dapat Kartu Diskon dari Harga"
else:
    keterangan = "Tidak Dapat Kartu Diskon"
if harga_satuan > 3 :
    diskon = jumlah * 0.3
    bayar_akhir = jumlah - diskon
else:
    bayar_akhir = jumlah

print("Jumlah = Rp. ", harga_satuan, "*", banyaknya, "=", jumlah)
print("Diskon = Rp. ", harga_satuan, "* 0.3 =", int(diskon))
print("Bayar Akhir =", int(bayar_akhir))
print("Keterangan = ", keterangan)
