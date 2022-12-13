orang = {"nama": "Ganesha noor", "kota": "Sukabumi", "Umur" : "8"}
try:
    contact = open("contact.txt", "r")
    print(orang["pekerjaan"])
except IOError as err:
    print("Terjadi kesalahan pada akses list/dict/tuple:", err)
finally:
    print("Baris ini akan selalu dieksekusi")
print(orang)