
print('Mengkonversi nilai dalam bentuk angka ke huruf')
print('----------------------------------------------')

nilai = float(input('Masukkan nilai: '))

if nilai >= 90:
    grade = 'A'
elif nilai >= 80:
    grade = 'B'
elif nilai >= 70:
    grade = 'C'
elif nilai >= 60:
    grade = 'D'
elif nilai >= 40:
    grade = 'E'
else:
    grade = 'F'

print('Nilai', nilai, '=' , format(grade))
