print("ketik 1 untuk menghitung penjumlahan.")
print("ketik 2 untuk menghitung pengurangan.")
print("ketik 3 untuk menghitung perkalian.")
print("ketik 4 untuk menghitung pembagian.")
print("ketik 5 untuk menghitung sisa hasil bagi(modulus).")
print("ketik 6 untuk menghitung pemangakatan.")
angka = input("masukkan pilihann anda :")
if(angka == 1):
    one = int(input("masukkan bilangan pertama :"))
    two = int(input("masukkan bilangan kedua :"))
    hasil = one - two
    print("hasil dari",one,"dijumlahkan dengan",two,"adalah",hasil)
else:
    onee = int(input("masukkan bilangan pertama :"))
    twoo = int(input("masukkan bilangan kedua :"))
    hasill = onee + twoo
    print("hasil dari",onee,"dijumlahkan dengan",twoo,"adalah",hasill)