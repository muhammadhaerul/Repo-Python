#Nomor 1

print("Menghitung panjang kapal")

import math

h = int(input("Ketinggian menara: "))
a = int(input("Sudut elevasi ujung depan kapal: "))
b = int(input("Sudut elevasi ujung belakang: "))

a = math.tan(math.radians(a))*h
b = math.tan(math.radians(b))*h

Panjang_kapal = a-b
Panjang_kapal = float (abs(round(Panjang_kapal, 1)))
print("Panjang kapal: ",Panjang_kapal, 'm')

