golongan = input("golongan: ")
daya = float(input("daya: "))
pemakaian = float(input("pemakaian: "))

match golongan:
    case 'R1':
        if daya == 900:
            tarif = pemakaian*1352
        elif daya == 1300 or daya == 2200:
            tarif = pemakaian*1444.70
        else:
            print("data tidak valid")

    case 'R2':
        if daya >= 3500 and daya <= 5500:
            tarif = pemakaian*1699.53
        else:
            print("data tidak valid")
    
    case 'R3':
        if daya >= 6600:
            tarif = pemakaian*1699.53
        else:
            print("data tidak valid")
        
    case 'B2':
        if daya >= 6600 and daya <= 200000:
            tarif = pemakaian*1444.70
        else:
            print("data tidak valid")
    
    case 'B3':
        if daya >= 200000:
            tarif = pemakaian * 1114.74
        else:
            print("data tidak valid")

    case 'I3':
        if daya >= 200000:
            tarif = pemakaian * 1314.12
        else:
            print("data tidak valid")

    case 'P1':
        if daya >= 6600 and daya <= 200000:
            tarif= pemakaian * 1523.28
        else:
            print("data tidak valid")
            
    case _:
        print("data tidak valid")

print('jumlah tagihan anda: {0:_}'.format(tarif).replace('.',',').replace('_','.'))