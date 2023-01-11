#2. Menginput info daya listrik dan Menghitung total tagihan listrik

golongan = str(input('golongan = '))
daya = float(input('daya = '))
Pemakaian = float(input('Pemakaian = '))

match golongan:
    case 'R1':
        if daya==900 :
            print(f'jumlah tagihan anda : {(Pemakaian*1352):,}')
        elif daya<=1300 and daya>=2200 :
            print(f'jumlah tagihan anda : {(Pemakaian*1444.70):,}')
        else:
            print("Data tidak valid")
    case 'R2':
        if daya<=3500 and daya>=5500 :
            print(f'jumlah tagihan anda : {(Pemakaian*1699.53):,}')
        else:
            print("Data tidak valid")
    case 'R3':
        if daya>=6600 :
            print(f'jumlah tagihan anda : {(Pemakaian**1699.53):,}')
        else:
            print("Data tidak valid")
    case 'B2':
        if daya>=6600 and daya<=200000 :
            print(f'jumlah tagihan anda : {(Pemakaian*1444.70):,}')
        else:
            print("Data tidak valid")
    case 'B3':
        if daya>200000 :
            print(f'jumlah pemakaian anda : {(Pemakaian*1144.74):,}')
        else:
            print("Data tidak valid")
    case 'I3':
        if daya>=200000 :
            print(f'jumlah tagihan anda : {(Pemakaian*1314.12):,}')
        else:
            print("Data tidak valid")
    case 'P1':
        if daya>=6600 and daya<=200000 :
            print(f'jumlah tagihan anda : {(Pemakaian*1523.28):,}')
        else:
            print("Data tidak valid")
    case _:
        print("Data tidak valid")