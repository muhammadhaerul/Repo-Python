# #Nomor3

print("=======Masukkan 5 angka=======")

a,b,c,d,e = input("Masukkan angka: ").split(' ')

positif = 0
negatif = 0
genap = 0
ganjil = 0

a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

if a > 0:
   positif += 1
elif a < 0:
   negatif += 1

if a % 2 == 0 or a == 0:
   genap += 1
elif a % 2 == 1:
   ganjil += 1

if b > 0:
   positif += 1
elif b < 0:
   negatif += 1

if b % 2 == 0 or b == 0:
   genap += 1
elif b % 2 == 1:
   ganjil += 1

if c > 0:
   positif += 1
elif c < 0:
   negatif += 1

if c % 2 == 0 or c == 0:
   genap += 1
elif c % 2 == 1:
   ganjil += 1

if d > 0:
   positif += 1
elif d < 0:
   negatif += 1

if d % 2 == 0 or d == 0:
   genap += 1
elif d % 2 == 1:
   ganjil += 1

if e > 0:
   positif += 1
elif e < 0:
   negatif += 1

if e % 2 == 0 or e == 0:
   genap += 1
elif e % 2 == 1:
   ganjil += 1

print(f"{positif} Angka positif")
print(f"{negatif} Angka negatif")
print(f"{genap} Angka genap")
print(f"{ganjil} Angka ganjil")








