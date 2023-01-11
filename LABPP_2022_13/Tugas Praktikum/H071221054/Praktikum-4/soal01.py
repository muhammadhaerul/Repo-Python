print('Program Nilai Faktorial dengan Fungsi Rekursif')
print('----------------------------------------------')

def fa(n):
    if n == 0:
        return 1
    elif n < 0:
        return 'Tidak Terdefinisi'
    else:
        return n*fa(n-1)

n = int(input(''))

print(fa(n))