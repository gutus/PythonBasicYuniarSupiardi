lama=int(input("Lama Menginap="))
harga=int(input("Harga Kamar="))
jumlah=lama*harga
if jumlah > 300000:
    diskon=jumlah*0.3
elif jumlah > 200000 and jumlah <= 300000:
    diskon=jumlah*0.2
elif jumlah > 100000 and jumlah <=200000:
    diskon=jumlah*0.1
else :
    diskon = 0
if diskon > 0:
    keterangan = "Anda Dapat Diskon"
else :
    keterangan = "Anda Tidak Dapat Diskon"
bayar = jumlah + diskon

print ("Total Bayar=", bayar)
print("Besar Diskon=", diskon)
print("Keterangan=", keterangan)

