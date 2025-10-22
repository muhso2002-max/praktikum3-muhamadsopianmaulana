# Program menentukan bilangan terbesar dari 3 bilangan

# Input tiga bilangan
a = int(input("masukan bilangan pertama: "))
b = int(input("masukan bilangan kedua: "))
c = int(input("masukan bilangan ketiga: "))

# Menentukan tiga bilangan terbesar
if a >= b and a >= c:
    print("bilangan terbesar adalah :", a)
elif  b >= a and b >= c:
    print("bilangan terbesar adalah:", b)
else:
    terbesar = c

# Menampilkan hasil
    print(f"bilang terbesar adalah: {terbesar}")
