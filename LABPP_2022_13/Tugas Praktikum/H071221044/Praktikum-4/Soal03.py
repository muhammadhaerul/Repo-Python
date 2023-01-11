#3. Cetak 'tahun','bulan' ,dan 'hari' menggunakan function myDay()

def myDay(usia_hari) :
    tahun = usia_hari//365
    sisa_hari = usia_hari%365
    bulan = sisa_hari//30
    hari = sisa_hari%30
    print(f'{tahun} Tahun')
    print(f'{bulan} Bulan')
    print(f'{hari} hari')

usia_hari = int(input(''))
myDay(usia_hari)