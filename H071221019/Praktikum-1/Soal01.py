# Menghitung Panjang Kapal

import math

h = float(input("Ketinggian Menara (m): ")) 
a = float(input("Sudut Elevasi Pengamat Terhadap Ujung Belakang Kapal : "))
b = float(input("Sudut Elevasi Pengamat Terhadap Ujung Depan Kapal : "))

belakang = h * (math.tan(math.radians(a)))
depan = h * (math.tan(math.radians(b)))
panjang = (belakang-depan)

print("Panjang Kapalnya adalah", abs(round(panjang, 1)), "m")