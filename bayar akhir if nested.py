QTY=int(input("Banyaknya Barang Dibeli: "))
HRGBRG=int(input("Harga Barang: "))
JMLBYR= QTY * HRGBRG
diskon=JMLBYR-(JMLBYR*0.3)
BYRAKH=JMLBYR-diskon
if JMLBYR > 300000:
    if HRGBRG > 100000:
        keterangan="Dapat Kartu Diskon."
    else :
        keterangan="Tidak Dapat iskon."
else :
    keterangan="Tidak dapat Diskon."
if QTY > 100:
    diskon==diskon
else :
    diskon=0
print ("Jumlah bayar Akhir: Rp.", BYRAKH)
print ("Keterangan: ", keterangan)
if diskon > 0:
    print ("Diskon: ", diskon)
else:
    print ("")
