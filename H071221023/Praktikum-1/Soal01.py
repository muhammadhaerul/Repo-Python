import math
h = float (input("Masukkan Ketinggian Menara (dalam satuan meter):"))
a = float (input("Masukkan Derajat Sudut Elevasi Pengamat Terhadap ujung belakang kapal:"))
b = float (input("Masukkan Derajat Sudut Elevasi Pengamat Terhadap ujung depan kapal:"))

belakang = h * (math.tan(math.radians(a)))
depan = h * (math.tan(math.radians(b)))
panjang = belakang-depan 

print ("Panjang kapalnya adalah" , abs(round(panjang,1)), "m"  )