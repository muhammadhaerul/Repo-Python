print('Program cetak tahun, bulan dan hari')
print('-----------------------------------')

def myDay(usia_hari):
    tahun = usia_hari // 360
    sisa_hari = usia_hari % 360
    bulan = sisa_hari // 30
    hari = sisa_hari % 30

    print(f'{tahun} Tahun')
    print(f'{bulan} Bulan')
    print(f'{hari} Hari')

usia_hari = int(input(''))
myDay(usia_hari)
