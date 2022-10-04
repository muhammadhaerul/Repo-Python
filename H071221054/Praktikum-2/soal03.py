print('Menentukan Bilangan ganjil genap dari 5 bilangan')
print('------------------------------------------------')

genap = 0
ganjil = 0
positif = 0
negatif = 0

a,b,c,d,e = input('').split()

if not a.isnumeric():
    if a[0] == '-' and len(a):
        negatif += 1
    else:
        print('Inputan Tidak Valid')
        exit()
a = int(a)
if a%2 == 0:
    genap+=1
elif a%2 != 0:
    ganjil+=1
if a > 0:
    positif+=1

if not b.isnumeric():
    if b[0] == '-' and len(b):
        negatif += 1
    else:
        print('Inputan Tidak Valid')
        exit()
b = int(b)
if b%2 == 0:
    genap+=1
elif b%2 !=0:
    ganjil+=1
if b > 0:
    positif+=1

if not c.isnumeric():
    if c[0] == '-' and len(c):
        negatif += 1
    else:
        print('Inputan Tidak Valid')
        exit()
c = int(c)
if c%2 == 0:
    genap+=1
elif c%2 != 0:
    ganjil+=1
if c > 0:
    positif+=1

if not d.isnumeric():
    if d[0] == '-' and len(d):
        negatif += 1
    else:
        print('Inputan Tidak Valid')
        exit()
d = int(d)
if d%2 == 0:
    genap+=1
elif d%2 != 0:
    ganjil+=1
if d > 0:
    positif+=1

if not e.isnumeric():
    if d[0] == '-' and len(e):
        negatif += 1
    else:
        print('Inputan Tidak Valid')
        exit()
e = int(e)
if e%2 == 0:
    genap+=1
elif e%2 != 0:
    ganjil+=1
if e > 0:
    positif+=1

print(genap,'Angka Genap')
print(ganjil,'Angka Ganjil')
print(positif,'Angka Positif')
print(negatif,'Angka Negatif')