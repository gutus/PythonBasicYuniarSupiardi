qty=int(input("Banyak Barang?"))
harga=int(input("Harga Barang?"))
jumlah=qty*harga
if jumlah > 1000000:
    diskon=jumlah*0.1
    keterangan="Dapat Diskon 10%"
else:
    diskon=0
    keterangan="Tidak Dapat Diskon"
bayar=jumlah-diskon
print("Bayar= Rp.",bayar)
print(keterangan)
