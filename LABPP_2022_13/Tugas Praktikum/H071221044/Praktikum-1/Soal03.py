#3. Hitung gaji karyawan

input('Nama: ')
a = float(input('Gaji pokok: '))
b = float(input('Total penjualan: '))
c = b * 0.15
d = round(a + c,2)

print('TOTAL = $' ,d)