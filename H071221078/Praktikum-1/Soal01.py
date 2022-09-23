import math

h = float(input("tinggi menara: "))
a = float(input("sudut elevasi pengamat dengan bagian belakang kapal: "))
b = float(input("sudut elevasi pengamat dengan bagian depan kapal: "))

c = math.tan(math.radians(a)) * h
d = math.tan(math.radians(b)) * h
panjang_kapal = abs(c - d)

print("panjang kapal: ",round(panjang_kapal,1) ,"m")