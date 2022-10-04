# Program untuk menentukan nilai terbesar dari tiga angka

a = int(input("Angka_1 = "))
b = int(input("Angka_2 = "))
c = int(input("Angka_3 = "))

if a >= b and a >= c:
    print(">", a, "adalah nilai terbesar")
elif b >= a and b >= c:
    print(">", b, "adalah nilai terbesar")
else:
    print(">", c, "adalah nilai terbesar")