print('\nMenghitung panjang kapal')

h = float(input('\nMasukkan tinggi menara : '))
a = int(input('Masukkan Sudut elevasi pengamat terhadap ujung belakang kapal : '))
b = int(input('Masukkan Sudut elevasi pengamat terhadap ujung depan kapal : '))

import math

ac = math.tan(math.radians(a))*h
bc = math.tan(math.radians(b))*h

ab = float(ac-bc)
print ('\nPanjang kapal : ', abs(round(ab,1)), 'm')
