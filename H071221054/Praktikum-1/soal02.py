print('Program Mengubah detik ke dalam format jam:menit:detik')
print('------------------------------------------------------')

detik = int(input('Masukkan jumlah detik yang akan di konversi : '))

jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(f'{jam:02d} : {menit:02d} : {detik:02d}')