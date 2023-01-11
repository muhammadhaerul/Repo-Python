print('Program Menghitung FPB Menggunakan Function')
print('-------------------------------------------')

def getFPB(a,b):
    if a >= b:
        bil_terbesar = a
        bil_terkecil = b
    elif b > a:
        bil_terbesar = b
        bil_terkecil = a
    
    fpb = 0
    for i in range(bil_terkecil, bil_terbesar + 1):
        if i != 0:
            if(a % i == 0) and (b % i == 0):
                fpb = i
    return abs(fpb)

a = int(input(''))
b = int(input(''))

print(f'FPB ({a},{b}) = {getFPB(a,b)}')