#2. Menghitung FPB dari dua inputan angka integer dari dua inputan menggunakan function getFPB()

from re import A


def menentukan_fpb(a,b):
    if a>b :
        bilangan_terbesar = a
    elif b>a :
        bilangan_terbesar = b
    else : 
        bilangan_terbesar = a or b
    fpb = 0
    for i in range(1, bilangan_terbesar+1) :
        if (a%i==0) and (b%i==0) :
            fpb = i
    return fpb
    
a = int(input(''))
b = int(input(''))

print(f'FPB ({a},{b}) = {menentukan_fpb(a,b)}')