print('Menghitung total tagihan listrik')
print('--------------------------------')

golongan = str(input('Masukkan golongan: ')).upper()
daya = float(input('Masukkan daya: '))
Pemakaian = float(input('Masukkan Pemakaian: '))

match golongan.upper():
    case "R1":
        if golongan == 'R1' and daya == 900:
            tarif = 1352
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        elif daya == 1300 or daya == 2200:
            tarif = 1444.70
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print("Data Tidak Valid")

    case "R2":
        if daya >= 3500 and daya <= 5500:
            tarif = 1699.53
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print('Data Tidak Valid')

    case "R3":
        if daya >= 6600:
            tarif = 1699.53
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print('Data Tidak Valid')

    case "B2":
        if daya >= 6000 and daya <= 200000:
            tarif = 1444.70
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print('Data Tidak Valid')

    case "B3":
        if daya > 200000:
            tarif = 1114.74
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print('Data Tidak Valid')

    case "I3":
        if daya >= 200000:
            tarif = 1314.12
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print('Data Tidak Valid')

    case "P1":
        if daya >= 6600 and daya <= 200000:
            tarif = 1523.28
            tagihan= tarif * Pemakaian
            print(f'Jumlah tagihan listrik anda : Rp{tagihan:_}'.replace('.',',').replace('_','.'))
        else:
            print('Data Tidak Valid')

    case _:
        print('Data Tidak Valid')