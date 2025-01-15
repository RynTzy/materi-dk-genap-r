harga = int (input("masukan harga"))
diskon = 0.05
total = float
if harga >= 100000:
    total = harga - (harga * diskon)
    print(" total bayar setelah menggunakan diskon",total)
else:
    print("tidak mendapatkan diskon, total bayar adalah",harga)