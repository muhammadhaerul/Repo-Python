#1. Mengembalikan nilai faktorial menggunakan recursive function

import math
def hitung_faktorial(angka) :
    faktorial = math.factorial(angka)

angka = int(input('masukkan angka :'))
print (f'nilai {angka} faktorial adalah : {hitung_faktorial(angka)}')