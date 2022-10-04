#Nomor2

golongan = str(input("Golongan: "))
daya = int(input("Daya: "))
pemakaiaan = int(input("Pemakaiaan: "))

match golongan:
    case 'R1':
        if daya == 900:
            tarif = 1352
            harga = "Jumlah tagihan anda: {:_}".format(pemakaiaan*tarif)
            print(harga.replace('.',',').replace('_','.'))
        elif daya == 1300 or daya == 2200:
            tarif = 1444.70
            harga = "Jumlah tagihan anda: {:_}".format(pemakaiaan*tarif)
            print(harga.replace('.',',').replace('_','.'))
        else:
            print('Data tidak valid')
    
    case 'R2':
        if daya >= 3500 and daya <= 5500:
            tarif = 1699.53
            harga = "Jumlah tagihan anda: {:_}".format(pemakaiaan*tarif)
            print(harga.replace('.',',').replace('_','.'))
        else:
            print('Data tidak valid')

    case 'R3':
        if daya > 6600:
            tarif = 1699.53
            harga = "Jumlah tagihan anda: {:_}".format(pemakaiaan*tarif)
            print(harga.replace('.',',').replace('_','.'))
        else:
            print('Data tidak valid')

    case 'B2':
        if daya >= 6600 and daya <= 200000:
            tarif = 1444.70
            harga = "Jumlah tagihan anda: {:_}".format(pemakaiaan*tarif)
            print(harga.replace('.',',').replace('_','.'))
        else:
            print('Data tidak valid')
    
    case 'B3':
        if daya >= 200000:
            tarif = 1114.74
            harga = "Jumlah tagihan anda: {:_}".format(pemakaiaan*tarif)
            print(harga.replace('.',',').replace('_','.'))
        else:
             print('Data tidak valid')
    
    case 'I3':
        if daya > 200000:
            tarif = 1314.12
            harga = "Jumlah tagihan anda: {:_}".format(pemakaiaan*tarif)
            print(harga.replace('.',',').replace('_','.'))
        else:
            print('Data tidak valid')
    
    case 'P1':
        if daya >= 6600 and daya <= 200000:
            tarif = 1523.28
            harga = "Jumlah tagihan anda: {:_}".format(pemakaiaan*tarif)
            print(harga.replace('.',',').replace('_','.'))
        else:
            print('Data tidak valid')
    case _:
        print("Data tidak valid")

            
