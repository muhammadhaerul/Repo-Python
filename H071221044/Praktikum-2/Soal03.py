#3. Inputan Bilangan Bulat

angka = list(map(int,input('').split()))
angka_ganjil = sum (1 for i in angka if i%2!=0)
angka_genap = sum(1 for i in angka if i%2==0)
angka_positif = sum(1 for i in angka if i>0)
angka_negatif = sum(1 for i in angka if i<0)
print (f'{angka_genap} angka genap')
print (f'{angka_ganjil} angka ganjil')
print (f'{angka_positif} angka positif')
print (f'{angka_negatif} angka negatif') 