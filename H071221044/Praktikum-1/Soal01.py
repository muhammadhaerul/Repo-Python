1. #Menghitung panjang kapal

import math
h = float(input('Masukkan tinggi menara : '))
b = float(input('Masukkan sudut elevasi pengamat terhadap ujung kapal : ')) 
a = float(input('Masukkan sudut elevasi pengamat terhadap ujung belakang kapal : '))

ac = math.tan(math.radians(a))*h
bc = math.tan(math.radians(b))*h
result = (bc - ac)

print("{:.1f}m".format(result))